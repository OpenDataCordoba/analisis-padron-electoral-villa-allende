# -*- coding: utf-8 -*-
""" leer los padrones de Villa Allende para las elecciones de Intendente 2015 y obtener resultados """

import codecs
from slugify import slugify
import operator # for sorting
from tools.parsers import parse_calle

# columnas del CSV
""" 
path='Padron-Villa-Allende-2015.csv'
cols = ['N°ELECTOR', 'DNI', 'CLASE', 'APELLIDO', 'NOMBRE', 'Direccion', 
        'Nro Dir', 'Depto Otro', 'Profesion', 'Tipo DNI', 'Analf.', 
        'Sec.', 'Cir', 'Sexo', 'Mesa', 'Col.']
"""

path='Padron-Villa-Allende-2015-anonimizado.csv'
cols = ['N°ELECTOR', 'CLASE', 'Direccion', 
        'Nro Dir', 'Depto Otro', 'Profesion', 'Tipo DNI', 'Analf.', 
        'Sec.', 'Cir', 'Sexo', 'Mesa', 'Col.']

f = codecs.open(path, 'r', encoding='utf8')
raw=f.read()

votantes = raw.split('\n')

domicilios={} # lugar donde vive

for votante in votantes:
    if votante == '': break #last record
    v = votante.split(',')

    # domicilio
    calle = parse_calle(slugify(v[2]))
    nro = slugify(v[3])
    depto = slugify(v[4])
    domicilio = '{} {} {}'.format(calle, nro, depto)
    if not domicilios.get(domicilio, None): domicilios[domicilio] = 0
    domicilios[domicilio] += 1


# ordenar
print '=============================='
print 'DOMICILIOS y votantes'
print '=============================='
domicilios_sorted = sorted(domicilios.items(), key=operator.itemgetter(1), reverse=True)

dest = 'votantes-por-docimilio.csv'
f = codecs.open(dest, 'w', encoding='utf8')
f.write('domicilio,votantes\n')

#mostrar los dies primeros e imprimir a archivo solo los domicilios que tienen mas de 10 votantes
n = 1
for d in domicilios_sorted:
    if n<11: print str(d)
    n += 1
    f.write('{},{}\n'.format(d[0], d[1]))
    if int(d[1]) < 10:
        break 

print '=============================='
print 'saved as %s' % dest
print '=============================='
f.close()


# -*- coding: utf-8 -*-
""" parse info """

def parse_calle(calle):
    #TODO detectar mas errores
    calles={'jeronimo-l-de-cabrera': 'jeronimo-luis-de-cabrera',
            'j-l-de-cabrera': 'jeronimo-luis-de-cabrera',
            'g-l-de-cabrera': 'jeronimo-luis-de-cabrera',
            }

    return calles.get(calle, calle)
# -*- coding: utf-8 -*-
""" parse info """

def parse_calle(calle):
    #TODO detectar mas errores, necesitamos un openRefinero
    calles={'jeronimo-l-de-cabrera': 'jeronimo-luis-de-cabrera',
            'j-l-de-cabrera': 'jeronimo-luis-de-cabrera',
            'g-l-de-cabrera': 'jeronimo-luis-de-cabrera',
            'chacabuco-la-cruz': 'chacabuco',
            'bindustrial-chacabuco': 'chacabuco',
            'la-cruz-chacabuco': 'chacabuco',
            'industrial-chacabuco': 'chacabuco',
            'bla-cruz-chacabuco': 'chacabuco',
            'chacabuco-industrial-': 'chacabuco',
            'p-de-los-andes': 'paso-de-los-andes',
            'bcruz-paso-de-los-andes': 'paso-de-los-andes',
            'paso-de-los-andes-la-cruz': 'paso-de-los-andes',
            'blomas-barcelona': 'barcelona',
            'blomas-sur-barcelona': 'barcelona',
            'd-quiros': 'duarte-quiros',
            
            }

    return calles.get(calle, calle)
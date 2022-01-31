# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{

    'name': "tb_gescsc",
    'summary': 'Modulo de prueba para gestion CSC',
    'description':'Un modulo para gestionar un Cannabis Social Club',
    'author': 'Tribuladores',
    'website': 'https://tribuladores.com',
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'base',
    ],
    'data': [
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
}

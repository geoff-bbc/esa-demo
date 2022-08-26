# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "Dynamic Google Maps",

    'summary': """
        """,

    'description': """
    """,

    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','web','crm'],

    # always loaded
    'data': [
        'views/crm_google_maps.xml',
    ],
}

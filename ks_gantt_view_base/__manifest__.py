# -*- coding: utf-8 -*-
{
    'name': "Odoo Gantt View Base",

    'summary': """
        Base module contains framework for Gantt view project.
        """,

    'description': """
        odoo gantt view
        base for odoo gantt view
        odoo 14 gantt view base
        odoo gantt view base in 14
        Odoo Gantt Base
    """,
    'author': "Ksolves India Ltd.",
    'license': 'OPL-1',
    'currency': 'EUR',
    'price': 200.0,
    'website': "https://www.ksolves.com",
    'maintainer': 'Ksolves India Ltd.',
    'category': 'Tools',
    'version': '14.0.2',
    'support': 'sales@ksolves.com',
    'depends': ['base', 'base_setup'],
    'images': [
        "static/description/banner.jpg",
    ],
    'data': [
        'views/ks_gantt_view_assets.xml',
        'views/ks_res_config_settings_view.xml',
        'data/week_days_data.xml',
        'security/ir.model.access.csv',
    ],

    'qweb': [
        'static/src/xml/ks_gantt_view.xml',
        'static/src/xml/ks_recommend_color_picker.xml',
    ],
}

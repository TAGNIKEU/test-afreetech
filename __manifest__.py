# -*- coding: utf-8 -*-
{
    'name': "gestion_gic",

    'summary': """
        Un gic cultive et vend les fruits et légumes
        Ce gic a besoin d'un logiciel de gestion intégré""",

    'description': """
        Logiciel de gestion intégré qui permettra la gestion des la vente de leurs produits
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/remove_product_cron.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
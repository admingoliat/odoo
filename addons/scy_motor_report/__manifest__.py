# -*- coding: utf-8 -*-
{
    'name': "scy motor report",

    'summary': """
        Sale Report and product report
        """,

    'description': """
        Sale Report and product report
    """,

    'author': "WAKO Raoul",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'sale',
        'product',
        'stock',
    ],

    # always loaded
    'data': [
        'report/template.xml',
        'report/external_layout.xml',
        'report/report.xml',
        'views/product.xml',
        'views/sale_order.xml',
        'views/company.xml',
    ],

}

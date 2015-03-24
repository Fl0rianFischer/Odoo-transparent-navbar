# -*- coding: utf-8 -*-
{
    'name': "Bloopark Reports",

    'summary': """
    Provide custom report style""",

    'description': """
    Provide custom report style""",

    'author': "bloopark systems GmbH & Co. KG",
    'website': "http://www.bloopark.de",

    'category': 'Modal',
    'version': '1.0',

    'depends': [
        'base',
        'website',
        'sale_layout'
    ],
    'data': [
        'views/layout.xml',
        'views/invoice.xml',
        'views/style.xml',
        'views/res_company_view.xml',
        'views/quotation.xml'
    ],

    'demo': [
    ],

    'tests': [
    ],
}

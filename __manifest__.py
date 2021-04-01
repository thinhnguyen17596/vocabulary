{
    'name': "vocabulary",

    'summary': """
        Quản lý học từ vựng""",

    'description': """
        Ứng dụng quản lý việc học từ vựng
    """,


    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Education',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/words.xml',
        'views/meaning.xml',
        'views/example.xml',
        'views/test.xml',
        'views/quiz.xml',
        'views/category.xml',
        'views/student.xml',
        'views/learn_section.xml',
    ],
    'application': True,
    'installable': True,
}
# -*- coding: utf-8 -*-

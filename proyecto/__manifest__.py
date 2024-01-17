# -*- coding: utf-8 -*-
{
    'name': "Proyecto",

    'summary': """
        Gestión de prácticas en empresas para alumnos de 2 de DAM y DAW""",

    'description': """
        Este módulo proyecto va a consistir en un CRM para gestionar el 
        manejo de las practicas para los alumnos de segundolos cursos DAM
        y DAW del IES Laguna de Joatzel de Getafe
    """,

    'author': "Alex",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/data.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    #Indicamos que es una aplicación
        'application': True,
}

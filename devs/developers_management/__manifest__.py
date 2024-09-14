{
    'name': 'Developers Management',
    'version': '1.0',
    'category': 'Custom',
    'description': 'Module to manage developers',
    'author': 'Julia',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/developer_view.xml',
        'views/company_view.xml',
        'views/menuitems.xml'
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3'
}
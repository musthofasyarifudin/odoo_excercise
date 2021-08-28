# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'client_management',
    'version' : '1.1',
    'summary': 'Management Material',
    'sequence': -100,
    'description': """Management Material Software""",
    'category':'Productivity',
    'category': 'Accounting/Accounting',
    'website': 'https://www.odoomates.cl',
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/materials.xml',
        'views/template.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

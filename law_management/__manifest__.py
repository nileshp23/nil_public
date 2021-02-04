# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Law Management',
    'version' : '1.0',
    'summary': 'it is used to manage law case',
    'sequence': 15,
    'description': """
    This module is used to law management.
    """,
    'category': 'Sale',
    'author': 'Nilesh'
    'depends' : ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/law_matter.xml',
        'views/law_client.xml',
        'views/law_evidence.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}

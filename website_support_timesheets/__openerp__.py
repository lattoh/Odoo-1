{
    'name': "Website Help Desk / Support Ticket - Timesheets",
    'version': "1.0.1",
    'author': "Sythil Tech",
    'category': "Tools",
    'support': "steven@sythiltech.com.au",
    'summary':'Track time spend on tickets and send an invoice',
    'license':'LGPL-3',
    'data': [
        'views/website_support_ticket_views.xml',
        'data/website.support.ticket.states.csv',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'depends': ['website_support','project','account'],
    'images':[
        'static/description/1.jpg',
    ],
    'installable': True,
}
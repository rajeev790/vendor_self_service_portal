{
    'name': 'Vendor Self-Service Portal',
    'version': '1.0',
    'author': 'Your Name',
    'category': 'Sales',
    'summary': 'Vendor Portal for Viewing Forecasts and Submitting Order Adjustments',
    'description': """
        This module allows vendors to view forecasts for upcoming demand and submit order adjustment requests.
    """,
    'depends': ['base', 'sale', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/vendor_forecast_views.xml',
        'views/vendor_adjustment_request_views.xml',
        'views/vendor_self_service_portal_menus.xml',
        'data/email_template_data.xml',
    ],
    'installable': True,
    'application': False,
}
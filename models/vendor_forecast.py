from odoo import models, fields

class VendorForecast(models.Model):
    _name = 'vendor.forecast'
    _description = 'Vendor Forecast'

    product_id = fields.Many2one('product.product', string='Product', required=True)
    expected_quantity = fields.Integer(string='Expected Quantity', required=True)
    forecast_date = fields.Date(string='Forecast Date', required=True)
from odoo import models, fields, api

class VendorAdjustmentRequest(models.Model):
    _name = 'vendor.adjustment.request'
    _description = 'Vendor Adjustment Request'

    order_id = fields.Many2one('sale.order', string='Order Reference', required=True)
    adjustment_detail = fields.Text(string='Adjustment Detail', required=True)
    comment = fields.Text(string='Comment')

    @api.model
    def create(self, vals):
        record = super(VendorAdjustmentRequest, self).create(vals)
        template_id = self.env.ref('vendor_self_service_portal.email_template_vendor_adjustment').id
        self.env['mail.template'].browse(template_id).send_mail(record.id, force_send=True)
        return record
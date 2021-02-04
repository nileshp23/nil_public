from odoo import api, fields, models, _

class LawClient(models.Model):
    _name = "law.client"
    _description = "law matter name"
    _rec_name = 'client_name'

    name = fields.Char(string='Client Reference', required=True, copy=False, readonly=True,
                       index=True, default=lambda self: _('New'))
    client_name = fields.Char(string="Name", help="matter name")
    contact_no = fields.Integer(string="Contact No", help="client contact no")
    email = fields.Char(string="Email", help="client email id")


    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            seq_date = ""
            if vals:
                vals['name'] = self.env['ir.sequence'].next_by_code('law.client') or _('New')
            else:
                vals['name'] = self.env['ir.sequence'].next_by_code('law.client', sequence_date=seq_date) or _('New')
        result = super(LawClient, self).create(vals)
        return result

    def unlink(self):
        return super(LawClient, self).unlink()

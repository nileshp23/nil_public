from odoo import api, fields, models, _

class LawMatter(models.Model):
    _name = "law.matter"
    _description = "law matter name"

    name = fields.Char(string='Client Reference', required=True, copy=False, readonly=True,
                       index=True, default=lambda self: _('New'))
    matter_type = fields.Char(string="Matter type", help="matter type")
    matter_name  = fields.Char(string="Matter Name", help="matter name")
    client_id = fields.Many2one('law.client', string="Client Name", help="client id")
    open_date = fields.Datetime(string="Matter Open Date", help="matter open date")
    close_date = fields.Datetime(string="Close Date", help="matter close date")
    hearing_date = fields.Datetime(string="Hearing Date", help="Next Hearing date")
    trail_date = fields.Datetime(string="Trail Date", help="Next Hearing date")
    matter_state = fields.Selection([('draft','Deaft'),('open','Open'),('close','Close'),('done','Done')],
                                    string="State",default='draft', help="matter state")
    matter_result = fields.Selection([('won','Won'),('lose','Lose')], string="Matter Result", help="matter result")
    judge_name = fields.Char(string="Judge Name", help="judge name")
    apponant_name = fields.Char(string="Opponant Lawyer", help="apponant lawyer name")
    matter_category = fields.Char(string="Category",help="matter category")
    matter_description = fields.Html(string="Description")


    @api.model
    def create(self,vals):
        if vals.get('name', _('New')) == _('New'):
            seq_date=""
            if vals:
                vals['name'] = self.env['ir.sequence'].next_by_code('law.matter') or _('New')
            else:
                vals['name'] = self.env['ir.sequence'].next_by_code('law.matter', sequence_date=seq_date) or _('New')
        result = super(LawMatter, self).create(vals)
        return result

    def unlink(self):
        return super(LawMatter, self).unlink()

    def action_close(self):
        self.write({'matter_state': 'close'})

    def action_done(self):
        self.write({'matter_state': 'done'})

from odoo import api, fields, models, _

class LawMatter(models.Model):
    _name = "law.evidence"
    _description = "law evidence"

    evidence_name = fields.Char("Name",help="evidence name")
    attachment_data = fields.Binary(string="Attachment", help="attachment file")
    evidence_description = fields.Html(string="Description")


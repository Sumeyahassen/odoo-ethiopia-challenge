from odoo import fields, models

class VaultCredential(models.Model):
    _name = "vault.credential"
    _description = "Credential"

    name = fields.Char(required=True)
    project_id = fields.Many2one("vault.project", required=True, ondelete="cascade")
    environment = fields.Selection([
        ("production", "Production"),
        ("staging", "Staging"),
        ("development", "Development"),
        ("local", "Local"),
    ], default="development", required=True)
    username = fields.Char()
    password = fields.Char()
    url = fields.Char()
    notes = fields.Text()
    active = fields.Boolean(default=True)
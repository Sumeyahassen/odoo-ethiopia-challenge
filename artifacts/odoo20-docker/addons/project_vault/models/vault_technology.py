
from odoo import fields, models

class VaultTechnology(models.Model):
    _name = "vault.technology"
    _description = "Technology"

    name = fields.Char(required=True)
    category = fields.Selection([
        ("frontend", "Frontend"),
        ("backend", "Backend"),
        ("database", "Database"),
        ("hosting", "Hosting"),
        ("other", "Other"),
    ], default="other", required=True)
    color = fields.Integer()
    active = fields.Boolean(default=True)
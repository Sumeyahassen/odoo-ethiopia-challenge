from odoo import fields, models

class VaultProject(models.Model):
    _name = "vault.project"
    _description = "Project"

    name = fields.Char(required=True)
    slug = fields.Char(required=True)
    status = fields.Selection([
        ("active", "Active"),
        ("development", "In Development"),
        ("staging", "Staging"),
        ("completed", "Completed"),
        ("archived", "Archived"),
    ], default="development", required=True)
    github_url = fields.Char()
    live_url = fields.Char()
    staging_url = fields.Char()
    local_path = fields.Char()
    technology_ids = fields.Many2many("vault.technology", string="Tech Stack")
    active = fields.Boolean(default=True)
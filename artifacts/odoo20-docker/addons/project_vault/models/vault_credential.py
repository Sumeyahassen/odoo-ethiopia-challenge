# -*- coding: utf-8 -*-
from odoo import fields, models # type: ignore

class VaultCredential(models.Model):
    _name = "vault.credential"
    _description = "Project Credential"

    name = fields.Char(
        string="Credential Title",
        required=True,
        help="Name or description for this credential (e.g. 'Production Admin', 'Staging Database')",
    )
    project_id = fields.Many2one(
        "vault.project",
        string="Project",
        required=True,
        ondelete="cascade",
        help="The project this credential belongs to",
    )
    environment = fields.Selection([
        ("production", "Production"),
        ("staging", "Staging"),
        ("development", "Development"),
        ("local", "Local"),
    ], string="Environment", default="development", required=True)
    username = fields.Char(
        string="Username / Email",
        help="Login username, email, or client ID",
    )
    password = fields.Char(
        string="Password / Secret",
        help="Secret password or API token",
    )
    show_password = fields.Boolean(
        string="Show Password",
        default=True,
        help="Toggle to reveal or mask the password",
    )
    url = fields.Char(
        string="Login URL / Endpoint",
        help="Link to the login portal or API endpoint",
    )
    notes = fields.Text(
        string="Notes & Instructions",
        help="Additional instructions, port numbers, or setup steps",
    )
    active = fields.Boolean(
        string="Active",
        default=True,
    )

    def action_toggle_password(self):
        """Action button to toggle password visibility"""
        for rec in self:
            rec.show_password = not rec.show_password

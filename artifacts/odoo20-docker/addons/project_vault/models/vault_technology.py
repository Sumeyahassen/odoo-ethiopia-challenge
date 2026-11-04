# -*- coding: utf-8 -*-
from odoo import fields, models # type: ignore

class VaultTechnology(models.Model):
    _name = "vault.technology"
    _description = "Technology Stack"

    name = fields.Char(
        string="Technology Name",
        required=True,
        help="Name of the language, framework, database, or tool (e.g. React, PostgreSQL, Docker)",
    )
    category = fields.Selection([
        ("frontend", "Frontend"),
        ("backend", "Backend"),
        ("database", "Database"),
        ("hosting", "Hosting & Infrastructure"),
        ("other", "Other"),
    ], string="Category", default="other", required=True)
    color = fields.Integer(
        string="Color Index",
        help="Color tag index used for badges in views",
    )
    active = fields.Boolean(
        string="Active",
        default=True,
    )

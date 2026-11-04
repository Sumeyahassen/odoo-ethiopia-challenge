from odoo import fields, models # type: ignore

class VaultProject(models.Model):
    _name = "vault.project"
    _description = "Project Vault"

    name = fields.Char(
        string="Project Name",
        required=True,
        help="Full display name of the project",
    )
    slug = fields.Char(
        string="Project Code",
        required=True,
        help="Unique short code or slug for the project (e.g. 'water-dist', 'addis-tradelink')",
    )
    status = fields.Selection([
        ("development", "In Development"),
        ("staging", "Staging / Testing"),
        ("active", "Active / Live"),
        ("completed", "Completed"),
        ("archived", "Archived"),
    ], string="Status", default="development", required=True)
    github_url = fields.Char(
        string="GitHub Repository",
        help="URL to the GitHub or Git source code repository",
    )
    live_url = fields.Char(
        string="Live Production URL",
        help="Public URL of the live deployed system",
    )
    staging_url = fields.Char(
        string="Staging / Test URL",
        help="URL of the staging or test environment",
    )
    local_path = fields.Char(
        string="Local Project Path",
        help="Local file path on the developer machine",
    )
    technology_ids = fields.Many2many(
        "vault.technology",
        string="Technologies Used",
        help="Select frameworks, languages, databases, and tools used in this project",
    )
    credential_ids = fields.One2many(
        "vault.credential",
        "project_id",
        string="Credentials",
    )
    active = fields.Boolean(
        string="Active",
        default=True,
        help="Uncheck to archive this project without deleting it",
    )

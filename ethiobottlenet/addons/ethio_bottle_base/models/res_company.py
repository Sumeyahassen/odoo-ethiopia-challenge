from odoo import models, fields  # type: ignore


class ResCompany(models.Model):
    _inherit = 'res.company'

    factory_code = fields.Char(
        string='Factory Code',
        help='Short code identifying this factory/company'
    )
    is_factory = fields.Boolean(
        string='Is Water Factory',
        default=False
    )

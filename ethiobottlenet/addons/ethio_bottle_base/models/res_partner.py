from odoo import models, fields  # type: ignore


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_shop = fields.Boolean(
        string='Is Shop / Retailer',
        default=False,
        help='Check if this contact is a shop or retail point'
    )
    city_zone = fields.Char(
        string='City Zone',
        help='Example: Bole, Piazza, Adama Center, Hawassa Main...'
    )
    is_driver = fields.Boolean(
        string='Is Driver',
        default=False
    )

from odoo import models, fields # type: ignore


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    bottle_size = fields.Selection([
        ('0.3', '0.3 L'),
        ('0.6', '0.6 L'),
        ('1.0', '1 L'),
        ('1.5', '1.5 L'),
        ('2.0', '2 L'),
        ('20', '20 L Jar'),
        ('other', 'Other'),
    ], string='Bottle Size')

    is_bottled_water = fields.Boolean(
        string='Is Bottled Water',
        default=False
    )
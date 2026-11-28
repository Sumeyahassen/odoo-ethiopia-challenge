
from odoo import models, fields, _ # type: ignore
from odoo.exceptions import UserError # pyright: ignore[reportMissingImports]


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    ethio_delivery_count = fields.Integer(
        string='Delivery Orders',
        compute='_compute_ethio_delivery_count'
    )

    def _compute_ethio_delivery_count(self):
        Delivery = self.env['ethio.delivery.order']
        for order in self:
            order.ethio_delivery_count = Delivery.search_count([
                ('sale_order_id', '=', order.id)
            ])

    def action_create_ethio_delivery(self):
        self.ensure_one()
        if self.state not in ('sale', 'done'):
            raise UserError(_('Please confirm the Sales Order first.'))

        Delivery = self.env['ethio.delivery.order']
        lines = []
        for line in self.order_line:
            if line.product_id and line.product_id.type != 'service':
                lines.append((0, 0, {
                    'product_id': line.product_id.id,
                    'quantity': line.product_uom_qty,
                }))

        if not lines:
            raise UserError(_('No deliverable products found on this Sales Order.'))

        delivery = Delivery.create({
            'partner_id': self.partner_id.id,
            'sale_order_id': self.id,
            'factory_id': self.company_id.id,
            'planned_date': fields.Datetime.now(),
            'line_ids': lines,
        })

        return {
            'type': 'ir.actions.act_window',
            'name': _('Delivery Order'),
            'res_model': 'ethio.delivery.order',
            'res_id': delivery.id,
            'view_mode': 'form',
            'target': 'current',
        }

    def action_view_ethio_deliveries(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': _('Delivery Orders'),
            'res_model': 'ethio.delivery.order',
            'view_mode': 'list,form',
            'domain': [('sale_order_id', '=', self.id)],
            'context': {'default_sale_order_id': self.id},
        }
from odoo import models, fields, api, _  # type: ignore
from odoo.exceptions import UserError  # type: ignore


class AssignVehicleWizard(models.TransientModel):
    _name = 'assign.vehicle.wizard'
    _description = 'Assign Vehicle and Driver Wizard'

    delivery_id = fields.Many2one(
        'ethio.delivery.order',
        string='Delivery Order',
        required=True
    )
    vehicle_id = fields.Many2one(
        'fleet.vehicle',
        string='Vehicle',
        required=True
    )
    driver_id = fields.Many2one(
        'res.partner',
        string='Driver',
        domain="[('is_company', '=', False)]",
        required=True
    )

    def action_assign(self):
        for wizard in self:
            if not wizard.vehicle_id or not wizard.driver_id:
                raise UserError(_('Please select both a vehicle and a driver.'))
            wizard.delivery_id.write({
                'vehicle_id': wizard.vehicle_id.id,
                'driver_id': wizard.driver_id.id,
                'state': 'assigned',
            })
        return {'type': 'ir.actions.act_window_close'}

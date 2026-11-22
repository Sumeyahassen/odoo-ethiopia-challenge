from odoo import models, fields, api, _ # type: ignore
from odoo.exceptions import UserError # type: ignore


class EthioRoute(models.Model):
    _name = 'ethio.route'
    _description = 'Delivery Route'
    _order = 'date desc, id desc'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(
        string='Route Name',
        required=True,
        copy=False,
        default=lambda self: _('New')
    )
    date = fields.Date(
        string='Date',
        default=fields.Date.context_today,
        required=True,
        tracking=True
    )
    vehicle_id = fields.Many2one(
        'fleet.vehicle',
        string='Vehicle',
        tracking=True
    )
    driver_id = fields.Many2one(
        'res.partner',
        string='Driver',
        domain="[('is_company', '=', False)]",
        tracking=True
    )
    factory_id = fields.Many2one(
        'res.company',
        string='Factory',
        default=lambda self: self.env.company,
        tracking=True
    )
    stop_ids = fields.One2many(
        'ethio.route.stop',
        'route_id',
        string='Stops'
    )
    stop_count = fields.Integer(
        string='Stops',
        compute='_compute_stop_count'
    )
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='draft', tracking=True, copy=False)

    note = fields.Text(string='Notes')

    @api.depends('stop_ids')
    def _compute_stop_count(self):
        for rec in self:
            rec.stop_count = len(rec.stop_ids)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', _('New')) == _('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code('ethio.route') or _('New')
        return super().create(vals_list)

    def action_confirm(self):
        for rec in self:
            if not rec.vehicle_id or not rec.driver_id:
                raise UserError(_('Please select Vehicle and Driver.'))
            if not rec.stop_ids:
                raise UserError(_('Please add at least one stop.'))
            rec.state = 'confirmed'

    def action_start(self):
        for rec in self:
            rec.state = 'in_progress'

    def action_done(self):
        for rec in self:
            rec.state = 'done'
            for stop in rec.stop_ids:
                if stop.state == 'pending':
                    stop.state = 'done'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancelled'

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'
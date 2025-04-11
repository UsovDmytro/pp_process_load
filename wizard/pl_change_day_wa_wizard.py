import logging

from odoo import models, fields, api, _
from datetime import timedelta

_logger = logging.getLogger(__name__)


class PLChangeDayWA(models.TransientModel):
    """
    Change day WA
    """
    _name = 'pl.change.day.wa.wizard'
    _description = _('Change day WA')

    foreman_id = fields.Many2one(
        comodel_name='pl.foreman',
        string=_("Foreman"),
    )
    product_id = fields.Many2one(
        comodel_name='pl.product',
        string=_("Product"),
    )
    client_order_id = fields.Many2one(
        comodel_name='pl.client.order',
        string=_("Client order"),
    )

    wa_ids = fields.Many2many(
        comodel_name='pl.work.assignment',
        string=_('WA'),)

    days_change = fields.Integer()

    @api.model
    def default_get(self, fields):
        res = super().default_get(fields)
        print("Привет")
        if self.env.context.get('active_ids'):
            wa_ids = self.env['pl.work.assignment'].browse(self.env.context.get('active_ids'))
            res['wa_ids'] = [(6, 0, wa_ids.ids)]
        return res

    @api.onchange('foreman_id', 'product_id', 'client_order_id')
    def _onchange_data(self):
        domain = []
        if self.foreman_id:
            domain.append(('foreman_id', '=', self.foreman_id.id))
        if self.product_id:
            domain.append(('product_id', '=', self.product_id.id))
        if self.client_order_id:
            domain.append(('order_id', '=', self.client_order_id.id))

        if len(domain):
            wa_ids = self.env['pl.work.assignment'].search(domain)
            self['wa_ids'] = [(6, 0, wa_ids.ids)]


    def change_day_in_wa(self):
        """
        changes days for WA
         :return:
        """
        for record in self['wa_ids']:
            work_start_datetime_new = record.work_start_datetime + timedelta(days=self.days_change)
            work_finish_datetime_new = record.work_finish_datetime + timedelta(days=self.days_change)
            record.write({'work_start_datetime': work_start_datetime_new,
                          'work_finish_datetime': work_finish_datetime_new})

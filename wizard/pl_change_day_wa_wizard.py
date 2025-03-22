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

    pl_foreman_id = fields.Many2one(
        comodel_name='pl.foreman',
        string=_("Foreman"),
    )
    pl_product_id = fields.Many2one(
        comodel_name='pl.product',
        string=_("Product"),
    )
    pl_client_order_id = fields.Many2one(
        comodel_name='pl.client.order',
        string=_("Client order"),
    )

    pl_wa_ids = fields.Many2many(
        comodel_name='pl.work.assignment',
        string=_('WA'),)

    days_change = fields.Integer()

    @api.model
    def default_get(self, fields):
        res = super().default_get(fields)
        print("Привет")
        if self.env.context.get('active_ids'):
            pl_wa_ids = self.env['pl.work.assignment'].browse(self.env.context.get('active_ids'))
            res['pl_wa_ids'] = [(6, 0, pl_wa_ids.ids)]
        return res

    @api.onchange('pl_foreman_id', 'pl_product_id', 'pl_client_order_id')
    def _onchange_data(self):
        domain = []
        if self.pl_foreman_id:
            domain.append(('pl_foreman_id', '=', self.pl_foreman_id.id))
        if self.pl_product_id:
            domain.append(('pl_product_id', '=', self.pl_product_id.id))
        if self.pl_client_order_id:
            domain.append(('pl_order_id', '=', self.pl_client_order_id.id))

        if len(domain):
            pl_wa_ids = self.env['pl.work.assignment'].search(domain)
            self['pl_wa_ids'] = [(6, 0, pl_wa_ids.ids)]


    def change_day_in_wa(self):
        """
        changes days for WA
         :return:
        """
        for record in self['pl_wa_ids']:
            work_start_datetime_new = record.work_start_datetime + timedelta(days=self.days_change)
            work_finish_datetime_new = record.work_finish_datetime + timedelta(days=self.days_change)
            record.write({'work_start_datetime': work_start_datetime_new,
                          'work_finish_datetime': work_finish_datetime_new})

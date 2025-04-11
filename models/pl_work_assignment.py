import logging

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class PLWorkAssignment(models.Model):
    """
    Work assignment
    """
    _name = 'pl.work.assignment'
    _description = _('Work assignment')
    _rec_name = 'custom_name'
    state = fields.Selection(
        selection=[('plan', _('Заплановано')),
                   ('in_process', _('В процесі')),
                   ('done', _('Завершено'))],
        default="plan",
    )
    foreman_id = fields.Many2one(
        comodel_name='pl.foreman',
    )
    order_product_id = fields.Many2one(
        comodel_name='pl.order.product',
    )
    stage_id = fields.Many2one(
        comodel_name='pl.stage',
    )
    client_id = fields.Many2one(
        related='order_product_id.client_order_id.client_id',
        store=True,
    )
    order_id = fields.Many2one(
        related='order_product_id.client_order_id',
        store=True,
    )
    product_id = fields.Many2one(
        related='order_product_id.product_id',
        store=True,
    )
    process_id = fields.Char(
        related='stage_id.process',
        store=True,
    )

    work_start_datetime = fields.Datetime(required=True)
    work_finish_datetime = fields.Datetime(required=True)
    custom_name = fields.Char(
        string="Отображаемое имя",
        compute="_compute_custom_name",
        store=True,
    )
    readonly_form = fields.Boolean(
        compute="_compute_readonly_form",
        store=True,
    )


    # _sql_constraints = [
    #
    #     ('uniq', 'unique (pl_foreman_id,pl_order_product_id,pl_stage_id)',
    #      _('the foreman has a record of only one step for a product, '
    #        'if you need to redo it, remove the status of completed from the existing one.!')),
    #
    # ]

    @api.depends('foreman_id', 'order_product_id', 'stage_id')
    def _compute_custom_name(self):
        for record in self:
            record.custom_name = f"{record.foreman_id.name} / {record.order_id.order_number} / {record.product_id.abbreviation} / {record.stage_id.name}"
            record.client_id = record.order_product_id.client_order_id.client_id
            record.order_id = record.order_product_id.client_order_id
            record.product_id = record.order_product_id.product_id
            record.process_id = record.stage_id.process

    @api.depends('state')
    def _compute_readonly_form(self):
        for record in self:
            record.readonly_form = record.state == 'done'

    # def name_get(self):
    #     return [(rec.id, "%s %s %s %s" % (rec.pl_foreman_id.name,
    #                                       rec.pl_order_id.pl_order_number,
    #                                       rec.pl_product_id.abbreviation,
    #                                       rec.pl_stage_id.name))
    #             for rec in self]


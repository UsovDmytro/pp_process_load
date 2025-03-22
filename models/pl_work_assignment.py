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
    pl_foreman_id = fields.Many2one(
        comodel_name='pl.foreman',
        string=_("Foreman"),
    )
    pl_order_product_id = fields.Many2one(
        comodel_name='pl.order.product',
        string=_("Order Product"),
    )
    pl_stage_id = fields.Many2one(
        comodel_name='pl.stage',
        string=_("Stage"),
    )
    pl_client_id = fields.Many2one(
        related='pl_order_product_id.pl_client_order_id.pl_client_id',
        string=_("Client"),
    )
    pl_order_id = fields.Many2one(
        related='pl_order_product_id.pl_client_order_id',
        string=_("Client order"),
    )
    pl_product_id = fields.Many2one(
        related='pl_order_product_id.pl_product_id',
        string=_("Product"),
    )
    pl_process_id = fields.Char(
        related='pl_stage_id.pl_process',
        string=_("Process"),
    )

    work_start_datetime = fields.Datetime(required=True)
    work_finish_datetime = fields.Datetime(required=True)
    custom_name = fields.Char(
        string="Отображаемое имя",
        compute="_compute_custom_name"
    )


    # _sql_constraints = [
    #
    #     ('uniq', 'unique (pl_foreman_id,pl_order_product_id,pl_stage_id)',
    #      _('the foreman has a record of only one step for a product, '
    #        'if you need to redo it, remove the status of completed from the existing one.!')),
    #
    # ]

    @api.depends('pl_foreman_id', 'pl_order_product_id', 'pl_stage_id')
    def _compute_custom_name(self):
        for record in self:
            # Формируем строку из нужных полей, можно добавить любые нужные элементы
            record.custom_name = f"{record.pl_foreman_id.name} / {record.pl_order_id.pl_order_number} / {record.pl_product_id.abbreviation} / {record.pl_stage_id.name}"

    # def name_get(self):
    #     return [(rec.id, "%s %s %s %s" % (rec.pl_foreman_id.name,
    #                                       rec.pl_order_id.pl_order_number,
    #                                       rec.pl_product_id.abbreviation,
    #                                       rec.pl_stage_id.name))
    #             for rec in self]


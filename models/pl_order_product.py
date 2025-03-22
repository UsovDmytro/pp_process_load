import logging

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class PLOrderProduct(models.Model):
    """
    Order product
    """
    _name = 'pl.order.product'
    _description = _('Order Product')
    _rec_name = 'custom_name'
    pl_product_id = fields.Many2one(
        comodel_name='pl.product',
        string=_("Product"),
    )
    pl_quantity = fields.Integer()

    pl_client_order_id = fields.Many2one(
        comodel_name='pl.client.order',
        string=_("Client order"),
    )
    custom_name = fields.Char(
        string="Отображаемое имя",
        compute="_compute_custom_name"
    )
    @api.depends('pl_product_id', 'pl_client_order_id')
    def _compute_custom_name(self):
        for record in self:
            # Формируем строку из нужных полей, можно добавить любые нужные элементы
            record.custom_name = f"{record.pl_product_id.name} / {record.pl_client_order_id.pl_order_number}"

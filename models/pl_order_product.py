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
    product_id = fields.Many2one(
        comodel_name='pl.product',
    )
    quantity = fields.Integer()

    client_order_id = fields.Many2one(
        comodel_name='pl.client.order',
    )
    custom_name = fields.Char(
        string="Отображаемое имя",
        compute="_compute_custom_name"
    )
    @api.depends('product_id', 'client_order_id')
    def _compute_custom_name(self):
        for record in self:
            record.custom_name = f"{record.product_id.name} / {record.client_order_id.order_number}"

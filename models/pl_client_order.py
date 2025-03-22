import logging

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class PLClientOrder(models.Model):
    """
    Client order
    """
    _name = 'pl.client.order'
    _description = _('Client order')
    _rec_name = 'pl_order_number'
    pl_order_number = fields.Char()


    pl_client_id = fields.Many2one(
        comodel_name='pl.client',
        string=_("Client"),
    )

    pl_order_product_ids = fields.One2many(comodel_name='pl.order.product', inverse_name='pl_client_order_id',
                                           string=_("Order products"),)


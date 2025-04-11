import logging

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class PLClient(models.Model):
    """
    Client
    """
    _name = 'pl.client'
    _description = _('Client')

    name = fields.Char()

    client_order_ids = fields.One2many(comodel_name='pl.client.order', inverse_name='client_id',
                                       string=_("Orders"),)


import logging

from odoo import models, fields, _

_logger = logging.getLogger(__name__)


class PLProduct(models.Model):
    """
    Product
    """
    _name = 'pl.product'
    _description = _('Product')

    name = fields.Char()
    abbreviation = fields.Char()
    active = fields.Boolean(
        default=True, )

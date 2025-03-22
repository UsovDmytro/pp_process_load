import logging

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class PLForeman(models.Model):
    """
    Foreman
    """
    _name = 'pl.foreman'
    _description = 'Бригадир'

    name = fields.Char()



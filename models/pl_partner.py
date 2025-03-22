import logging

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class PLPartner(models.Model):
    """
    Client
    """
    _inherit = 'res.partner'

    pl_client_id = fields.Many2one('pl.client')


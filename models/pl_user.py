import logging

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class PLUser(models.Model):
    """
    Foreman
    """
    _inherit = 'res.users'
    pl_foreman_id = fields.Many2one('pl.foreman')


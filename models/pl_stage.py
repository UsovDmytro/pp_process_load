import logging

from odoo import models, fields, _

_logger = logging.getLogger(__name__)


class PLStage(models.Model):
    """
    Stage
    """
    _name = 'pl.stage'
    _description = _('Stage')

    name = fields.Char()
    pl_process = fields.Char()

    # pl_process = fields.Selection(
    #     selection=[('slicing', _('slicing')),
    #                ('painting', _('painting')),
    #                ('assembly', _('assembly'))],
    # )
    active = fields.Boolean(
        default=True, )

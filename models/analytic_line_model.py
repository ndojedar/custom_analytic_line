# -*- coding: utf-8 -*-

from odoo import models, fields


class CustomAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    manager_id = fields.Many2one(
        string="Resp. de Proyecto",
        comodel_name="res.users",
        related="task_id.manager_id",
        store=True,
        readonly=True
    )

    bam_id = fields.Many2one(
        string="Business Area Manager",
        comodel_name="res.users",
        related="task_id.business_area_manager_id",
        store=True,
        readonly=True
    )

# -*- coding: utf-8 -*-

from odoo import fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    mode_de_financement = fields.Selection(
        selection=[
            ('SCE', 'SCE'),
            ('UBA', 'UBA'),
            ('CASH', 'CASH'),
            ('SCB', 'SCB'),
            ('BACM', 'BACM'),
            ('ALIOS FINANCE', 'ALIOS FINANCE'),
            ('AFRILAND FIRST BANK', 'AFRILAND FIRST BANK'),
        ],
        string='Mode de Financement'
    )


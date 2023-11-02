# -*- coding: utf-8 -*-

from odoo import fields, models

class ResCompany(models.Model):
    _inherit = 'res.company'

    entete = fields.Binary(
        string='Image Entete'
    )

    pieds = fields.Binary(
        string='Image pieds de page'
    )
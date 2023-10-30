# -*- coding: utf-8 -*-

from odoo import fields, models

class ProductProduct(models.Model):
    _inherit = 'product.product'

    source_dnergie = fields.Char(
        string="Source D'Energir"
    )

    nombre_de_place = fields.Char(
        string="Nombre de Place"
    )

    genre = fields.Char(
        string="Genre"
    )

    type_moteur = fields.Char(
        string="Type Moteur"
    )

    caracteristique_techinque = fields.Char(
        string="Carcteristique technique"
    )

    marque = fields.Char(
        string="Marque"
    )

    nombre_de_places = fields.Char(
        string='Nombre de Place'
    )

    puissance_administrative = fields.Char(
            string="Puissance Administrative"
    )

    equipement = fields.Text(
        string="Equipement"
    )

    caracteristique_technique = fields.Text(
        string="Caracteristiques Techiniques"
    )

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    source_dnergie = fields.Char(
        string="Source D'Energir"
    )

    nombre_de_place = fields.Char(
        string="Nombre de Place"
    )

    genre = fields.Char(
        string="Genre"
    )

    type_m = fields.Char(
        string="Type"
    )

    marque = fields.Char(
        string="Marque"
    )

    puissance_administrative = fields.Char(
            string="Puissance Administrative"
    )

    type_moteur = fields.Char(
        string='Type Moteur'
    )

    nombre_de_places = fields.Char(
        string='Nombre de Place'
    )

    equipement = fields.Text(
        string="Equipement"
    )

    caracteristique_technique = fields.Text(
        string="Caracteristiques Techiniques"
    )


 # -*- coding: utf-8 -*-

from odoo import fields, models

class ProductProduct(models.Model):
    _inherit = 'product.product'

    source_dnergie = fields.Char(
        string="Source D'Energir"
    )

    genre = fields.Char(
        string="Genre"
    )

    type_moteur = fields.Char(
        string="Type Moteur"
    )

    type_m = fields.Char(
        string="Type"
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

    caracteristiques_techniques = fields.Text(
        string="Caracteristiques Techiniques"
    )

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    source_dnergie = fields.Char(
        string="Source D'Energir"
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
        string="Equipements"
    )

    caracteristiques_techniques = fields.Text(
        string="Caracteristiques Techiniques"
    )


    def write(self, values):
        res = super(ProductTemplate, self).write(values)

        val = {}

        if 'caracteristiques_techniques' in values:
            val['caracteristiques_techniques'] = values['caracteristiques_techniques']

        if 'equipement' in values:
            val['equipement'] = values['equipement']

        if 'nombre_de_places' in values:
            val['nombre_de_places'] = values['nombre_de_places']

        if 'type_moteur' in values:
            val['type_moteur'] = values['type_moteur']

        if 'puissance_administrative' in values:
            val['puissance_administrative'] = values['puissance_administrative']

        if 'marque' in values:
            val['marque'] = values['marque']

        if 'type_m' in values:
            val['type_m'] = values['type_m']

        if 'genre' in values:
            val['genre'] = values['genre']

        if 'source_dnergie' in values:
            val['source_dnergie'] = values['source_dnergie']

        if val:
            self.product_variant_ids.write(val)

        return res

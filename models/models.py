# -*- coding: utf-8 -*-

from odoo import models, fields, api


# définition de la classe produit qui hérite de product.template


class Produit(models.Model):
    # _name = 'gestion_gic.produit'
    _description = 'Informations des produits'
    _inherit = 'product.template'

    qualite = fields.Selection([('frais', 'Frais'), ('recent', 'Récent'), ('fletri', 'Flétri')],
                               string='Etat du produit', compute='compute_qualite_recolte', readonly=True, store=True)
    recolte = fields.Date(string='Date récolte', default=fields.Date.today())
    date_jour = fields.Date.today()
    diff_jour = fields.Integer(string='Différence de jours', readonly=True)

    # Calecul du la durée en jour du fruit et définition des états du produit
    @api.depends('recolte', 'diff_jour')
    def compute_qualite_recolte(self):
        for rec in self:
            if rec.recolte and rec.date_jour:
                rec.diff_jour = (rec.date_jour - rec.recolte).days
                if rec.diff_jour > 3:
                    rec.qualite = 'fletri'
                elif rec.diff_jour in [2, 3]:
                    rec.qualite = 'recent'
                else:
                    rec.qualite = 'frais'

    # retrait du produit du stock après plus de 7 jours sans être vendu
    @api.multi
    def remove_from_stock(self):
        for prod in self:
            while (prod.create_date - prod.date_jour).days > 7:
                prod.unlink()

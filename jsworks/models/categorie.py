from odoo import api,fields, models, exceptions

class Categorie(models.Model):
    _name= "jsworks.categorie"
    _description = "Categorie"
    _rec_name = "Symbol"

    Symbol=fields.Char()
    Description=fields.Char()
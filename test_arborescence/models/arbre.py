from odoo import api,fields, models, exceptions

class Arbre(models.Model):
    _name= "test_arborescence.arbre"
    _description = "Arbre"

    Name=fields.Char()
    Parent=fields.Many2one("test_arborescence.arbre") 
    Enfants=fields.One2many("test_arborescence.arbre","Parent")

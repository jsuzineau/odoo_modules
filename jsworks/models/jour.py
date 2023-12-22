from odoo import api,fields, models, exceptions

class Jour(models.Model):
    _name= "jsworks.jour"
    _description = "Jour"
    _rec_name = "D"

    D=fields.Date()
    def action_Connecte_Works(self):
        works= self.env['jsworks.work'].search([("D","=",self.D)])
        for w in works:
            w.Jour = self

    Works=fields.One2many("jsworks.work","Jour")

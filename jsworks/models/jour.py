from odoo import api,fields, models, exceptions

class Jour(models.Model):
    _name= "jsworks.jour"
    _description = "Jour"
    _rec_name = "D"

    D=fields.Date()
    def action_Connecte_Works(self):
        works= self.env['jsworks.work'].search([("D","=",self.D),("partner_id.id","=",self.partner_id.id)])
        for w in works:
            w.Jour = self
    def action_Facture(self):
        print ("Parent jsworks.Jour.action_Facture")
        return True
    partner_id=fields.Many2one('res.partner', index=True)

    Works=fields.One2many("jsworks.work","Jour")

from odoo import api,fields, models, exceptions

class Temps(models.Model):
    _name= "jsworks.temps"
    _description = "Temps"
    _rec_name = "Debut"

    Debut=fields.Date()
    Fin  =fields.Date()
    Description=fields.Text()
    def action_Connecte_Works(self):
        works= self.env['jsworks.work'].search([("D",">=",self.Debut),("D","<=",self.Fin),("partner_id.id","=",self.partner_id.id)])
        for w in works:
            w.Temps = self
    def action_Facture(self):
        print ("Parent jsworks.Jour.action_Facture")
        return True
    partner_id=fields.Many2one('res.partner', index=True)

    Works=fields.One2many("jsworks.work","Temps")

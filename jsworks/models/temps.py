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
            for t in w.Tags:
                if not (t.id in [tt.Tag.id for tt in self.Tags]):
                    #self.update({'Tags': [(fields.Command.link(t.id))] })
                    self.update({'Tags': [(fields.Command.create({'Tag': t.id}))]})
                for tt in (tt for tt in self.Tags if tt.Tag.id == t.id):
                    if not (w.id in [ w.id for w in tt.Works]):
                        tt.update({'Works': [(fields.Command.link(w.id))]})


    def action_Facture(self):
        print ("Parent jsworks.Jour.action_Facture")
        return True
    partner_id=fields.Many2one('res.partner', index=True)

    Works= fields.One2many("jsworks.work","Temps")

    Duree = fields.Float(compute="_compute_Duree", digits=(10,2))
    @api.depends("Works")
    def _compute_Duree(self):
        for record in self:
            record.Duree= sum([w.Duree for w in record.Works])

    Taux_horaire = fields.Float()
    Tags = fields.One2many("jsworks.temps_tag","Temps")

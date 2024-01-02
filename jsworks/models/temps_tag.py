from odoo import api,fields, models, exceptions

class Temps_Tag(models.Model):
    _name= "jsworks.temps_tag"
    _description = "Temps_Tag"
    _rec_name = "Tag"

    Temps=fields.Many2one("jsworks.temps")
    Tag=fields.Many2one("jsworks.tag")
    Works = fields.Many2many("jsworks.work")

    Duree = fields.Float(compute="_compute_Duree", digits=(10,2))
    @api.depends("Works")
    def _compute_Duree(self):
        for record in self:
            record.Duree= sum([w.Duree for w in record.Works])

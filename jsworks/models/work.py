from odoo import api,fields, models, exceptions

class Work(models.Model):
    _name= "jsworks.work"
    _description = "Work"
    _rec_name = "Beginning"

    partner_id=fields.Many2one('res.partner', index=True)
    Beginning=fields.Datetime( default=lambda self : fields.Datetime.now())
    @api.onchange("Beginning")
    def _onchange_Beginning(self):
        self._D_from_Beginning()

    End=fields.Datetime()
    def action_Arreter(self):
        for record in self:
            record.End= fields.Datetime.now()
        return True
    def action_Redemarrer(self):
        self.action_Arreter()
        self.env['jsworks.work'].create({'Project': self.Project, 'Description':"créé par action_Redemarrer"})
        return True

    Description=fields.Text()

    Project = fields.Many2one("jsworks.project")

    Developments=fields.One2many("jsworks.development","CreationWork")

    D=fields.Date()
    def _D_from_Beginning(self):
        if self.Beginning:
            self.D= fields.Date.to_date(self.Beginning)

    Jour = fields.Many2one("jsworks.jour")
    Temps = fields.Many2one("jsworks.temps")

    Duree = fields.Float(compute="_compute_Duree")

    def _calcule_Duree_interne(self, work):
        delta = work.End - work.Beginning
        result=   delta.total_seconds() / 3600
        print("delta:", delta, "  result=", result)
        return result

    @api.depends("Beginning")
    @api.depends("End")
    def _compute_Duree(self):
        for record in self:
            record.Duree= self._calcule_Duree_interne( record)
    def action_calcule_Duree(self):
        self.Duree = self._calcule_Duree_interne( self)
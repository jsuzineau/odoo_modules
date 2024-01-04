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

    Temps = fields.Many2one("jsworks.temps")

    Duree = fields.Float(compute='_compute_Duree', digits=(10,2), store=True)
    @api.depends("Beginning")
    @api.depends("End")
    def _compute_Duree(self):
        for work in self:
            if work and work.End:
                delta = work.End - work.Beginning
                work.Duree= delta.total_seconds() / 3600
                print("delta:", delta, "  work.Duree=", work.Duree)

    Tags=fields.Many2many("jsworks.tag")

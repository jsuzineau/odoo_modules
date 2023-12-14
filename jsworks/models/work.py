from odoo import api,fields, models, exceptions

class Work(models.Model):
    _name= "jsworks.work"
    _description = "Work"
    _rec_name = "Beginning"

    Beginning=fields.Datetime( default=lambda self : fields.Datetime.now())
    End=fields.Datetime()
    Description=fields.Text()
    Project = fields.Many2one("jsworks.project")
    Developments=fields.One2many("jsworks.development","CreationWork")
    def action_Arreter(self):
        for record in self:
            record.End= fields.Datetime.now()
        return True
    def action_Redemarrer(self):
        self.action_Arreter()
        self.env['jsworks.work'].create({'Project': self.Project, 'Description':"créé par action_Redemarrer"})
        return True

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

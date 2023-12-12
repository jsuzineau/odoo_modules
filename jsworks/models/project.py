from odoo import api,fields, models, exceptions

class Project(models.Model):
    _name= "jsworks.project"
    _description = "Project"
    _rec_name = "Name"

    Name        = fields.Char()
    Developments= fields.One2many("jsworks.development", "Project")
    Works       = fields.One2many("jsworks.work"       , "Project")

from odoo import api,fields, models, exceptions

class Work(models.Model):
    _name= "jsworks.work"
    _description = "Work"

    nProject=fields.Integer()
    Beginning=fields.Char()
    End=fields.Char()
    Description=fields.Char()
    nUser=fields.Integer() 
#models_class.py_many_to_one_creation_line
    Development=fields.One2many("jsworks.development","CreationWork") 

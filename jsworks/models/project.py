from odoo import api,fields, models, exceptions

class Project(models.Model):
    _name= "jsworks.project"
    _description = "Project"

    Name=fields.Char() 
#models_class.py_many_to_one_creation_line
#models_class.py_one_to_many_creation_line
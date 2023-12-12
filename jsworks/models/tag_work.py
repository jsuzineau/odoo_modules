from odoo import api,fields, models, exceptions

class Tag_Work(models.Model):
    _name= "jsworks.tag_work"
    _description = "Tag_Work"

    idTag=fields.Integer()
    idWork=fields.Integer() 
#models_class.py_many_to_one_creation_line
#models_class.py_one_to_many_creation_line

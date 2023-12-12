from odoo import api,fields, models, exceptions

class Tag(models.Model):
    _name= "jsworks.tag"
    _description = "Tag"

    idType=fields.Integer()
    Name=fields.Char() 
#models_class.py_many_to_one_creation_line
#models_class.py_one_to_many_creation_line

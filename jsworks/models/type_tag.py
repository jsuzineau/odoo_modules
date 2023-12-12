from odoo import api,fields, models, exceptions

class Type_Tag(models.Model):
    _name= "jsworks.type_tag"
    _description = "Type_Tag"

    Name=fields.Char() 
#models_class.py_many_to_one_creation_line
#models_class.py_one_to_many_creation_line

from odoo import api,fields, models, exceptions

class Tag_Development(models.Model):
    _name= "jsworks.tag_development"
    _description = "Tag_Development"

    idTag=fields.Integer()
    idDevelopment=fields.Integer() 
#models_class.py_many_to_one_creation_line
#models_class.py_one_to_many_creation_line

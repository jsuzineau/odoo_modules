from odoo import api,fields, models, exceptions

class Tag(models.Model):
    _name= "jsworks.tag"
    _description = "Tag"
    _rec_name = "Name"

    Name=fields.Char()
    Type=fields.Many2one("jsworks.type_tag")
#models_class.py_many_to_one_creation_line
#models_class.py_one_to_many_creation_line

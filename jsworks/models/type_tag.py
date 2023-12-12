from odoo import api,fields, models, exceptions

class Type_Tag(models.Model):
    _name= "jsworks.type_tag"
    _description = "Type_Tag"
    _rec_name = "Name"

    Name=fields.Char()
    Tags = fields.One2many("jsworks.tag", "Type")

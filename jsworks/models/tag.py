from odoo import api,fields, models, exceptions

class Tag(models.Model):
    _name= "jsworks.tag"
    _description = "Tag"
    _rec_name = "Name"

    Name=fields.Char()
    Type=fields.Many2one("jsworks.type_tag")
    Works = fields.Many2many("jsworks.work")

from odoo import api,fields, models, exceptions

class State(models.Model):
    _name= "jsworks.state"
    _description = "State"
    _rec_name = "Symbol"

    Symbol=fields.Char()
    Description=fields.Char() 
#models_class.py_many_to_one_creation_line
#models_class.py_one_to_many_creation_line

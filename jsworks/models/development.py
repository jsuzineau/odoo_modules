from odoo import api,fields, models, exceptions

class Development(models.Model):
    _name= "jsworks.development"
    _description = "Development"
    _rec_name = "Description"

    Description=fields.Text()
    Steps=fields.Text()
    Origin=fields.Text()
    Solution=fields.Text()
    isBug=fields.Boolean()
    Project=fields.Many2one("jsworks.project")
    State=fields.Many2one("jsworks.state")
    CreationWork=fields.Many2one("jsworks.work")
    SolutionWork=fields.Many2one("jsworks.work")
    Categorie=fields.Many2one("jsworks.categorie")
#models_class.py_one_to_many_creation_line

from odoo import api,fields, models, exceptions

class Development(models.Model):
    _name= "jsworks.development"
    _description = "Development"

    nProject=fields.Integer()
    nState=fields.Integer()
    nCreationWork=fields.Integer()
    nSolutionWork=fields.Integer()
    Description=fields.Char()
    Steps=fields.Char()
    Origin=fields.Char()
    Solution=fields.Char()
    nCategorie=fields.Integer()
    isBug=fields.Integer()
    nDemander=fields.Integer()
    nSheetRef=fields.Integer() 
    Project=fields.Many2one("jsworks.project")
    State=fields.Many2one("jsworks.state")
    CreationWork=fields.Many2one("jsworks.work")
    SolutionWork=fields.Many2one("jsworks.work")
    Categorie=fields.Many2one("jsworks.categorie")
    #Demander=fields.Many2one("jsworks.demander")
    #SheetRef=fields.Many2one("jsworks.sheetref")
#models_class.py_one_to_many_creation_line

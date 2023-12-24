from odoo import api,fields, models, exceptions, Command


class Temps(models.Model):
    _inherit = "jsworks.temps"

    def action_Facture(self):
        print ("jsworks_account.Temps.action_Facture")
        #invoice_vals_list = [{"partner_id.id":self.partner_id.id}]
        #moves = self.env['account.move'].sudo().with_context(default_move_type='out_invoice').create(invoice_vals_list)
        vals={
             "partner_id":self.partner_id.id,
             "move_type":"out_invoice",
             "journal_id":1,
             "invoice_line_ids": [
                                 Command.create(
                                               {
                                               "name":"Temps",
                                               "quantity":10,
                                               "price_unit":30
                                               }
                                               )
                                 ]
             }
        self.env['account.move'].create(vals)
        return super(Temps,self).action_Facture()

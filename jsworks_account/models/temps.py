from odoo import api,fields, models, exceptions, Command


class Temps(models.Model):
    _inherit = "jsworks.temps"

    Facture= fields.Many2one("account.move")
    def action_Facture(self):
        if (self.Facture):
          return

        print ("jsworks_account.Temps.action_Facture")
        #invoice_vals_list = [{"partner_id.id":self.partner_id.id}]
        #moves = self.env['account.move'].sudo().with_context(default_move_type='out_invoice').create(invoice_vals_list)
        vals=\
          {
          "partner_id":self.partner_id.id,
          "move_type":"out_invoice",
          "journal_id":1,
          "invoice_line_ids":\
              [
              Command.create\
                 ({
                 "name":"Temps",
                 "quantity":self.Duree,
                 "price_unit":self.Taux_horaire
                 })
              ]
          }
        self.Facture=self.env['account.move'].create(vals)
        return super(Temps,self).action_Facture()

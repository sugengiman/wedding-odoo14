from odoo import api, fields, models


class OrderKursiTamu(models.Model):
    _name = 'wedding.orderkursitamu'
    _description = 'New Description'

    orderkursi_ids = fields.One2many(comodel_name='wedding.orderkursitamu', inverse_name='orderkursi_id', string='Kode Order')
    name = fields.Char(string='Kode Order')

class OrderKursiTamu_Detail(models.Model):
    _name = 'module.orderkursitamu_detail'
    _description = 'New Description'

    orderkursi_id = fields.Many2one(comodel_name='wedding.orderkursitamu', string='Order')
    kursi_id = fields.Many2one(comodel_name='wedding.kursitamu', string='Kursi Tamu')
    name = fields.Char(string='Name')
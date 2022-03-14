from odoo import api, fields, models


class Panggung(models.Model):
    _name = 'wedding.panggung'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    pelaminan = fields.Char(string='Tipe Pelaminan')
    bunga = fields.Selection(string='Tipe Bunga', selection=[('bunga mati', 'Bunga Mati'),('bunga hidup', 'Bunga Hidup')])
    accesories = fields.Char(string='Accesories')
    harga = fields.Integer(string='Harga')
    
    
    

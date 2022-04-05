from odoo import api, fields, models


class Pelaminan(models.Model):
    _name = 'wedding.pelaminan'
    _description = 'Deskripsi Pelaminan'

    name = fields.Char(string='Nama', required=True)
    deskripsi = fields.Char(string='Deskripsi Pelaminan', required=True)
    harga = fields.Integer(string='Harga Sewa', required=True)
    
    

from odoo import api, fields, models


class Pelaminan(models.Model):
    _name = 'wedding.pelaminan'
    _description = 'Deskripsi Pelaminan'

    name = fields.Char(string='Nama')
    deskripsi = fields.Char(string='Deskripsi Pelaminan')
    harga = fields.Integer(string='Harga Sewa')
    
    

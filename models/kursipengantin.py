from odoo import api, fields, models


class Kursi_Pengantin (models.Model):
    _name = 'wedding.kursipengantin'
    _description = 'Daftar Kursi Pengantin'

    name = fields.Char(string='Nama', required=True)
    deskripsi = fields.Char(string='Deskripsi', required=True)
    harga = fields.Integer(string='Harga Sewa', required=True)
    
    

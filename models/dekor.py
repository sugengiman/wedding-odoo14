from odoo import api, fields, models


class Dekor(models.Model):
    _name = 'wedding.dekor' #nama tabel dan nama model
    _description = 'Model untuk tabel dekor'

    name = fields.Char(string='Nama Dekorasi')
    harga = fields.Integer(string='Harga Dekorasi') #ofint
    deskripsi = fields.Char(string='Deskripsi Dekorasi') #ofchar

    

    
from odoo import api, fields, models


class Kursi_Tamu(models.Model):
    _name = 'wedding.kursitamu'
    _description = 'Deskripsi Kursi Tamu'

    name = fields.Char(string='Name', required=True)
    tipe = fields.Selection(string='Tipe Kursi', selection=[('plastik', 'Plastik'), ('besi', 'Besi'), ('kayu', 'Kayu'),], required=True)
    deskripsi = fields.Char(string='Deskripsi', required=True)
    stock = fields.Integer(string='Stock', required=True)    
    harga = fields.Integer(string='Harga', required=True)


    
    

from tracemalloc import DomainFilter
from odoo import api, fields, models


class Panggung(models.Model):
    _name = 'wedding.panggung'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    # pelaminan = fields.Char(string='Tipe Pelaminan')
    pelaminan = fields.Many2one(comodel_name='wedding.pelaminan', 
                                string='Tipe Pelaminan', 
                                required=True, #membuat form harus diisi
                                domain=[('harga','>','15000000',)] #membuat filter pada bagian pelaminan dengan harga tertentu 
                                )
    bunga = fields.Selection(string='Tipe Bunga', selection=[('bunga mati', 'Bunga Mati'),('bunga hidup', 'Bunga Hidup')], required=True)
    accesories = fields.Char(string='Accesories') 
    # harga = fields.Integer(string='Harga')
    harga = fields.Char(compute='_compute_harga', string='Harga Sewa') #oofcompute digunakan untuk membuat menghitung beberapa nilai pada inputan lain

    @api.depends('pelaminan')
    def _compute_harga(self):
        for record in self:
            record.harga = record.pelaminan.harga
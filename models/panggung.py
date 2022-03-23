from tracemalloc import DomainFilter
from odoo import api, fields, models


class Panggung(models.Model):
    _name = 'wedding.panggung'
    _description = 'New Description'

    name = fields.Char(string='Nama', required=True)
    # pelaminan = fields.Char(string='Tipe Pelaminan')
    # pelaminan_id = fields.Many2one(comodel_name='wedding.pelaminan', 
    #                             string='Tipe Pelaminan', 
    #                             required=True, #membuat form harus diisi
    #                             domain=[('harga','>','15000000',)] #membuat filter pada bagian pelaminan dengan harga tertentu 
    #                             )
    pelaminan = fields.Many2one(comodel_name='wedding.pelaminan', 
                                string='Tipe Pelaminan', 
                                required=True)
    kursipengantin = fields.Many2one(comodel_name='wedding.kursipengantin', 
                                string='Kursi Pelaminan', 
                                required=True)
    kursitamu = fields.Many2one(comodel_name='wedding.kursitamu', 
                                string='Kursi Tamu',
                                required=True)
    
    bunga = fields.Selection(string='Tipe Bunga', selection=[('bunga mati', 'Bunga Mati'),('bunga hidup', 'Bunga Hidup')], required=True)
    accesories = fields.Char(string='Accesories') 
    # harga = fields.Integer(string='Harga')
    orderdetail_ids = fields.One2many(comodel_name='wedding.order_detail', inverse_name='panggung_id', string='Order Detail')
    harga = fields.Integer(compute='_compute_harga', string='Harga Sewa') #oofcompute digunakan untuk membuat menghitung beberapa nilai pada inputan lain

    @api.depends('pelaminan','kursipengantin','kursitamu')
    def _compute_harga(self):
        for record in self:
            record.harga = record.pelaminan.harga + record.kursipengantin.harga + record.kursitamu.harga

    des_pelaminan = fields.Char(compute='_compute_des_pelaminan', string='Deskripsi Pelaminan')
    
    @api.depends('pelaminan')
    def _compute_des_pelaminan(self):
        for record in self: 
            record.des_pelaminan = record.pelaminan.deskripsi

    des_kursipengantin = fields.Char(compute='_compute_des_kursipengantin', string='Deskripsi Kursi Pengantin')
    
    @api.depends('kursipengantin')
    def _compute_des_kursipengantin(self):
        for record in self:
            record.des_kursipengantin = record.kursipengantin.deskripsi

    des_kursitamu = fields.Char(compute='_compute_des_kursitamu', string='Deskripsi Kursi Tamu')
    
    @api.depends('kursitamu')
    def _compute_des_kursitamu(self):
        for record in self:
            record.des_kursitamu = record.kursitamu.deskripsi

    stock = fields.Integer(string='Stock Paket')
       
    
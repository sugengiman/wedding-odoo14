from odoo import api, fields, models


class Pengembalian(models.Model):
    _name = 'wedding.pengembalian'
    _description = 'Pengembalian Alat Pengantin'

    name = fields.Char(string='Name')
    order_id = fields.Many2one(comodel_name='wedding.order', string='Kode Barang', domain=[('pengembalian_barang','=', False)])
    tgl_pengembalian = fields.Date(string='Pengembalian', default=fields.Date.today())  
    nama_peminjam = fields.Char(compute='_compute_nama_peminjam', string='Nama Peminjam')
    
    @api.depends('order_id')
    def _compute_nama_peminjam(self):
        for record in self:
            record.nama_peminjam = self.env['wedding.order'].search([('id', '=', record.order_id.id)]).pelanggan.name

    # order_panggung_id = fields.Many2one(comodel_name='wedding.order_detail', string='Kode Barang')
    # tipe_kursitamu = fields.Char(compute='_compute_tipe_kursitamu', string='Tipe Kursi')
    
    # @api.depends('tipe_kursitamu')
    # def _compute_tipe_kursitamu(self):
    #     for record in self:
    #         # record.tipe_panggung = self.env['wedding.order'].search([('id', '=', record.order_panggung_id.id)]).panggung_id.name
    #         record.tipe_kursitamu = self.env['wedding.order'].search([('id', '=', record.order_id.id)]).order_id.orderdetailtamu_ids


    tagihan = fields.Integer(compute='_compute_tagihan', string='Tagihan')
    
    @api.depends('tagihan')
    def _compute_tagihan(self):
        for record in self:
            record.tagihan = record.order_id.total

    @api.model
    def create(self, vals):
        record = super(Pengembalian, self).create(vals)
        if record.tgl_pengembalian:
            self.env['wedding.order'].search([('id', '=', record.order_id.id)]).write({'pengembalian_barang': True})
            return record
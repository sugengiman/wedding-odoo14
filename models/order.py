from odoo import api, fields, models
from odoo.exceptions import ValidationError




class Order(models.Model):
    _name = 'wedding.order'
    _description = 'New Description'
  
    tanggal_pesan = fields.Datetime(string='Tanggal Pemesanan', default=fields.Datetime.now(), required=True)
    tanggal_kirim = fields.Date(string='Tanggal Pengiriman', default=fields.Date.today(), required=True)
    orderdetail_ids = fields.One2many(comodel_name='wedding.order_detail', inverse_name='order_id', string='Order Panggung')
    orderdetailtamu_ids = fields.One2many(comodel_name='wedding.order_detail_tamu', inverse_name='order_a_id', string='Order Kursi Tamu')
    
    name = fields.Char(string='Kode Order', required=True)
    pelanggan = fields.Many2one(comodel_name='res.partner', string='Pelanggan',
    domain=[('is_customer','=',True)], required=True)
    pengembalian_barang = fields.Boolean(string='Dikembalikan', default=False)
    total = fields.Integer(compute='_compute_total', string='Total Harga', store=True) #store agar harga tidak berubah meskipun harga barangnya sudah diperbarui
    
    @api.depends('orderdetail_ids')
    def _compute_total(self):
        for record in self :
            total_a = sum(self.env['wedding.order_detail'].search([('order_id', '=', record.id)]).mapped('harga'))
            total_b = sum(self.env['wedding.order_detail_tamu'].search([('order_a_id', '=', record.id)]).mapped('harga_kursi'))
            record.total = total_a + total_b

    def kembali_barang(self):
        for record in self:
            if record.pengembalian_barang == True:
                raise ValidationError('Barang sudah dikembalikan')
            else:
                record.pengembalian_barang = True
    
    def batalkan_kembali(self):
        for record in self:
            if record.pengembalian_barang == False:
                raise ValidationError('Barang belum dikembalikan')
            else:
                record.pengembalian_barang = False

class Order_Detail(models.Model):
    _name = 'wedding.order_detail'
    _description = 'New Description'

    order_id = fields.Many2one(comodel_name='wedding.order', string='Order Panggung')
    panggung_id = fields.Many2one(comodel_name='wedding.panggung', string='Panggung')
    qty = fields.Integer(string='Quantity')
    
    harga = fields.Integer(compute='_compute_harga', string='Harga')
    
    @api.depends('qty','panggung_id')
    def _compute_harga(self):
        for record in self :
            record.harga = record.qty * record.panggung_id.harga

    harga_satuan = fields.Integer(compute='_compute_harga_satuan', string='Harga Satuan')
    
    @api.depends('panggung_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan = record.panggung_id.harga
    
    @api.model
    def create(self, vals):
        record = super(Order_Detail, self).create(vals)
        if record.qty:
            self.env['wedding.panggung'].search([('id', '=', record.panggung_id.id)]).write({'stock': record.panggung_id.stock-record.qty})
            return record

class Order_Detail_Tamu(models.Model):
    _name = 'wedding.order_detail_tamu'
    _description = 'New Description'

    order_a_id = fields.Many2one(comodel_name='wedding.order', string='Order Kursi Tamu')
    kursitamu_id = fields.Many2one(
        comodel_name='wedding.kursitamu', 
        string='Kursi Tamu', 
        domain=[('stock','>', '100')], 
        required=True)
    
    qty_kursi = fields.Integer(string='Quantity', required=True)

    @api.constrains('qty_kursi')
    def _check_stock(self):
        for record in self:
            bahan = self.env['wedding.kursitamu'].search([('stock', '<', record.qty_kursi),('id', '=', record.kursitamu_id.id)])
            if bahan:
                raise ValidationError("Stock Yang Dipilih Tidak Cukup")
            
    
    harga_kursi = fields.Integer(compute='_compute_harga_kursi', string='')

    @api.depends('qty_kursi','kursitamu_id')
    def _compute_harga_kursi(self):
        for record in self :
            record.harga_kursi = record.qty_kursi * record.kursitamu_id.harga

    harga_satuan_kursi = fields.Char(compute='_compute_harga_satuan_kursi', string='Harga Satuan')

    @api.depends('kursitamu_id')
    def _compute_harga_satuan_kursi(self):
        for record in self:
            record.harga_satuan_kursi = record.kursitamu_id.harga

    @api.model
    def create(self, vals):
        record = super(Order_Detail_Tamu, self).create(vals)
        if record.qty_kursi:
            self.env['wedding.kursitamu'].search([('id', '=', record.kursitamu_id.id)]).write({'stock': record.kursitamu_id.stock-record.qty_kursi})
            return record


    

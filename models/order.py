from odoo import api, fields, models


class Order(models.Model):
    _name = 'wedding.order'
    _description = 'New Description'
  
    orderdetail_ids = fields.One2many(comodel_name='wedding.order_detail', inverse_name='order_id', string='Order Detail')
    name = fields.Char(string='Kode Order', required=True)
    total = fields.Integer(compute='_compute_total', string='Total Harga', store=True) #store agar harga tidak berubah meskipun harga barangnya sudah diperbarui
    
    @api.depends('orderdetail_ids')
    def _compute_total(self):
        for record in self :
            total_a = sum(self.env['wedding.order_detail'].search([('order_id', '=', record.id)]).mapped('harga'))
            record.total = total_a

class Order_Detail(models.Model):
    _name = 'wedding.order_detail'
    _description = 'New Description'

    order_id = fields.Many2one(comodel_name='wedding.order', string='Order')
    panggung_id = fields.Many2one(comodel_name='wedding.panggung', string='Panggung')
    name = fields.Selection(string='Nama', selection=[('panggung', 'Panggung'), ('kursi tamu', 'Kursi Tamu'),])
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
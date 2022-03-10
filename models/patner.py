from odoo import api, fields, models


class patnet(models.Model):
    _name = 'wedding.patner' 
    #_name = 'wedding.patner' || module = nama project, name = nama classnya
    _description = 'Standar class patners'

    name = fields.Char(string='Nama')
    alamat = fields.Char(string='Alamat')
    no_telp = fields.Char(string='No Telpon')
    
    
    

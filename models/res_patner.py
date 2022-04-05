from odoo import api, fields, models


class Res_Patner(models.Model):
    _inherit = 'res.partner'

    is_pegawai = fields.Boolean(string='Pegawai', default=False)
    is_customer = fields.Boolean(string='Customer', default=False)
        



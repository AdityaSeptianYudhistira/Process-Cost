# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class MrpBom(models.Model):
    _inherit = 'mrp.bom'

    process_cost = fields.Float(string='Process Cost')
    

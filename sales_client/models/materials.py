# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Materials(models.Model):
    _name = "materials.data"
    _description = "Materials Inputs"

    name = fields.Char(string='Name Of Materials', required=True)
    code = fields.Char(string="Materials Code", required=True)
    type = fields.Selection([
        ('fabrics', 'Fabrics'),
        ('jeans', 'Jeans'),
        ('cotton', 'Cotton'),
    ], required=True, default='fabrics')
    buy_price = fields.Integer(string="Materials Buy Price", required=True)
    suppliers = fields.Selection([
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
    ], required=True, default='a')
    #note = fields.Text(string='Note')

    @api.constrains('buy_price')
    def _check_something(self):
        for record in self:
            if record.buy_price < 100:
                raise ValidationError("Buy Price Cannot Lower Than 100")

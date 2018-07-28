import uuid

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class ProductStyle(models.Model):
    _name = 'product.style'

    name = fields.Char(string="Name")
    code = fields.Char(string="Code",required=True)
    product_template_id = fields.Many2one('product.template',string="Product Template")
    stock_no = fields.Integer(string="Number",required=True)
    is_active = fields.Boolean(string="IS Active")
    product_category = fields.Many2one('product.category',string="Product Category")
    quantity = fields.Integer(string="Product Quanitity")
    weight = fields.Float(string="Weight")
    height = fields.Float(string="Height")
    depth = fields.Float(string="Depth")
    volume = fields.Float(string="Volume")
    brand_id = fields.Many2one('product.brand',string="Brand Name")
    barcode = fields.Char(string="Barcode")
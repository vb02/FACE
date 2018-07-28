import uuid

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class ProductTemplate(models.Model):
    _inherit = "product.template"

    product_style_ids = fields.One2many('product.style','product_template_id',string="Style")

from odoo import models,fields,api


class Brand(models.Model):
	_name = "product.brand"

	name = fields.Char(string="Name",required=True)
{
    'name': 'Product Template Enhancement',
    'version': '1.0',
    #'category': 'Hidden',
    'summary': 'New Functionality will be Added',
    'description': """
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Name and Code !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
""",
#    'website': 'https://www.odoo.com/page/warehouse',
    'depends': ['base','product'],
    'data': [
    			'views/product_template_view.xml',
                'views/product_style_view.xml',
                'views/brand_view.xml',
    ],

}

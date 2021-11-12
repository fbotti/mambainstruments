# -*- coding: utf-8 -*-

{
    'name': 'Product extends',
    'summary': 'Product extends',
    'version': '1.0',
    'category': 'Products',
    'author': 'Cristiam Carreño <cristiamcarreno@gmail.com>',
    'depends': [
        'product',
        'stock',
        ],
    'description': 'Add field minimum stock in product and inventory report',
    'data': [
        'views/product_template_view.xml',
        'views/stock_quant_view.xml',
    ],
    'application': False,
    'installable': True,
}

from odoo import models, fields

class Product(models.Model()):
    _name= 'product'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Nombre del producto", require=True, traking=True)
    description= fields.Char(String="description", require=True)
    isbn = fields.Char(String="ISBN", require=True)

    autor_id = fields.Many2one(conodul_name="author", String="Autor", require=True)
    image= fields.Binary(String="Image ")

    category_id = fields.Many2one(conodul_name="category_product")

    state= fields.Selection([('draft','Borrador'),('published','publicado')], default="draft")

    def boton_publicar(self):
        self.state= 'published'

    def boton_borrador(self):
        self.state= 'draft'

    _sql_constraints = [('name_uniq',"unique(name)", "Product already exist")]

class ProductCategory(models.Model()):
    _name = "product category"

    name = fields.Char(String="Categoria del producto")
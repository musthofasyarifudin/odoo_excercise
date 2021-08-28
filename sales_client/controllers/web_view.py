from odoo import http

from odoo.http import request

class Material(http.Controller):

  @http.route('/home', type='http', auth='public', website=True)

  def sale_details(self , **kwargs):
      materials_details = request.env['materials.data'].sudo().search([])
      return request.render("sales_client.material_client_show", {
          'materials': materials_details
      })

        #return request.render('my_sale_addons.sale_details_page', {'my_details': sale_details})


#@http.route('/my_sale_details', type='http', auth='public', website=True)
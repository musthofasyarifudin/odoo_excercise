from odoo.tests import HttpCase, tagged

@tagged('-at_install', 'post_install')
class WebsiteVisitorTests(HttpCase):
  def test_create_visitor_on_tracked_page(self):
      Page = self.env['website.page']
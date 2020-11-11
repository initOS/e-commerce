# Copyright (C) 2020 Alexandre Díaz - Tecnativa S.L.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
import odoo.tests


@odoo.tests.tagged("-at_install", "post_install")
class TestUi(odoo.tests.HttpCase):
    def test_01_shop_buy(self):
        # Ensure that 'vat' is not empty for compatibility with
        # website_sale_vat_required module
        testuser = self.env["res.users"].create(
            {
                "email": "testuser@testuser.com",
                "name": "Test User",
                "login": "testuser",
                "password": "testuser",
            }
        )
        if not testuser.partner_id.vat:
            testuser.partner_id.vat = "BE1234567"
        current_website = self.env["website"].get_current_website()
        current_website.auth_signup_uninvited = "b2b"
        self.start_tour(
            "/shop", "shop_buy_checkout_suggest_account_website", login="testuser"
        )

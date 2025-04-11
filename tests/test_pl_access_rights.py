import datetime

from common import TestCommon
from odoo.tests import tagged
from odoo.exceptions import AccessError


@tagged('post_install', '-at_install', 'library', 'access')
class TestAccessRights(TestCommon):

    def test_01_pl_access_rights(self):
        test_client = self.env['pl.client'].with_user(self.pl_admin).create(
            {'name': 'Test client',
             })
        test_client_order = self.env['pl.client.order'].with_user(self.pl_admin).create(
            {'order_number': '100',
             'client_id': test_client.id,
             })
        test_product = self.env['pl.product'].with_user(self.pl_admin).create(
            {'name': 'Test product',
             })
        test_order_product = self.env['pl.order.product'].with_user(self.pl_admin).create(
            {'client_order_id': test_client_order.id,
             'quantity': 1,
             'product_id': test_product.id,
             })
        test_stage = self.env['pl.stage'].with_user(self.pl_admin).create(
            {'process': 'slicing',
             'name': 'Test stage',
             })
        test_stage_2 = self.env['pl.stage'].with_user(self.pl_admin).create(
            {'process': 'slicing',
             'name': 'Test stage 2',
             })
        self.env['pl.work.assignment'].with_user(self.pl_admin).create(
            {'foreman_id': self.foreman.id,
             'order_product_id': test_order_product.id,
             'test_stage': test_stage.id,
             'work_start_datetime': datetime.datetime.now(),
             'work_finish_datetime': datetime.datetime.now() + datetime.timedelta(days=1),
             })

        with self.assertRaises(AccessError):
            self.env['pl.work.assignment'].with_user(self.pl_user_2).create(
                {'foreman_id': self.foreman.id,
                 'order_product_id': test_order_product.id,
                 'test_stage': test_stage_2.id,
                 'work_start_datetime': datetime.datetime.now(),
                 'work_finish_datetime': datetime.datetime.now() + datetime.timedelta(days=1),
                 })


from odoo.tests.common import TransactionCase


class TestCommon(TransactionCase):

    def setUp(self):
        super(TestCommon, self).setUp()
        self.group_pl_user = self.env.ref(
            'pp_process_load.group_pl_user')
        self.group_pl_admin = self.env.ref(
            'pp_process_load.group_pl_admin')
        self.foreman = self.env['pl.foreman'].create({
            'name': 'Demo foreman',
            # 'user_id': self.pl_user.id,
        })
        self.another_foreman = self.env['pl.foreman'].create({
            'name': 'Demo foreman 2',
            # 'user_id': self.pl_user_2.id,
        })
        self.pl_user = self.env['res.users'].create({
            'name': 'PL User',
            'login': 'pl_user',
            'pl_foreman_id': self.foreman,
            'groups_id': [(4, self.env.ref('base.group_user').id),
                          (4, self.group_pl_user.id)],
        })
        self.pl_user_2 = self.env['res.users'].create({
            'name': 'PL User 2',
            'login': 'pl_user_2',
            'pl_foreman_id': self.another_foreman,
            'groups_id': [(4, self.env.ref('base.group_user').id),
                          (4, self.group_pl_user.id)],
        })
        self.pl_admin = self.env['res.users'].create({
            'name': 'PL Admin',
            'login': 'pl_admin',
            'groups_id': [(4, self.env.ref('base.group_user').id),
                          (4, self.group_pl_admin.id)],
        })

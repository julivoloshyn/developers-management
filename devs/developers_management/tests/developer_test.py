from datetime import date

from odoo.tests import TransactionCase


class TestDeveloper(TransactionCase):

    def setUp(self):
        super(TestDeveloper, self).setUp()
        self.Company = self.env['company']
        self.Developer = self.env['developer']
        self.company = self.Company.create({
            'name': 'Google',
            'address': 'Address',
        })
        self.developer = self.Developer.create({
            'name': 'John',
            'position_type': 'Front-End',
            'phone': '1234567890',
            'email': 'test@test.com',
            'address': 'London',
            'birthdate': date(2000, 9, 9),
            'company_id': self.Company.id,
        })

    def test_developer_create(self):
        developer = self.Developer.search([('name', '=', 'John')])
        self.assertEqual(len(developer), 1)
        self.assertEqual(developer.position_type, 'Front-End')
        self.assertEqual(developer.global_identification, 'John - Front-End')
        self.assertEqual(developer.phone, '1234567890')
        self.assertEqual(developer.email, 'developer@test.com')
        self.assertEqual(developer.address, 'London')
        self.assertEqual(developer.birthdate, date(2000, 9, 9))
        self.assertEqual(developer.company_id.id, self.Company.id)

    def test_developer_update(self):
        self.developer.write({
            'position_type': 'Out-Stack',
        })

        self.assertEqual(self.developer.position_type, 'Out-Stack')
        self.assertFalse(self.developer.phone)

    def test_developer_delete(self):
        self.developer.unlink()

        developer = self.Developer.search([('id', '=', self.developer.id)])
        self.assertFalse(developer)

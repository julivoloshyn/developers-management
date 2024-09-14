from odoo.tests import TransactionCase


class TestDeveloper(TransactionCase):

    def setUp(self):
        super(TestDeveloper, self).setUp()
        self.Company = self.env['company']
        self.company = self.Company.create({
            'name': 'Google',
            'address': 'Address',
        })

    def test_company_create(self):
        company = self.Company.search([('name', '=', 'Google')])
        self.assertEqual(len(company), 1)
        self.assertEqual(company.name, 'Google')
        self.assertEqual(company.address, 'Address')

    def test_company_update(self):
        self.company.write({
            'position_type': 'Out-Stack',
        })

        self.assertEqual(self.company.position_type, 'Out-Stack')
        self.assertFalse(self.company.phone)

    def test_company_delete(self):
        self.company.unlink()

        company = self.company.search([('id', '=', self.company.id)])
        self.assertFalse(company)
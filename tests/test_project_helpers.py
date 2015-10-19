import unittest
from freelancersdk.resources.projects.helpers import (create_budget_object,
                                                      create_currency_object,
                                                      create_job_object)

class TestProjectHelpers(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create_currency_object(self):
        c = create_currency_object(1, name='USD')
        self.assertEquals(c['id'], 1)
        self.assertEquals(c['name'], 'USD')

    def test_create_budget_object(self):
        b = create_budget_object(minimum=10, maximum=100)
        self.assertEquals(b['minimum'], 10)
        self.assertEquals(b['maximum'], 100)   

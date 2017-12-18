import unittest

from freelancersdk.resources.users.helpers import (
    create_get_users_object,
    create_get_users_details_object,
)


class TestUsersHelpers(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create_get_users_object(self):
        query = create_get_users_object(
            user_ids=[
                201,
                202,
                203,
            ],
        )
        self.assertIn(('users[]', [201, 202, 203]), query.items())

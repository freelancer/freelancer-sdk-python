from freelancersdk.exceptions import AuthTokenNotSuppliedException
from freelancersdk.session import Session
from freelancersdk.resources.projects import (create_project,
                                              place_project_bid,
                                              create_milestone_payment,
                                              projects_endpoint)
from freelancersdk.resources.projects.helpers import (create_budget_object,
                                                      create_currency_object,
                                                      create_job_object)
from freelancersdk.resources.projects.types import MilestoneReason
try:
    from unittest.mock import Mock
except ImportError:
    from mock import Mock

import unittest

class FakeProjectPostResponse:

    status_code = 200

    def json(self):
        return {'result':{'title': 'My New Project',
                          'seo_url': 'java/foo',
                          }
        }

class FakePlaceBidPostResponse:

    status_code = 200

    def json(self):
        return {'result':
                {
                    'milestone_percentage': 100,
                    'period': 2,
                    'id': 39343812,
                    'retracted': False,
                    'project_owner_id': 12,
                    'submitdate': 1424142980,
                    'project_id': 1,
                    'bidder_id': 2,
                    'description': 'A bid',
                    'time_submitted': 1424142980,
                    'amount': 10
                }
        }

class FakeMilestonePaymentCreatePostResponse:

    status_code = 200

    def json(self):
        return {'result':
                {
                    'bidder_id': 2,
                    'description': 'A milestone',
                    'time_submitted': 1424142980,
                    'amount': 10,
                    'reason': MilestoneReason.PARTIAL_PAYMENT,
                }
        }

class TestProjects(unittest.TestCase):
    def setUp(self):
        self.session = Session(1, '$sometoken', url='https://fake-fln.com')

    def tearDown(self):
        pass

    def test_create_project(self):
        project_data = {
            'title': 'My new project',
            'description': 'description',
            'currency': create_currency_object(id=1),
            'budget': create_budget_object(minimum=10),
            'jobs': create_job_object(id=7),
        }

        self.session.session.post = Mock()
        self.session.session.post.return_value = FakeProjectPostResponse()
        p = create_project(self.session, **project_data)
        self.session.session.post.assert_called_once_with(
            'https://fake-fln.com/api/projects/0.1/projects/',
            json=project_data,
            verify=True)
        self.assertEquals(p.url, 'https://fake-fln.com/projects/java/foo')

    def test_place_project_bid(self):
        bid_data = {
            'project_id': 1,
            'bidder_id': 2,
            'amount': 10,
            'period': 2,
            'milestone_percentage': 100,
            'description': 'A bid',
        }

        self.session.session.post = Mock()
        self.session.session.post.return_value = FakePlaceBidPostResponse()
        b = place_project_bid(self.session, **bid_data)
        self.session.session.post.assert_called_once_with(
            'https://fake-fln.com/api/projects/0.1/bids/',
            json=bid_data,
            verify=True)
        self.assertTrue(getattr(b, 'bidder_id'))
        self.assertTrue(getattr(b, 'description'))

    def test_create_milestone_payment(self):
        milestone_data = {
            'project_id': 1,
            'bidder_id': 2,
            'amount': 10,
            'reason': MilestoneReason.PARTIAL_PAYMENT,
            'description': 'This is a milestone',
        }

        self.session.session.post = Mock()
        self.session.session.post.return_value = FakeMilestonePaymentCreatePostResponse()
        m = create_milestone_payment(self.session, **milestone_data)
        self.session.session.post.assert_called_once_with(
            'https://fake-fln.com/api/projects/0.1/milestones/',
            json=milestone_data,
            verify=True)
        self.assertTrue(getattr(m, 'bidder_id'))
        self.assertTrue(getattr(m, 'description'))
        self.assertEquals(m.reason, MilestoneReason.PARTIAL_PAYMENT)

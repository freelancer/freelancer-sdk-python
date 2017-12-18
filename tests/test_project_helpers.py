import unittest
from freelancersdk.resources.projects.helpers import (
    create_budget_object, create_currency_object, create_job_object,
    create_hourly_project_info_object, create_country_object,
    create_location_object, create_bid_object, create_review_freelancer_object,
    create_review_employer_object, create_get_projects_object,
    create_get_projects_project_details_object,
    create_get_projects_user_details_object,
)


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

    def test_create_job_object(self):
        j = create_job_object(id=1, name='HTML', seo_url='html')
        self.assertEquals(j['id'], 1)
        self.assertEquals(j['name'], 'HTML')
        self.assertEquals(j['seo_url'], 'html')

    def test_create_hourly_project_info_object(self):
        h = create_hourly_project_info_object(commitment_hours=40,
                                              commitment_interval='WEEK',)
        self.assertEquals(h['commitment']['hours'], 40)
        self.assertEquals(h['commitment']['interval'], 'WEEK')

    def test_create_country_object(self):
        c = create_country_object(name='Australia', code='AU')
        self.assertEquals(c['name'], 'Australia')
        self.assertEquals(c['code'], 'AU')

    def test_create_location_object(self):
        c = create_country_object(name='Australia')
        l = create_location_object(country=c, city='Sydney', latitude=-33,
                                   longitude=151)
        self.assertEquals(l['country'], c)
        self.assertEquals(l['city'], 'Sydney')
        self.assertEquals(l['latitude'], -33)
        self.assertEquals(l['longitude'], 151)

    def test_create_bid_object(self):
        c = create_bid_object(id=1, bidder_id=2, project_id=3, retracted=False,
                              amount=100, period=7, description='Hello',
                              project_owner_id=4)
        self.assertEquals(c['id'], 1)
        self.assertEquals(c['bidder_id'], 2)
        self.assertEquals(c['project_id'], 3)
        self.assertEquals(c['retracted'], False)
        self.assertEquals(c['amount'], 100)
        self.assertEquals(c['period'], 7)
        self.assertEquals(c['description'], 'Hello')
        self.assertEquals(c['project_owner_id'], 4)

    def test_create_review_freelancer_object(self):
        r = create_review_freelancer_object(project_id=201, employer_id=101,
                                            freelancer_id=102, on_budget=True,
                                            on_time=True, quality=5,
                                            communication=5, expertise=5,
                                            professionalism=5, hire_again=5,
                                            comment='Great work')
        self.assertEquals(r['project_id'], 201)
        self.assertEquals(r['to_user_id'], 102)
        self.assertEquals(r['from_user_id'], 101)
        self.assertEquals(r['role'], 'freelancer')
        self.assertEquals(r['reputation_data']['on_budget'], True)
        self.assertEquals(r['reputation_data']['on_time'], True)
        self.assertEquals(
            r['reputation_data']['category_ratings']['quality'], 5)
        self.assertEquals(
            r['reputation_data']['category_ratings']['communication'], 5)
        self.assertEquals(
            r['reputation_data']['category_ratings']['expertise'], 5)
        self.assertEquals(
            r['reputation_data']['category_ratings']['professionalism'], 5)
        self.assertEquals(
            r['reputation_data']['category_ratings']['hire_again'], 5)
        self.assertEquals(r['comment'], 'Great work')

    def create_review_employer_object(self):
        r = create_review_employer_object(project_id=201, employer_id=101,
                                          freelancer_id=102, clarity_spec=5,
                                          communication=5, payment_prom=5,
                                          professionalism=5, work_for_again=5,
                                          comment='Thanks for all the fish')
        self.assertEquals(r['project_id'], 201)
        self.assertEquals(r['to_user_id'], 101)
        self.assertEquals(r['from_user_id'], 102)
        self.assertEquals(r['role'], 'employer')
        self.assertEquals(
            r['reputation_data']['category_ratings']['clarity_spec'], 5)
        self.assertEquals(
            r['reputation_data']['category_ratings']['communication'], 5)
        self.assertEquals(
            r['reputation_data']['category_ratings']['payment_prom'], 5)
        self.assertEquals(
            r['reputation_data']['category_ratings']['professionalism'], 5)
        self.assertEquals(
            r['reputation_data']['category_ratings']['work_for_again'], 5)
        self.assertEquals(r['comment'], 'Thanks for all the fish')

    def test_create_get_projects_object(self):
        query = create_get_projects_object(
            project_ids=[
                201,
                202,
                203,
            ],
            project_details=create_get_projects_project_details_object(
                full_description=True,
            ),
            user_details=create_get_projects_user_details_object(
                basic=True,
            ),
        )

        self.assertIn(('projects[]', [201, 202, 203]), query.items())

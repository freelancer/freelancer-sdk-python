# This module will contain helper functions/classes for projects
# Reference: https://www.freelancer.com/api/docs/structs/index

from freelancersdk.resources.projects import projects_endpoint
try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin

# Make API calls
# /api/projects/0.1/<specific_endpoint>
def make_post_request(session, endpoint, json_data):
    return session.session.post(urljoin(session.url,
                                        '%s/%s/' % (projects_endpoint, endpoint)),
                                json=json_data,
                                verify=True)

# Helper functions for creating various objects
def create_currency_object(id, code=None, sign=None,
                           name=None, exchange_rate=None,
                           country=None):
    c = dict(id=id)
    if code:
        c.update(code=code)
    if sign:
        c.update(sign=sign)
    if name:
        c.update(name=name)
    if exchange_rate:
        c.update(exchange_rate=exchange_rate)
    if country:
        c.update(country=country)
    return c

def create_category(id, name=None):
    c = dict(id=id)
    if name:
        c.update(name=name)

    return c

def create_job_object(id, name=None, category=None,
                      active_project_count=None,
                      seo_url=None, seo_info=None):
    j = dict(id=id)
    if name:
        j.update(name=name)
    if category:
        j.update(category=category)
    if active_project_count:
        j.update(active_project_count=active_project_count)
    if seo_url:
        j.update(seo_url=seo_url)
    if seo_info:
        j.update(seo_info=seo_info)

    return j

def create_budget_object(minimum, maximum=None, name=None,
                         project_type=None, currency_id=None):
    b = dict(minimum=minimum)
    if maximum:
        b.update(maximum=maximum)
    if name:
        b.update(name=name)
    if project_type:
        b.update(project_type=project_type)
    if currency_id:
        b.update(currency_id=currency_id)

    return b

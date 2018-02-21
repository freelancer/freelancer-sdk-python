# This module will contain helper functions/classes for users
# Reference: https://www.freelancer.com/api/docs/structs/index

from freelancersdk.resources.users import users_endpoint

try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin


# Make API calls
# /api/users/0.1/<specific_endpoint>
def make_post_request(session, endpoint, json_data):
    return session.session.post(urljoin(session.url,
                                        '%s/%s/' % (users_endpoint, endpoint)),
                                json=json_data,
                                verify=True)


def make_get_request(session, endpoint, params_data=None):
    url = urljoin(session.url, '{}/{}/'.format(users_endpoint, endpoint))
    return session.session.get(url, params=params_data, verify=True)


def make_put_request(session, endpoint, headers=None, params_data=None,
                     form_data=None, json_data=None):
    return session.session.put(urljoin(session.url,
                                       '%s/%s/' % (users_endpoint, endpoint)),
                               headers=headers,
                               params=params_data,
                               data=form_data,
                               json=json_data,
                               verify=True)


def make_delete_request(session, endpoint, headers=None, params_data=None,
                        form_data=None, json_data=None):
    return session.session.delete(urljoin(session.url,
                                          '%s/%s/' % (users_endpoint,
                                                      endpoint)),
                                  headers=headers,
                                  params=params_data,
                                  data=form_data,
                                  json=json_data,
                                  verify=True)


def create_get_users_object(user_ids=None, usernames=None, user_details=None):
    u = {}
    if user_ids:
        u['users[]'] = user_ids
    if usernames:
        u['usernames[]'] = usernames
    if user_details:
        u.update(user_details)
    return u


def create_get_users_details_object(basic=None, avatar=None,
                                            country=None,
                                            profile_description=None,
                                            display_info=None, jobs=None,
                                            balance=None, qualifications=None,
                                            membership=None, financial=None,
                                            location=None, portfolio=None,
                                            preferred=None, badge=None,
                                            status=None, reputation=None,
                                            employer_reputation=None,
                                            reputation_extra=None,
                                            employer_reputation_extra=None,
                                            cover_image=None, past_covers=None,
                                            responsiveness=None,
                                            corporate_accounts=None):
    d = {}
    if basic:
        d.update(details=basic)
    if avatar:
        d.update(avatar=avatar)
    if country:
        d.update(country_details=country)
    if profile_description:
        d.update(profile_description=profile_description)
    if display_info:
        d.update(display_info=display_info)
    if jobs:
        d.update(jobs=jobs)
    if balance:
        d.update(balance_details=balance)
    if qualifications:
        d.update(qualification_details=qualifications)
    if membership:
        d.update(membership_details=membership)
    if financial:
        d.update(financial_details=financial)
    if location:
        d.update(location_details=location)
    if portfolio:
        d.update(portfolio_details=portfolio)
    if preferred:
        d.update(preferred_details=preferred)
    if badge:
        d.update(badge_details=badge)
    if status:
        d.update(status=status)
    if reputation:
        d.update(reputation=reputation)
    if employer_reputation:
        d.update(employer_reputation=employer_reputation)
    if reputation_extra:
        d.update(reputation_extra=reputation_extra)
    if employer_reputation_extra:
        d.update(employer_reputation_extra=employer_reputation_extra)
    if cover_image:
        d.update(cover_image=cover_image)
    if past_covers:
        d.update(past_covers=past_covers)
    if responsiveness:
        d.update(responsiveness=responsiveness)
    if corporate_accounts:
        d.update(corporate_accounts=corporate_accounts)

    return d

# This module will contain helper functions/classes for projects
# Reference: https://www.freelancer.com/api/docs/structs/index

from freelancersdk.resources.projects import projects_endpoint
try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin


# Make API calls
# /api/projects/0.1/<specific_endpoint>
def make_get_request(session, endpoint, params_data=None):
    url = urljoin(session.url, '{}/{}/'.format(projects_endpoint, endpoint))
    return session.session.get(url, params=params_data, verify=True)


def make_post_request(session, endpoint, json_data):
    url = urljoin(session.url, '{}/{}/'.format(projects_endpoint, endpoint))
    return session.session.post(url, json=json_data, verify=True)


def make_put_request(session, endpoint, headers=None, params_data=None,
                     form_data=None, json_data=None):
    url = urljoin(session.url, '{}/{}/'.format(projects_endpoint, endpoint))
    return session.session.put(url, headers=headers, params=params_data,
                               data=form_data, json=json_data, verify=True)


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


def create_hourly_project_info_object(commitment_hours, commitment_interval):
    h = {
        'commitment': {
            'hours': commitment_hours,
            'interval': commitment_interval,
        },
    }
    return h


def create_country_object(name, flag_url=None, code=None, highres_flag_url=None,
                          flag_url_cdn=None, highres_flag_url_cdn=None,
                          iso3=None, region_id=None, phone_code=None,
                          demonym=None, person=None, seo_url=None,
                          sanction=None, language_code=None, language_id=None):
    c = {
       'name': name
    }
    if flag_url:
        c.update(flag_url=flag_url)
    if code:
        c.update(code=code)
    if highres_flag_url:
        c.update(highres_flag_url=highres_flag_url)
    if flag_url_cdn:
        c.update(flag_url_cdn=flag_url_cdn)
    if highres_flag_url_cdn:
        c.update(highres_flag_url_cdn=highres_flag_url_cdn)
    if iso3:
        c.update(iso3=iso3)
    if region_id:
        c.update(region_id=region_id)
    if phone_code:
        c.update(phone_code=phone_code)
    if demonym:
        c.update(demonym=demonym)
    if person:
        c.update(person=person)
    if seo_url:
        c.update(seo_url=seo_url)
    if sanction:
        c.update(sanction=sanction)
    if language_code:
        c.update(language_code=language_code)
    if language_id:
        c.update(language_id=language_id)

    return c


def create_location_object(country=None, city=None, latitude=None,
                           longitude=None, vicinity=None,
                           administrative_area=None, full_address=None):
    l = {}
    if country:
        l.update(country=country)
    if city:
        l.update(city=city)
    if latitude:
        l.update(latitude=latitude)
    if longitude:
        l.update(longitude=longitude)
    if vicinity:
        l.update(vicinity=vicinity)
    if administrative_area:
        l.update(administrative_area=administrative_area)
    if full_address:
        l.update(full_address=full_address)

    return l


def create_bid_object(id, bidder_id, project_id, retracted, amount, period,
                      description, project_owner_id):
    b = {
        'id': id,
        'bidder_id': bidder_id,
        'project_id': project_id,
        'retracted': retracted,
        'amount': amount,
        'period': period,
        'description': description,
        'project_owner_id': project_owner_id
    }

    return b


def create_review_freelancer_object(project_id, employer_id, freelancer_id,
                                    on_budget, on_time, quality, communication,
                                    expertise, professionalism, hire_again,
                                    comment):
    return {
        'project_id': project_id,
        'to_user_id': freelancer_id,
        'from_user_id': employer_id,
        'role': 'freelancer',
        'reputation_data': {
            'on_budget': on_budget,
            'on_time': on_time,
            'category_ratings': {
                'quality': quality,
                'communication': communication,
                'expertise': expertise,
                'professionalism': professionalism,
                'hire_again': hire_again,
            },
        },
        'comment': comment,
    }


def create_review_employer_object(project_id, employer_id, freelancer_id,
                                  clarity_spec, communication, payment_prom,
                                  professionalism, work_for_again, comment):
    return {
        'project_id': project_id,
        'to_user_id': employer_id,
        'from_user_id': freelancer_id,
        'role': 'employer',
        'reputation_data': {
            'category_ratings': {
                'clarity_spec': clarity_spec,
                'communication': communication,
                'payment_prom': payment_prom,
                'professionalism': professionalism,
                'work_for_again': work_for_again,
            },
        },
        'comment': comment,
    }


def create_get_projects_project_details_object(full_description=None, jobs=None,
                                               upgrades=None, attachments=None,
                                               files=None, qualifications=None,
                                               selected_bids=None, hiremes=None,
                                               invited_freelancers=None,
                                               recommended_freelancers=None,
                                               support_sessions=None,
                                               location=None):
    d = {}
    if full_description:
        d.update(full_description=full_description)
    if jobs:
        d.update(job_details=jobs)
    if upgrades:
        d.update(upgrade_details=upgrades)
    if attachments:
        d.update(attachment_details=attachments)
    if files:
        d.update(file_details=files)
    if qualifications:
        d.update(qualification_details=qualifications)
    if selected_bids:
        d.update(selected_bids=selected_bids)
    if hiremes:
        d.update(hireme_details=hiremes)
    if invited_freelancers:
        d.update(invited_freelancer_details=invited_freelancers)
    if recommended_freelancers:
        d.update(recommended_freelancer_details=recommended_freelancers)
    if support_sessions:
        d.update(support_session_details=support_sessions)
    if location:
        d.update(location_details=location)

    return d


def create_get_projects_user_details_object(basic=None, avatar=None,
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
        d.update(user_details=basic)
    if avatar:
        d.update(user_avatar=avatar)
    if country:
        d.update(user_country_details=country)
    if profile_description:
        d.update(user_profile_description=profile_description)
    if display_info:
        d.update(user_display_info=display_info)
    if jobs:
        d.update(user_jobs=jobs)
    if balance:
        d.update(user_balance_details=balance)
    if qualifications:
        d.update(user_qualification_details=qualifications)
    if membership:
        d.update(user_membership_details=membership)
    if financial:
        d.update(user_financial_details=financial)
    if location:
        d.update(user_location_details=location)
    if portfolio:
        d.update(user_portfolio_details=portfolio)
    if preferred:
        d.update(user_preferred_details=preferred)
    if badge:
        d.update(user_badge_details=badge)
    if status:
        d.update(user_status=status)
    if reputation:
        d.update(user_reputation=reputation)
    if employer_reputation:
        d.update(user_employer_reputation=employer_reputation)
    if reputation_extra:
        d.update(user_reputation_extra=reputation_extra)
    if employer_reputation_extra:
        d.update(user_employer_reputation_extra=employer_reputation_extra)
    if cover_image:
        d.update(cover_image=cover_image)
    if past_covers:
        d.update(past_covers=past_covers)
    if responsiveness:
        d.update(responsiveness=responsiveness)
    if corporate_accounts:
        d.update(corporate_accounts=corporate_accounts)

    return d


def create_get_projects_object(project_ids=None, owner_ids=None, seo_urls=None,
                               from_time=None, to_time=None,
                               frontend_statuses=None, count=None,
                               project_details=None, user_details=None,
                               limit=None, offset=None):
    p = {}
    if project_ids:
        p.update({'projects[]': project_ids})
    if owner_ids:
        p.update({'owners[]': owner_ids})
    if seo_urls:
        p.update({'seo_urls[]': seo_urls})
    if from_time:
        p.update(from_time=from_time)
    if to_time:
        p.update(to_time=to_time)
    if frontend_statuses:
        p.update(frontend_project_statuses=frontend_statuses)
    if count:
        p.update(count=count)
    if project_details:
        p.update(project_details)
    if user_details:
        p.update(user_details)
    if limit:
        p.update(limit=limit)
    if offset:
        p.update(offset=offset)

    return p

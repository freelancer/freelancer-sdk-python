Python library for Freelancer.com API
=====================================

.. image:: https://badge.fury.io/py/freelancersdk.svg
    :target: https://badge.fury.io/py/freelancersdk
.. image:: https://travis-ci.org/freelancer/freelancer-sdk-python.svg?branch=master
    :target: https://travis-ci.org/freelancer/freelancer-sdk-python


This is a Python library for the `Freelancer.com
API <https://developers.freelancer.com>`__. Using this, you can interact
with Freelancer.com from your Python applications. It supports Python
2.7 and Python 3 (3.6+). For more about information about the
Freelancer.com API, visit https://developers.freelancer.com.

Install
~~~~~~~

Install it using ``pip install freelancersdk``. It may be a good idea to
use `virtualenv <https://virtualenv.readthedocs.org/en/latest/>`__ as
part of your workflow.

Versioning
----------

The current version `series` of the library is ``0.1.x`` which corresponds to the
``0.1`` version of the API. The revision number ``x`` corresponds to the
revision of the SDK. The ``0.1`` series of the library will continue to
support (in a backward compatible way) the ``0.1`` version of the
Freelancer.com API.

Usage
~~~~~

The first step to using any SDK function is to create a `Session` object:

::

    >>> from freelancersdk.session import Session
    >>> session = Session(oauth_token=token)

You must have a valid OAuth2 token before you can use the SDK or the
API. See the `Freelancer.com Developer
portal <https://developers.freelancer.com>`__ for more information on
how you can do so.

Once we have a session object, we can start using the SDK functions.

Examples
~~~~~~~~

All the examples below recognizes two environment variables:

-  ``FLN_OAUTH_TOKEN``: The OAuth2 token to create the session with and
   must be specified
-  ``FLN_URL``: If you want to use the library to make requests against
   the `Freelancer.com
   Sandbox <https://developers.freelaner.com/docs/api-overview/sandbox-environment>`__,
   you can specifiy ``FLN_URL=https://www.freelancer-sandbox.com``. If
   not specified, it defaults to ``https://www.freelancer.com``.

**Projects**

-  `Create a Fixed Project <examples/create_project.py>`__
-  `Create a Hourly Project <examples/create_hourly_project.py>`__
-  `Create a Local Project <examples/create_local_project.py>`__
-  `Create a Hireme Project <examples/create_hireme_project.py>`__
-  `Create a Freelancer Review <examples/create_freelancer_review.py>`__
-  `Create a Employer Review <examples/create_employer_review.py>`__
-  `Search for Projects <examples/search_projects.py>`__
-  `Retrieve Project details <examples/get_projects.py>`__
-  `Get a list of jobs (skills) <examples/get_jobs.py>`__

**Bids**

-  `Create a Bid <examples/place_project_bid.py>`__
-  `Award a Bid <examples/award_project_bid.py>`__
-  `Accept a bid <examples/accept_project_bid.py>`__
-  `Revoke a Bid <examples/revoke_project_bid.py>`__
-  `Retract a Bid <examples/retract_project_bid.py>`__
-  `Highlight a Bid <examples/highlight_project_bid.py>`__
-  `Retrieve project bids <examples/get_bids.py>`__

**Milestone Payments**

-  `Create a Milestone payment <examples/create_milestone_payment.py>`__
-  `Create a Milestone payment
   request <examples/create_milestone_request.py>`__
-  `Accept a Milestone payment
   request <examples/accept_milestone_request.py>`__
-  `Reject a Milestone payment
   request <examples/reject_milestone_request.py>`__
-  `Delete a Milestone payment
   request <examples/delete_milestone_request.py>`__
-  `Release Milestone payment
   request <examples/release_milestone_payment.py>`__
-  `Cancel Milestone payment
   request <examples/cancel_milestone_payment.py>`__
-  `Request a Milestone payment
   release <examples/request_release_milestone_payment.py>`__
-  `Retrieve project milestones <examples/get_milestones.py>`__
-  `Retrieve a milestone by ID <examples/get_specific_milestone.py>`__

**Messaging**

-  `Create a new thread in the context of a
   project <examples/create_message_project_thread.py>`__
-  `Create a new message in an existing
   thread <examples/create_message.py>`__
-  `Upload an attachment in an exising
   thread <examples/create_message_with_attachment.py>`__
-  `Retrieve messages <examples/get_messages.py>`__
-  `Retrieve threads <examples/get_threads.py>`__
-  `Search for messages <examples/search_messages.py>`__

**Contests**

-  `Create a contest <examples/create_contest.py>`__

**Users**

-  `Add a job to a user's list of jobs <examples/add_user_jobs.py>`__
-  `Delete a job from a user's jobs <examples/delete_user_jobs.py>`__
-  `Set a user's list of jobs <examples/set_user_jobs.py>`__
-  `Retrieve User Details <examples/get_users.py>`__

License
~~~~~~~

GNU LGPLv3. Please see `LICENSE <LICENSE>`__ and
`COPYING.LESSER <COPYING.LESSER>`__.

Please note that 0.1.3 release changed the LICENSE from BSD to GNU
LGPLv3. If you were using the library prior to this release, please file
a issue to let us know if the change affects you in any way.

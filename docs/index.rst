.. freelancersdk documentation master file, created by
   sphinx-quickstart on Wed Oct 28 16:45:55 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Freelancer.com SDK for Python
=============================

A Python library for working with `Freelancer.com <https://ww.freelancer.com>`__.
It exposes the core functionalities - posting a project, bidding on a project,
accepting a bid and others. 

For more about information about the Freelancer.com API, 
visit `https://developers.freelancer.com <https://developers.freelancer.com>`__.


Installing the SDK
------------------

The latest stable release is available from `PyPi <https://pypi.python.org/pypi/freelancersdk>`__. 
Install it using `pip`::

    pip install freelancersdk

Getting Started
---------------

To talk to Freelancer.com, we first create *session*:

.. code-block:: python

   from freelancersdk.session import Session
   s = Session(oauth_token="myoauth$token")



.. toctree::
   :hidden:
   :maxdepth: 2

   projects
   users
   messages
   contests
   help
   contribute

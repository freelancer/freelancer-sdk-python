# Python SDK for Freelancer REST API

This is a SDK for the
[Freelancer.com API](https://www.freelancer.com/api/docs/). It supports
Python 2.7 and Python 3 (3.4+).

### Install

Install it using `pip install freelancersdk` or by running `python
setup.py install` from a clone of the source tree. It may be a good
idea to use
[virtualenv](https://virtualenv.readthedocs.org/en/latest/) as part of
your workflow.

### Usage

The first step to using any SDK function is to create a session
object:

```
>>> from freelancersdk.session import Session
>>> id = <DEVELOPER ID>
>>> token = <DEVELOPER TOKEN>
>>> session = Session(id=id, token=token)
```

You must have a developer ID and token before you can use the SDK or
the API. To get one, visit the
[Developer Signup](https://www.freelancer.com/developers/hackathon/)
page.

Once we have a session object, we can start using the SDK
functions. See the `samples` directory for some ready to use scripts
demonstrating using the SDK functions.

### Examples

Please see `samples`. The API documentation is also
[available](http://freelancercom-python-sdk.readthedocs.org/en/latest/).

### Overview of the source

- ``freelancersdk``: The SDK source code lives here. The ``resources``
  sub-directory has a ``projects`` and ``user`` sub-directories
  corresponding to the REST API projects and users endpoints. In
  future, there will be a sub-directory for each of the endpoints listed
  [here](https://www.freelancer.com/api/docs/).
- ``samples``: Sample usage of the SDK functions
- ``tests``: Unit tests

### Tests

To run the tests, invoke ``tox``.

### License

Please see LICENSE

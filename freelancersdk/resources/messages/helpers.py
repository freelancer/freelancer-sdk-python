# This module will contain helper functions/classes for messages

from freelancersdk.resources.messages import messages_endpoint
try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin


# Make API calls
# /api/messages/0.1/<specific_endpoint>
def make_post_request(session, endpoint, headers=None, params_data=None,
                      form_data=None, json_data=None, files=None):
    url = urljoin(session.url, '{}/{}/'.format(messages_endpoint, endpoint))
    return session.session.post(url=url, headers=headers, params=params_data,
                                data=form_data, json=json_data, files=files,
                                verify=True)


# Helper functions for creating various objects
def create_attachment(file_object, file_name):
    a = {
        'file': ('files[]', (file_name, file_object)),
        'filename': file_name,
    }
    return a

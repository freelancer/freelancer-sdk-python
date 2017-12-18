from freelancersdk.resources.projects.exceptions import *
from freelancersdk.resources.users.exceptions import *

class AuthTokenNotSuppliedException(Exception):
    """
    Authorization token not supplied
    """
    pass

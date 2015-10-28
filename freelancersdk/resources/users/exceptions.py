class UserIdNotRetrievedException(Exception):
    """
    User ID could not retrieved
    """
    def __init__(self, message, error_code):
        super(UserIdNotRetrievedException, self).__init__(message)
        self.error_code = error_code

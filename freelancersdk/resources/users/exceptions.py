class UserIdNotRetrievedException(Exception):
    """
    User ID could not retrieved
    """

    def __init__(self, message, error_code, request_id):
        super(UserIdNotRetrievedException, self).__init__(message)

        self.request_id = request_id


class UserJobsNotAddedException(Exception):
    """
    User jobs could not be added
    """

    def __init__(self, message, error_code, request_id):
        super(UserJobsNotAddedException, self).__init__(message)

        self.request_id = request_id


class UserJobsNotSetException(Exception):
    """
    User jobs could not be set
    """

    def __init__(self, message, error_code, request_id):
        super(UserJobsNotSetException, self).__init__(message)

        self.request_id = request_id


class UserJobsNotDeletedException(Exception):
    """
    User jobs could not be deleted
    """

    def __init__(self, message, error_code, request_id):
        super(UserJobsNotDeletedException, self).__init__(message)

        self.request_id = request_id


class UserNotFoundException(Exception):
    """
    Specific user could not be found
    """

    def __init__(self, message, error_code, request_id):
        super(UserNotFoundException, self).__init__(message)
        self.error_code = error_code
        self.request_id = request_id


class UsersNotFoundException(Exception):
    """
    Users could not be found
    """

    def __init__(self, message, error_code, request_id):
        super(UsersNotFoundException, self).__init__(message)
        self.error_code = error_code
        self.request_id = request_id


class SelfNotRetrievedException(Exception):
    """
    Self User could not be retrieved
    """

    def __init__(self, message, error_code, request_id):
        super(SelfNotRetrievedException, self).__init__(message)
        self.error_code = error_code
        self.request_id = request_id


class ReputationsNotFoundException(Exception):
    """
    User reputations could not be found
    """

    def __init__(self, message, error_code, request_id):
        super(ReputationsNotFoundException, self).__init__(message)
        self.error_code = error_code
        self.request_id = request_id


class PortfoliosNotFoundException(Exception):
    """
    User portfolios could not be found
    """

    def __init__(self, message, error_code, request_id):
        super(PortfoliosNotFoundException, self).__init__(message)
        self.error_code = error_code
        self.request_id = request_id

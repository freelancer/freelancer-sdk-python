class UserIdNotRetrievedException(Exception):
    """
    User ID could not retrieved
    """
    def __init__(self, message, error_code):
        super(UserIdNotRetrievedException, self).__init__(message)
        self.error_code = error_code


class UserJobsNotAddedException(Exception):
    """
    User jobs could not be added
    """
    def __init__(self, message, error_code):
        super(UserJobsNotAddedException, self).__init__(message)
        self.error_code = error_code


class UserJobsNotSetException(Exception):
    """
    User jobs could not be set
    """
    def __init__(self, message, error_code):
        super(UserJobsNotSetException, self).__init__(message)
        self.error_code = error_code


class UserJobsNotDeletedException(Exception):
    """
    User jobs could not be deleted
    """
    def __init__(self, message, error_code):
        super(UserJobsNotDeletedException, self).__init__(message)
        self.error_code = error_code


class UsersNotFoundException(Exception):
    """
    Users could not be found
    """
    def __init__(self, message, error_code):
        super(UsersNotFoundException, self).__init__(message)
        self.error_code = error_code

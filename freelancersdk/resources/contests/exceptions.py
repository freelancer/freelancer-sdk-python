class ContestNotCreatedException(Exception):
    """
    Contest could not be created
    """
    def __init__(self, message, error_code):
        super(ContestNotCreatedException, self).__init__(message)
        self.error_code = error_code

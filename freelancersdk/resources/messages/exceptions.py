class ThreadNotCreatedException(Exception):
    """
    Thread could not be created
    """
    def __init__(self, message, error_code):
        super(ThreadNotCreatedException, self).__init__(message)
        self.error_code = error_code


class MessageNotCreatedException(Exception):
    """
    Message could not be created
    """
    def __init__(self, message, error_code):
        super(MessageNotCreatedException, self).__init__(message)
        self.error_code = error_code

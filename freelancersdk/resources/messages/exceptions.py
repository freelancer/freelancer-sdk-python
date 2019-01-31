class ThreadNotCreatedException(Exception):
    """
    Thread could not be created
    """

    def __init__(self, message, error_code, request_id):
        super(ThreadNotCreatedException, self).__init__(message)
        self.error_code = error_code
        self.request_id = request_id


class MessageNotCreatedException(Exception):
    """
    Message could not be created
    """

    def __init__(self, message, error_code, request_id):
        super(MessageNotCreatedException, self).__init__(message)
        self.error_code = error_code
        self.request_id = request_id


class MessagesNotFoundException(Exception):
    """
    Messages could not be found
    """

    def __init__(self, message, error_code, request_id):
        super(MessagesNotFoundException, self).__init__(message)
        self.error_code = error_code
        self.request_id = request_id


class ThreadsNotFoundException(Exception):
    """
    Threads could not be found
    """

    def __init__(self, message, error_code, request_id):
        super(ThreadsNotFoundException, self).__init__(message)
        self.error_code = error_code
        self.request_id = request_id

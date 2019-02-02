class ProjectNotCreatedException(Exception):
    """
    Project could not be created
    """

    def __init__(self, message, error_code, request_id):
        super(ProjectNotCreatedException, self).__init__(message)
        self.error_code = error_code
        self.request_id = request_id


class BidNotPlacedException(Exception):
    """
    Bid could not be placed
    """

    def __init__(self, message, error_code, request_id):
        super(BidNotPlacedException, self).__init__(message)
        self.error_code = error_code
        self.request_id = request_id


class TrackNotFoundException(Exception):
    """
    Track could not be found
    """

    def __init__(self, message, error_code, request_id):
        super(TrackNotFoundException, self).__init__(message)
        self.error_code = error_code
        self.request_id = request_id


class TrackNotUpdatedException(Exception):
    """
    Track could not be updated
    """

    def __init__(self, message, error_code, request_id):
        super(TrackNotUpdatedException, self).__init__(message)
        self.error_code = error_code
        self.request_id = request_id


class TrackNotCreatedException(Exception):
    """
    Track could not be created
    """

    def __init__(self, message, error_code, request_id):
        super(TrackNotCreatedException, self).__init__(message)
        self.error_code = error_code
        self.request_id = request_id


class BidsNotFoundException(Exception):
    """
    Bids could not be found
    """

    def __init__(self, message, error_code, request_id):
        super(BidsNotFoundException, self).__init__(message)
        self.error_code = error_code
        self.request_id = request_id


class BidNotAwardedException(Exception):
    """
    Bid could not be awarded
    """

    def __init__(self, message, error_code, request_id):
        super(BidNotAwardedException, self).__init__(message)
        self.error_code = error_code
        self.request_id = request_id


class BidNotRevokedException(Exception):
    """
    Bid could not be revoked
    """

    def __init__(self, message, error_code, request_id):
        super(BidNotRevokedException, self).__init__(message)
        self.error_code = error_code
        self.request_id = request_id


class BidNotAcceptedException(Exception):
    """
    Bid could not be revoked
    """

    def __init__(self, message, error_code, request_id):
        super(BidNotAcceptedException, self).__init__(message)
        self.error_code = error_code
        self.request_id = request_id


class BidNotHighlightedException(Exception):
    """
    Bid could not be revoked
    """

    def __init__(self, message, error_code, request_id):
        super(BidNotHighlightedException, self).__init__(message)
        self.error_code = error_code
        self.request_id = request_id


class BidNotRetractedException(Exception):
    """
    Bid could not be revoked
    """

    def __init__(self, message, error_code, request_id):
        super(BidNotRetractedException, self).__init__(message)
        self.error_code = error_code
        self.request_id = request_id


class MilestonesNotFoundException(Exception):
    """
    Milestone could not be found
    """

    def __init__(self, message, error_code, request_id):
        super(MilestonesNotFoundException, self).__init__(message)
        self.error_code = error_code
        self.request_id = request_id


class MilestoneNotCreatedException(Exception):
    """
    Milestone could not be created
    """

    def __init__(self, message, error_code, request_id):
        super(MilestoneNotCreatedException, self).__init__(message)
        self.error_code = error_code
        self.request_id = request_id


class MilestoneNotReleasedException(Exception):
    """
    Milestone cout not be released
    """

    def __init__(self, message, error_code, request_id):
        super(MilestoneNotReleasedException, self).__init__(message)
        self.error_code = error_code
        self.request_id = request_id


class MilestoneNotRequestedReleaseException(Exception):
    """
    Milestone cout not be requested for released
    """

    def __init__(self, message, error_code, request_id):
        super(MilestoneNotRequestedReleaseException, self).__init__(message)
        self.error_code = error_code
        self.request_id = request_id


class MilestoneNotCancelledException(Exception):
    """
    Milestone cout not be cancelled
    """

    def __init__(self, message, error_code, request_id):
        super(MilestoneNotCancelledException, self).__init__(message)
        self.error_code = error_code
        self.request_id = request_id


class MilestoneRequestNotCreatedException(Exception):
    """
    Milestone request could not be created
    """

    def __init__(self, message, error_code, request_id):
        super(MilestoneRequestNotCreatedException, self).__init__(message)
        self.error_code = error_code
        self.request_id = request_id


class MilestoneRequestNotAcceptedException(Exception):
    """
    Milestone request could not be accepted
    """

    def __init__(self, message, error_code, request_id):
        super(MilestoneRequestNotAcceptedException, self).__init__(message)
        self.error_code = error_code
        self.request_id = request_id


class MilestoneRequestNotRejectedException(Exception):
    """
    Milestone request could not be rejected
    """

    def __init__(self, message, error_code, request_id):
        super(MilestoneRequestNotRejectedException, self).__init__(message)
        self.error_code = error_code
        self.request_id = request_id


class MilestoneRequestNotDeletedException(Exception):
    """
    Milestone request could not be deleted
    """

    def __init__(self, message, error_code, request_id):
        super(MilestoneRequestNotDeletedException, self).__init__(message)
        self.error_code = error_code
        self.request_id = request_id


class ReviewNotPostedException(Exception):
    """
    Review could not be posted
    """

    def __init__(self, message, error_code, request_id):
        super(ReviewNotPostedException, self).__init__(message)
        self.error_code = error_code
        self.request_id = request_id


class ProjectsNotFoundException(Exception):
    """
    Projects could not be found
    """

    def __init__(self, message, error_code, request_id):
        super(ProjectsNotFoundException, self).__init__(message)
        self.error_code = error_code
        self.request_id = request_id


class JobsNotFoundException(Exception):
    """
    Jobs could not be found
    """

    def __init__(self, message, error_code, request_id):
        super(JobsNotFoundException, self).__init__(message)
        self.error_code = error_code
        self.request_id = request_id

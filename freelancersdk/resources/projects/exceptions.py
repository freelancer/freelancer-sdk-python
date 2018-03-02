class ProjectNotCreatedException(Exception):
    """
    Project could not be created
    """
    def __init__(self, message, error_code):
        super(ProjectNotCreatedException, self).__init__(message)
        self.error_code = error_code


class BidNotPlacedException(Exception):
    """
    Bid could not be placed
    """
    def __init__(self, message, error_code):
        super(BidNotPlacedException, self).__init__(message)
        self.error_code = error_code


class BidsNotFoundException(Exception):
    """
    Bids could not be found
    """
    def __init__(self, message, error_code):
        super(BidsNotFoundException, self).__init__(message)
        self.error_code = error_code


class BidNotAwardedException(Exception):
    """
    Bid could not be awarded
    """
    def __init__(self, message, error_code):
        super(BidNotAwardedException, self).__init__(message)
        self.error_code = error_code


class BidNotRevokedException(Exception):
    """
    Bid could not be revoked
    """
    def __init__(self, message, error_code):
        super(BidNotRevokedException, self).__init__(message)
        self.error_code = error_code


class BidNotAcceptedException(Exception):
    """
    Bid could not be revoked
    """
    def __init__(self, message, error_code):
        super(BidNotAcceptedException, self).__init__(message)
        self.error_code = error_code


class BidNotHighlightedException(Exception):
    """
    Bid could not be revoked
    """
    def __init__(self, message, error_code):
        super(BidNotHighlightedException, self).__init__(message)
        self.error_code = error_code


class BidNotRetractedException(Exception):
    """
    Bid could not be revoked
    """
    def __init__(self, message, error_code):
        super(BidNotRetractedException, self).__init__(message)
        self.error_code = error_code


class MilestonesNotFoundException(Exception):
    """
    Milestone could not be found
    """
    def __init__(self, message, error_code):
        super(MilestonesNotFoundException, self).__init__(message)
        self.error_code = error_code


class MilestoneNotCreatedException(Exception):
    """
    Milestone could not be created
    """
    def __init__(self, message, error_code):
        super(MilestoneNotCreatedException, self).__init__(message)
        self.error_code = error_code


class MilestoneNotReleasedException(Exception):
    """
    Milestone cout not be released
    """
    def __init__(self, message, error_code):
        super(MilestoneNotReleasedException, self).__init__(message)
        self.error_code = error_code


class MilestoneNotRequestedReleaseException(Exception):
    """
    Milestone cout not be requested for released
    """
    def __init__(self, message, error_code):
        super(MilestoneNotRequestedReleaseException, self).__init__(message)
        self.error_code = error_code


class MilestoneNotCancelledException(Exception):
    """
    Milestone cout not be cancelled
    """
    def __init__(self, message, error_code):
        super(MilestoneNotCancelledException, self).__init__(message)
        self.error_code = error_code


class MilestoneRequestNotCreatedException(Exception):
    """
    Milestone request could not be created
    """
    def __init__(self, message, error_code):
        super(MilestoneRequestNotCreatedException, self).__init__(message)
        self.error_code = error_code


class MilestoneRequestNotAcceptedException(Exception):
    """
    Milestone request could not be accepted
    """
    def __init__(self, message, error_code):
        super(MilestoneRequestNotAcceptedException, self).__init__(message)
        self.error_code = error_code


class MilestoneRequestNotRejectedException(Exception):
    """
    Milestone request could not be rejected
    """
    def __init__(self, message, error_code):
        super(MilestoneRequestNotRejectedException, self).__init__(message)
        self.error_code = error_code


class MilestoneRequestNotDeletedException(Exception):
    """
    Milestone request could not be deleted
    """
    def __init__(self, message, error_code):
        super(MilestoneRequestNotDeletedException, self).__init__(message)
        self.error_code = error_code


class ReviewNotPostedException(Exception):
    """
    Review could not be posted
    """
    def __init__(self, message, error_code):
        super(ReviewNotPostedException, self).__init__(message)
        self.error_code = error_code


class ProjectsNotFoundException(Exception):
    """
    Projects could not be found
    """
    def __init__(self, message, error_code):
        super(ProjectsNotFoundException, self).__init__(message)
        self.error_code = error_code


class JobsNotFoundException(Exception):
    """
    Jobs could not be found
    """
    def __init__(self, message, error_code):
        super(JobsNotFoundException, self).__init__(message)
        self.error_code = error_code

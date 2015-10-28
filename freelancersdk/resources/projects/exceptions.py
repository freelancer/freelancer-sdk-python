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


class MilestoneNotCreatedException(Exception):
    """
    Milestone could not be created
    """
    def __init__(self, message, error_code):
        super(MilestoneNotCreatedException, self).__init__(message)
        self.error_code = error_code

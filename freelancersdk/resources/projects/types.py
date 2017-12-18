# Reference: https://www.freelancer.com/api/docs/structs/index

from enum import IntEnum


class Project:
    """
    Create a Project object from the JSON data
    retrieved from the API
    """
    def __init__(self, project_data):
        for k in iter(project_data):
            setattr(self, k, project_data[k])


class Bid:
    """
    Create a Bid object from the JSON data
    retrieved from the API
    """
    def __init__(self, project_data):
        for k in iter(project_data):
            setattr(self, k, project_data[k])


class Milestone:
    """
    Create a Milestone object from the JSON data
    retrieved from the API
    """
    def __init__(self, project_data):
        for k in iter(project_data):
            setattr(self, k, project_data[k])


class MilestoneRequest:
    """
    Create a Milestone Request object from the JSON data
    retrieved from the API
    """
    def __init__(self, milestone_request_data):
        for k in iter(milestone_request_data):
            setattr(self, k, milestone_request_data[k])


# Enumerations
# We use IntEnum to aid serialization by default
class ProjectType(IntEnum):
    """
    Project types
    """
    FIXED = 0
    HOURLY = 1


class MilestoneReason(IntEnum):
    """
    Reason for Milestone
    """
    FULL_PAYMENT = 0
    PARTIAL_PAYMENT = 1
    TASK_DESCRIPTION = 2
    OTHER = 3

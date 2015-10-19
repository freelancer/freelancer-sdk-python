from enum import IntEnum

class Project:
    def __init__(self, project_data):
        for k in iter(project_data):
            setattr(self, k, project_data[k])

class Bid:
    def __init__(self, project_data):
        for k in iter(project_data):
            setattr(self, k, project_data[k])

class Milestone:
    def __init__(self, project_data):
        for k in iter(project_data):
            setattr(self, k, project_data[k])

# Enumerations
# We use IntEnum to aid serialization by default
class ProjectType(IntEnum):
    FIXED = 0
    HOURLY = 1

class MilestoneReason(IntEnum):
    FULL_PAYMENT = 0
    PARTIAL_PAYMENT = 1
    TASK_DESCRIPTION = 2
    OTHER = 3

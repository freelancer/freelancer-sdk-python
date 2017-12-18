class Thread:
    """
    Create a Messages Thread object from the JSON data retrieved from the API
    """
    def __init__(self, project_data):
        for k in iter(project_data):
            setattr(self, k, project_data[k])


class Message:
    """
    Create a Messages object from the JSON data retrieved from the API
    """
    def __init__(self, project_data):
        for k in iter(project_data):
            setattr(self, k, project_data[k])

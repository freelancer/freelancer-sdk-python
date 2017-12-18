class Contest:
    """
    Create a Contest object from the JSON data retrieved from the API
    """
    def __init__(self, contest_data):
        for k in iter(contest_data):
            setattr(self, k, contest_data[k])

class InvalidWorkException(Exception):
    def __init__(self):
        self._message = "number of work can't be lesser than 1"

    def __str__(self):
        return self._message

    def get_message(self):
        return self._message

class KeyMissingError(Exception) :

    def __init__(self, message) -> None:

        self.message = f'your missing these keys: {message}'


class ValueTypeError(Exception) :

    def __init__(self, message) -> None:

        self.message = f'Only string type. These props has a different type: {set(message)}'
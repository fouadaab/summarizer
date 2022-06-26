class KeyMissingError(Exception) :

    def __init__(self, message) -> None:

        self.error = f'Unexpected Key ID returned: {message}'


class ValueTypeError(Exception) :

    def __init__(self) -> None:

        self.error = f'Only numeric type detected.'
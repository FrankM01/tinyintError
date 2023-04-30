class TinyIntError(Exception):
    def __init__(self):
        self.message = (
            "The number does not have the characteristics of a tinyInt number."
        )

    def __str__(self):
        return self.message

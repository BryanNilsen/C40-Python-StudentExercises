class Exercise():
    """
    Represents an exercise object
    Attributes:
        name (str): name of exercise
        language (str): language of exercise
    """

    def __init__(self, name, language):
        self.name = name
        self.language = language

    def __repr__(self):
        return f'{self.name} - {self.language}'

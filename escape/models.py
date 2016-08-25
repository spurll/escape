class Room:
    def __init__(self, name):
        self.name = name

    @property
    def something(self):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        return self.__repr__()


import copy


class Bus:
    def __init__(self, passengers) -> None:
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


class HauntedBus:
    def __init__(self, passengers=[]) -> None:
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']


class TwilightBus:

    def __init__(self, passengers=None) -> None:
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


bus = TwilightBus(basketball_team)
bus.drop('Sue')
bus.drop('Maya')
print(basketball_team)
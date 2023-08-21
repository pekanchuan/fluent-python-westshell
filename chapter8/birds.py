class Bird:
    pass


class Duck(Bird):
    def quack(self):
        print('Quack!')


def alert(birdie):
    birdie.quack()


def alert_duck(birdie: Duck) -> None:
    birdie.quack()


def alert_bird(birdie: Bird) -> None:
    birdie.quack()


if __name__ == "__main__":
    alert(Bird())

    alert_duck(Duck())

    alert_bird(Bird())

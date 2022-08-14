class Character:  # Base Character Class

    def __init__(self, name="New Char"):  # Default Constructor
        self.name = name
        self.health = 10
        self.attack = 5
        self.defence = 4
        self.speed = 3

    def print_stats(self):  # Prints the character's stats
        print(self.name)
        print(self.health)
        print(self.attack)
        print(self.defence)
        print(self.speed)


class Enemy(Character):  # Enemy class derived from Character

    def __init__(self, name="New Char"):  # Default Constructor
        super().__init__(name)
        self.exp_gain = 2
        self.gold_gain = 6

    def print_stats(self):  # Prints the enemy's stats
        super().print_stats()
        print(self.exp_gain)
        print(self.gold_gain)

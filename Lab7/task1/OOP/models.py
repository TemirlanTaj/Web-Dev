class Entity:
    def __init__(self, name, age, gender, is_mutated=False):
        self.name = name
        self.age = age
        self.gender = gender
        self.is_mutated = is_mutated

    def introduce(self):
        if self.is_mutated:
            mutant_status = "Mutant"
        else :
            mutant_status = "Regular"
        return f"I am {self.name}, {self.age} years old, {self.gender}. Status: {mutant_status}"

    def status(self):
        return f"{self.name} exists in the world of Teenage Mutant Ninja Turtles."

    def __str__(self):
        return f"Entity({self.name}, {self.age}, {self.gender}, mutant={self.is_mutated})"


class Turtle(Entity):
    def __init__(self, name, age, gender, weapon, color):
        super().__init__(name, age, gender, is_mutated=True)
        self.weapon = weapon
        self.color = color

    def fight(self):
        return f"{self.name} attacks with weapon {self.weapon}!"

    def status(self):  # override
        return f"{self.name} is a ninja turtle in a {self.color} mask. His weapon is {self.weapon}."

    def __str__(self):
        return f"Turtle({self.name}, mask={self.color}, weapon={self.weapon})"


class Villain(Entity):
    def __init__(self, name, age, gender, evil_plan):
        super().__init__(name, age, gender, is_mutated=True)
        self.evil_plan = evil_plan

    def threaten(self):
        return f"{self.name}: 'My plan is to {self.evil_plan}. You cannot stop me!'"

    def status(self):  # override
        return f"{self.name} is a villain. His plan: {self.evil_plan}."

    def __str__(self):
        return f"Villain({self.name}, plan={self.evil_plan})"
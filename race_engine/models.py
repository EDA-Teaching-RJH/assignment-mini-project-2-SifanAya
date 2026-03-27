import random
class Horse:
    def __init__(self, name): self.name = name
    def get_speed(self): return random.randint(1, 10)

class ProHorse(Horse):
    def get_speed(self): return random.randint(1, 10) + 5
class Subject:
    def __init__(self, name, difficulty=1):
        self.name = name
        self.difficulty = difficulty

    def adjust_difficulty(self, score):
        if score < 50:
            self.difficulty += 1
        elif score > 80 and self.difficulty > 1:
            self.difficulty -= 1

    def to_dict(self):
        return {"name": self.name, "difficulty": self.difficulty}

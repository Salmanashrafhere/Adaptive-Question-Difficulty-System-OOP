from subject import Subject

class Learner:
    def __init__(self, name):
        self.name = name
        self.subjects = {}
        self.history = []

    def add_subject(self, name, difficulty=1):
        self.subjects[name] = Subject(name, difficulty)

    def record_performance(self, subject, score, time_spent):
        self.history.append({
            "subject": subject,
            "score": score,
            "time": time_spent
        })
        self.subjects[subject].adjust_difficulty(score)

    def to_dict(self):
        return {
            "name": self.name,
            "subjects": {k: v.to_dict() for k,v in self.subjects.items()},
            "history": self.history
        }

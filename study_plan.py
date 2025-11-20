class StudyPlan:
    def __init__(self, learner):
        self.learner = learner

    def generate_plan(self):
        plan = {}
        for name, subject in self.learner.subjects.items():
            time = 30 + subject.difficulty * 10
            plan[name] = time
        return plan

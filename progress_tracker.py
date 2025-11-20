import json
import os

class ProgressTracker:
    FILE = "progress.json"

    @staticmethod
    def save(learner):
        with open(ProgressTracker.FILE, "w") as f:
            json.dump(learner.to_dict(), f, indent=4)

    @staticmethod
    def load():
        if not os.path.exists(ProgressTracker.FILE):
            return None
        with open(ProgressTracker.FILE, "r") as f:
            return json.load(f)

from learner import Learner
from study_plan import StudyPlan
from progress_tracker import ProgressTracker

def menu():
    data = ProgressTracker.load()
    if data:
        learner = Learner(data['name'])
        for s, info in data['subjects'].items():
            learner.add_subject(s, info['difficulty'])
        learner.history = data['history']
    else:
        name = input("Enter learner name: ")
        learner = Learner(name)
        n = int(input("How many subjects? "))
        for _ in range(n):
            s = input("Subject name: ")
            learner.add_subject(s)

    while True:
        print("\n1. Record Performance\n2. Generate Study Plan\n3. Save Progress\n4. Exit")
        ch = input("Choice: ")

        if ch == "1":
            s = input("Subject: ")
            score = int(input("Score: "))
            time = int(input("Time spent (mins): "))
            learner.record_performance(s, score, time)

        elif ch == "2":
            plan = StudyPlan(learner).generate_plan()
            print("\nAdaptive Study Plan:")
            for k,v in plan.items():
                print(f"{k}: {v} mins")

        elif ch == "3":
            ProgressTracker.save(learner)
            print("Progress saved.")

        else:
            break

if __name__ == "__main__":
    menu()

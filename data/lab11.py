import matplotlib.pyplot as plt

students = []
with open("students.txt") as f:
    for line in f:
        line = line.strip()
        score = int(line[:3])
        name = line[3:].strip()
        students.append(name)

assignments = {}

with open("submissions/assignments.txt") as f:
    lines = [line.strip() for line in f]

i = 0
while i < len(lines):
    name = lines[i]
    digits = lines[i+1]
    points = int(lines[i+2])

    scores = [int(d) for d in digits]

    assignments[name] = (scores, points)

    i += 3

print("1. Student grade")
print("2. Assignment statistics")
print("3. Assignment graph\n")

selection = input("Enter your selection: ")

if selection == "1":
    name = input("What is the student's name: ").strip()

    if name not in students:
        print("Student not found")
        exit()

    idx = students.index(name)
    total = 0
    total_possible = 0

    for assign, (scores, points) in assignments.items():
        d = scores[idx]
        earned = (d / 9) * points
        total += earned
        total_possible += points

    percent = round(total / total_possible * 100)
    print(f"{percent}%")

elif selection == "2":
    name = input("What is the assignment name: ").strip()

    if name not in assignments:
        print("Assignment not found")
        exit()

    scores, points = assignments[name]

    percentages = [(d / 9) * 100 for d in scores]

    print(f"Min: {round(min(percentages))}%")
    print(f"Avg: {round(sum(percentages)/len(percentages))}%")
    print(f"Max: {round(max(percentages))}%")

elif selection == "3":
    name = input("What is the assignment name: ").strip()

    if name not in assignments:
        print("Assignment not found")
        exit()

    scores, points = assignments[name]

    percentages = [(d / 9) * 100 for d in scores]

    plt.hist(percentages, bins=[0,25,50,75,100])
    plt.show()


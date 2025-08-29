student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

for key in student_scores:
    if student_scores[key] >= 91:
        student_scores[key] = "Outstanding"
        # etc..
print(student_scores)

def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def get_score(subject_name):
    while True:
        try:
            score = float(input("Enter score for " + subject_name + ": "))
            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def collect_scores(num_students, num_subjects):
    scores = {}

    for student in range(1, num_students + 1):
        print("\nEntering scores for student", student)
        student_scores = {}
        for subject in range(1, num_subjects + 1):
            subject_name = input("Enter subject name: ")
            score = get_score(subject_name)
            student_scores[subject_name] = score
        scores["Student " + str(student)] = student_scores
        print("Saved successfully")

    return scores


def display_summary(scores):
    print("=========================================================================")
    print("STUDENTS        SUB1    SUB2    SUB3    TOT    AVE      POS")
    print("=========================================================================")

    student_count = 1
    for student, student_scores in scores.items():
        print(student, end='')
        total = 0
        for subject, score in student_scores.items():
            print("      {:.2f}".format(score), end='')
            total += score
        average = total / len(student_scores)
        print("    {:.2f}    {:.2f}    {}".format(total, average, student_count))
        student_count += 1

    print("=========================================================================")
    print("=========================================================================")


def main():
    print("Welcome Teacher! Enter students' numbers and scores\n")

    num_students = get_integer_input("How many students do you have? ")
    num_subjects = get_integer_input("How many subjects do they offer? ")

    print("Saved successfully")

    print("\nEntering scores...")
    scores = collect_scores(num_students, num_subjects)

    display_summary(scores)


if __name__ == "__main__":
    main()

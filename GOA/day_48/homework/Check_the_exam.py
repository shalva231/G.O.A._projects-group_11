# This function calculates the score for a student based on their answers to a multiple-choice exam.
def check_exam(arr1, arr2):
    # Initialize an index variable to keep track of the current question.
    index = 0
    # Initialize a score variable to keep track of the student's total score.
    score = 0

    # Iterate through each answer in the second array (student's answers).
    for i in arr2:
        # If the student's answer matches the correct answer, add 4 points to the score.
        if i == arr1[index]:
            score += 4
        # If the student's answer is empty (did not attempt the question), add 0 points to the score.
        elif i == "":
            score += 0
        # If the student's answer is incorrect, subtract 1 point from the score.
        else:
            score -= 1
        # Move to the next question by increasing the index.
        index += 1

    # If the score is less than 0, return 0 as the final score.
    if score < 0:
        return 0
    # Otherwise, return the calculated score.
    else:
        return score
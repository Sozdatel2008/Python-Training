def get_grade(s1, s2, s3):
    total = s1 + s2 + s3
    score = total / 3
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    else:
        return 'F'

  #Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.

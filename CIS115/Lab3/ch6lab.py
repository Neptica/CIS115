def main():
    fil_inp_stu = open("student_test_scores.txt", "r")

    numberFailing = 0
    numberStudents = 0
    numberPassing = 0
    totalScores = 0

    print("#\tScore\tStatus\n----------------------------")
    one_score = fil_inp_stu.readline()
    while one_score != "":
        one_score_int = int(one_score)
        totalScores += one_score_int
        numberStudents += 1
        if one_score_int >= 50:
            print(f"{numberStudents:>2d}      {one_score_int:>4d}")
            numberPassing += 1
        else:
            print(f"{numberStudents:>2d}      {one_score_int:>4d}      X")
            numberFailing += 1
        one_score = fil_inp_stu.readline()
    averageScore = totalScores / numberStudents
    averageRateFailure = numberFailing / numberStudents * 100
    print(f"Number of Students         : {numberStudents}")
    print(f"Average Score              : {averageScore:.2f}")
    print(f"Students with Scores <= 50 : {numberFailing} ({averageRateFailure:.1f}%)")
    fil_inp_stu.close()

main()

###	Score	Status
##----------------------------
## 1        69
## 2         9      X
## 3       129
## 4       131
## 5       146
## 6       109
## 7        71
## 8        69
## 9        18      X
##10       129
##11        94
##12        53
##13        25      X
##Number of Students         : 13
##Average Score              : 80.92
##Students with Scores <= 50 : 3 (23.1%)

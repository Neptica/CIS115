##Michael Mumme, Grading students from a list and singling out As and Bs

import random
def main():
    size = 11
    lst_stu_names = ["Vernon", "Domenic", "Michael", "Celena",
                    "Odis", "Rufus", "Rose", "Cheryll",
                     "Mignon", "Monte", "Ralph"]

    lst_stu_grades = [""] * size

    for i in range(size):
         lst_stu_grades[i] = random.choice(["A", "B", "C", "D", "F"])

    num_A_stu = 0
    num_B_stu = 0
    tot_rec = 0
    
    print(" # Student\tGrade\n--------------------------")

    for i in range(size):
        tot_rec += 1
        grade = lst_stu_grades[i]
        st_name = lst_stu_names[i]
        if grade == "A":
            message = "**"
            num_A_stu += 1
        elif grade == "B":
            message = "*"
            num_B_stu += 1
        else:
            message = " "
        
        print(f"{tot_rec:>2d}. {st_name:<11}\t  {grade} {message:>4}")

    num_AB_stu = num_A_stu + num_B_stu
    
    print()
    print(f"Total Students   : {size:>2}")
    print(f"'A' Students     : {num_A_stu:>2} ({num_A_stu/tot_rec:>.1%})")
    print(f"'B' Students     : {num_B_stu:>2} ({num_B_stu*100/tot_rec:>.1f}%)")
    print(f"'A', 'B' Students: {num_AB_stu:>2} ({(num_A_stu+num_B_stu)/tot_rec:>.1%})")

main()

## # Student	Grade
##--------------------------
## 1. Vernon      D     
## 2. Domenic     D     
## 3. Michael     B    *
## 4. Celena      B    *
## 5. Odis        D     
## 6. Rufus       D     
## 7. Rose        A   **
## 8. Cheryll     A   **
## 9. Mignon      D     
##10. Monte       C     
##11. Ralph       D     
##
##Total Students   : 11
##'A' Students     :  2 (18.2%)
##'B' Students     :  2 (18.2%)
##'A', 'B' Students:  4 (36.4%)

## # Student	Grade
##--------------------------
## 1. Vernon      B    *
## 2. Domenic     F     
## 3. Michael     A   **
## 4. Celena      D     
## 5. Odis        A   **
## 6. Rufus       A   **
## 7. Rose        D     
## 8. Cheryll     B    *
## 9. Mignon      D     
##10. Monte       F     
##11. Ralph       D     
##
##Total Students   : 11
##'A' Students     :  3 (27.3%)
##'B' Students     :  2 (18.2%)
##'A', 'B' Students:  5 (45.5%)

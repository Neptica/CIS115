##Michael Mumme, week 9, Lab 2

import random
def main():
    score_1 = random.randint(55,100)
    score_2 = random.randint(55,100)
    score_3 = random.randint(55,100)

    avg_score = get_average(score_1, score_2, score_3)
    
    #Invoke get_grade with avg_score as the argument to the
    #function invocation
    letter_grade = get_grade(avg_score)
    
    print(f"Score 1       : {score_1:.1f}")
    print(f"Score 2       : {score_2:.1f}")
    print(f"Score 3       : {score_3:.1f}")
    print(f"Average score : {avg_score:.1f}")
    print(f"Letter Grade  : {letter_grade}")
    
# The calc_average function calculates and returns average
# of the 3 grades sent in as arguments
def get_average(param_1, param_2, param_3):
    avg_param = (param_1 + param_2 + param_3) / 3.0
    return avg_param

# The get_grade function receives a numeric  
# grade as a parameter and returns the corresponding letter grade 
def get_grade(score):
    if score >= 90:
        grade = "A"
    else:
        if score >= 80:
            grade = "B"
        else:
            if score >= 70:
                grade = "C"
            else:
                if score >= 60:
                    grade = "D"
                else:
                    grade = "F"

    return grade

# Call the main function.
main()

##Score 1       : 68.0
##Score 2       : 91.0
##Score 3       : 62.0
##Average score : 73.7
##Letter Grade  : C
##
##Score 1       : 96.0
##Score 2       : 85.0
##Score 3       : 98.0
##Average score : 93.0
##Letter Grade  : A
##
##Score 1       : 80.0
##Score 2       : 70.0
##Score 3       : 76.0
##Average score : 75.3
##Letter Grade  : C

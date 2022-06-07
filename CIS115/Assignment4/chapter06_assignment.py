def main():
    file_students = open("student_points.txt", "r")
    stu_name = file_students.readline()  #read the first record,
                                        #which is the first stduent's name
    num_stu = 0
    num_failed_students = 0
    num_passed_students = 0
    print(f"#R  Student           Points    Grade")
    print("--------------------------------------\n")
    while stu_name != "":
        stu_name = stu_name.rstrip("\n")        #strip \n from name
        stu_points = file_students.readline()   #read numeric points
        stu_points = int(stu_points)            #cast points into an int
        num_stu += 1
        if stu_points < 60:
            print(f"#{num_stu:>1}  {stu_name:15}     {stu_points}      **F**")
            num_failed_students += 1
        else:
            print(f"#{num_stu:>1}  {stu_name:15}     {stu_points}")
            num_passed_students += 1
        
        stu_name = file_students.readline()

    avg_passed = num_passed_students / num_stu * 100
    file_students.close()
    print()
    print(f"Number of students processed  =  {num_stu}")
    print(f"Number of 'F' students        =  {num_failed_students}")
    print(f"% of students who passed      =  {avg_passed:.1f}%")


main()


##  #R  Student           Points    Grade
##  --------------------------------------
##  
##  #1  Johnson Smith       93
##  #2  Maryanne James      80
##  #3  Stanton Chase       45      **F**
##  #4  Mildred Morris      90
##  #5  George Deitz        58      **F**
##  #6  Maisie Kling        79
##
##  Number of students processed  =  6
##  Number of 'F' students        =  2
##  % of students who passed      =  66.7%

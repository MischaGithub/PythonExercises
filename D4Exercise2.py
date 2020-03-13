grade_A = 80-100
grade_B = 60-79
grade_C = 50-59
grade_D = 0-49
#PROMPTING THE USER TO ENTER THE MARK
first_Name = input("Please Enter Student First Name \n")
sur_Name = input("Please Enter Student Last Name \n")
mark_Stu = float(input("Please Enter Student mark \n"))
#Creating a loop to display the correct mark per category
if mark_Stu >= 0 and mark_Stu <= 49:
    print(str(first_Name), str(sur_Name), "Grade D-Failed")
elif mark_Stu >= 50 and mark_Stu <= 59:
    print(str(first_Name), str(sur_Name), "Grade C-Pass")
elif mark_Stu >= 60 and mark_Stu <= 79:
    print(str(first_Name), str(sur_Name), "Grade B-Satisfactory")
elif mark_Stu >= 80 and mark_Stu <= 100:
    print(str(first_Name), str(sur_Name), "Grade A-Outstanding")








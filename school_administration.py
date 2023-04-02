condition = True
while(condition):
    student_info=input("Enter student info :")
    print(student_info)
    condition_check=input("Enter yes/no  if you want to enter another student info:")
    if condition_check=="yes":
        condition=True
    else condition_check=="no":
        condition=False

with open("reg_form.txt",'a+') as file:
    student_count=int(input("How many syudents are registering: "));
    student_id=[];
    for i in range(student_count):
        student_id.append(input("Enter student id: "));
        file.write(student_id[i]+"..........."+"\n");
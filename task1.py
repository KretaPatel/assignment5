
#Declaring Dictionary:
student={'Alice':85,'Mike':90,'Nick':87}


#Taking Name of Unit:
name=str(input("Enter Name Of Students Whose marks you want to search:"))


#prints the ddata of students:
if name in student.keys():

    print(name,'\'s marks:',student[name])
else:
    print("Student Not found.")
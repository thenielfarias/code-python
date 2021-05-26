gradesList=[]

grade1=int(input("Type the first grade: "))
gradesList.append(grade1)

grade2=int(input("Type the second grade: "))
gradesList.append(grade2)

grade3=int(input("Type the third grade: "))
gradesList.append(grade3)

grade4=int(input("Type the fourth grade: "))
gradesList.append(grade4)

grade5=int(input("Type the fifth grade: "))
gradesList.append(grade5)

grade6=int(input("Type the sixth grade: "))
gradesList.append(grade6)

grade7=int(input("Type the seventh grade: "))
gradesList.append(grade7)

grade8=int(input("Type the eighth grade: "))
gradesList.append(grade8)

grade9=int(input("Type the ninth grade: "))
gradesList.append(grade9)

grade10=int(input("Type the tenth grade: "))
gradesList.append(grade10)

gradesList.sort()

print("The lowest grade is " +str(gradesList[0]))
print("The highest grade is " +str(gradesList[9]))
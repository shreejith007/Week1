student_height=input("Enter the list of height").split()

for n in range(0,len(student_height)):
    student_height[n]=int(student_height[n])
print(student_height)
total_height=0
for height in student_height:
    total_height +=height
print(total_height)
student_no= 0
for x in student_height:
    student_no += 1
print(student_no)
Average_height =round(total_height/student_no)
print(Average_height)
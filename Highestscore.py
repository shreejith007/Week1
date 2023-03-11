student_score =input("Input the mark in the list").split()
for n in range(0,len(student_score)):
    student_score[n]=int (student_score[n])
print("THE STUDENT SCORE"+ str(student_score))
print("Highest Score"+ " " +str(max(student_score)))
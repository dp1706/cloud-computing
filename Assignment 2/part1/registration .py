

print("-------registration----------")
name=input("enter student name: ")
roll_no=input("enter roll no.")
sem=input("enter semester")
branch=int(input(" branch \n 1. CSE \n 2. ECE \n "))
year=input("enter your year")

content_array = []
with open('available_course.txt') as f:
             
        for line in f:
                content_array.append(line)
course_arr  = []
final_course = []
if(branch == 1):
    print("List of courses available for you are following:-")
    for i in content_array:
        if "CS"+year in i:
            course_arr.append(i)
           
        if "SC"+year in i:
            course_arr.append(i)
            
        if "HS"+year in i:
            course_arr.append(i)
    for j in range(len(course_arr)): 
        print (j+1, end = " ") 
        print (course_arr[j])
    
elif(branch==2):
    print("List of courses available for you are following:-")
    for i in content_array:
        if "EC"+year in i:
            course_arr.append(i)
            
        if "SC"+year in i:
            course_arr.append(i)
            
        if "HS"+year in i:
            course_arr.append(i)
    for j in range(len(course_arr)): 
        print (j+1, end = " ") 
        print (course_arr[j])
else:
    print("Choose Correct Branch")
    exit




print("how many courses \n")
n=int(input())
print("Select the course from the above  courses:-")

for i in range(n):
    cno = int(input())
    final_course.append(course_arr[cno-1])


print("You have successfully registered")
f = open("stud_info.txt", "a")

f.write("\n")
f.write("Name : "+name +"\n"+"Roll no: " + roll_no +"\n"+"Branch : "+str(branch)+"\n")

for j in range(len(final_course)): 
    f.write(final_course[j]+"\n")

f.close()

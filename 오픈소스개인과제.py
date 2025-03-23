def indata(): 
    ID=int(input(" 학번: "))
    name=str(input(" 이름: "))
    English=int(input(" 영어: "))
    C=int(input(" C언어: "))
    Python=int(input(" 파이썬썬: "))
    student=[ID,name,English,C,Python]
    return student
def total(student):
    all=0
    for i in range(2,5):
        all+=student[i]
    return all
def average(all):
    avg=all/3
    return avg
def gpa(avg):
    if avg>=95:
        return 'A+'
    elif avg>=90:
        return 'A0'
    elif avg>=85:
        return 'B+'
    elif avg>=80:
        return 'B0'
    elif avg>=75:
        return 'C+'
    elif avg>=70:
        return 'C0'
    else:
        return 'F'
def outdata(studentlist):
    for student in studentlist:
        print(f"{student[0]}     {student[1]}          {student[2]}         {student[3]}         {student[4]}         {student[5]}      {student[6]:.2f}     {student[7]}         {student[8]}")
    return 0

def rank(studentlist):
    ranking=[]
    gparanking=[]
    studentgpa=[]
    for stu in studentlist:
        studentgpa.append(stu[7])
        gparanking.append(stu[7])
    gparanking.sort(reverse=True)
    for gpa in gparanking:
        for i, stu in enumerate(studentlist):
            if stu[7] == gpa and (i + 1) not in ranking:
                ranking.append(i + 1)
                stu.append(ranking[-1])
                break

    return studentlist


studentlist=[]
personnel=int(input("총원: "))
for i in range(personnel):
    data=indata()
    all=total(data)
    avg=average(all)
    grade=gpa(avg)
    student=data+[all, avg, grade]
    studentlist.append(student)
studentlist=rank(studentlist)
print("                               성적관리 프로그램")
print(" =============================================================================")
print("학번                    이름                 영어      C-언어      파이썬         총점       평균         학점          등수")
outdata(studentlist) 
print(" =============================================================================")

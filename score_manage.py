# 성적관리 프로그램

def indata(): 
    ID = int(input("학번: "))
    name = input("이름: ")
    English = int(input("영어: "))
    C = int(input("C-언어: "))
    Python = int(input("파이썬: "))
    return [ID, name, English, C, Python]

def total(student):
    return sum(student[2:5])  # 총점 계산

def average(all_score):
    return all_score / 3  # 평균 계산

def gpa(avg):
    if avg >= 95:
        return 'A+'
    elif avg >= 90:
        return 'A0'
    elif avg >= 85:
        return 'B+'
    elif avg >= 80:
        return 'B0'
    elif avg >= 75:
        return 'C+'
    elif avg >= 70:
        return 'C0'
    else:
        return 'F'

def rank(studentlist):
    studentlist.sort(key=lambda x: x[5], reverse=True)  # 총점 기준 내림차순 정렬
    for i, student in enumerate(studentlist):
        student[8] = i + 1  # 등수 저장

def outdata(studentlist):
    print("\n                               성적관리 프로그램")
    print("=" * 85)
    print("학번       이름       영어    C-언어    파이썬    총점    평균    학점    등수")
    for student in studentlist:
        print(f"{student[0]:<10}{student[1]:<10}{student[2]:<7}{student[3]:<7}{student[4]:<7}"
              f"{student[5]:<7}{student[6]:.2f}   {student[7]:<5} {student[8]:<5}")
    print("=" * 85)

def insert(studentlist):
    student = indata()
    all_score = total(student)
    avg = average(all_score)
    grade = gpa(avg)
    student += [all_score, avg, grade, 0]  # 총점, 평균, 학점, 등수 추가
    studentlist.append(student)
    rank(studentlist)  # 삽입 후 등수 재계산

def search(studentlist):
    name = input("이름을 입력하세요: ")
    id = int(input("학번을 입력하세요: "))
    for student in studentlist:
        if student[0] == id and student[1] == name:
            print("=" * 85)
            print("학번       이름       영어    C-언어    파이썬    총점    평균    학점    등수")
            print(f"{student[0]:<10}{student[1]:<10}{student[2]:<7}{student[3]:<7}{student[4]:<7}"
                  f"{student[5]:<7}{student[6]:.2f}   {student[7]:<5} {student[8]:<5}")
            print("=" * 85)
            return student
    print("잘못된 이름 혹은 학번입니다.")
    return None

def delete(studentlist):
    student = search(studentlist)
    if student is None:
        print("해당 학생을 삭제할 수 없습니다.")
        return
    studentlist.remove(student)
    rank(studentlist)  # 삭제 후 등수 재계산
    print("학생 정보가 삭제되었습니다.")

def sort_total(studentlist):
    studentlist.sort(key=lambda x: x[5], reverse=True)  # 총점 기준 내림차순 정렬
    rank(studentlist)  # 정렬 후 등수 재계산

def count80(studentlist):
    count = sum(1 for student in studentlist if student[6] >= 80)
    print(f"평균 80점 이상 학생 수: {count}")

# 프로그램 실행
studentlist = []
personnel = int(input("총원: "))

for _ in range(personnel):
    student = indata()
    all_score = total(student)
    avg = average(all_score)
    grade = gpa(avg)
    student += [all_score, avg, grade, 0]  # 🔥 등수(0)를 미리 추가하여 오류 방지
    studentlist.append(student)

rank(studentlist)  # 초기 데이터 입력 후 등수 계산
outdata(studentlist)

# 메뉴 실행
while True:
    print("\n1. 학생 삽입")
    print("2. 학생 삭제")
    print("3. 학생 탐색")
    print("4. 학생 총점 정렬")
    print("5. 평균 80점 이상 학생 카운트")
    print("6. 나가기")
    
    choice = int(input("입력>> "))
    
    if choice == 1:
        insert(studentlist)
        outdata(studentlist)
    elif choice == 2:
        delete(studentlist)
        outdata(studentlist)
    elif choice == 3:
        search(studentlist)
    elif choice == 4:
        sort_total(studentlist)
        outdata(studentlist)
    elif choice == 5:
        count80(studentlist)
    elif choice == 6:
        print("메뉴를 나갑니다.")
        break
    else:
        print("잘못된 입력입니다. 다시 시도하세요.")

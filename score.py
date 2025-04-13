##################

  #프로그램명: score.py

  #작성자: 소프트웨어학부 인공지능학과과

  #작성일: 2025-04-13

  #프로그램 설명: 성적 분석, 산출 코드드

  ###################

class Student:
    def __init__(self, student_id, name, english, c_lang, python):
        self.student_id = student_id
        self.name = name
        self.english = english
        self.c_lang = c_lang
        self.python = python
        self.total = self.calculate_total()
        self.average = self.calculate_average()
        self.grade = self.calculate_grade()
        self.rank = 0

    def calculate_total(self):
        return self.english + self.c_lang + self.python

    def calculate_average(self):
        return self.total / 3

    def calculate_grade(self):
        avg = self.average
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

    def update_scores(self, english, c_lang, python):
        self.english, self.c_lang, self.python = english, c_lang, python
        self.total = self.calculate_total()
        self.average = self.calculate_average()
        self.grade = self.calculate_grade()


class Gradebook:
    def __init__(self):
        self.students = []

    def insert_student(self):
        student_id = int(input("학번: "))
        name = input("이름: ")
        english = int(input("영어: "))
        c_lang = int(input("C-언어: "))
        python = int(input("파이썬: "))
        student = Student(student_id, name, english, c_lang, python)
        self.students.append(student)
        self.calculate_ranks()

    def delete_student(self):
        student = self.search_student()
        if student:
            self.students.remove(student)
            self.calculate_ranks()
            print("학생 정보가 삭제되었습니다.")

    def search_student(self):
        name = input("이름을 입력하세요: ")
        student_id = int(input("학번을 입력하세요: "))
        for student in self.students:
            if student.student_id == student_id and student.name == name:
                self.display_student(student)
                return student
        print("잘못된 이름 혹은 학번입니다.")
        return None

    def sort_by_total(self):
        self.students.sort(key=lambda s: s.total, reverse=True)
        self.calculate_ranks()

    def count_above_80(self):
        count = sum(1 for student in self.students if student.average >= 80)
        print(f"평균 80점 이상 학생 수: {count}")

    def calculate_ranks(self):
        self.students.sort(key=lambda s: s.total, reverse=True)
        for idx, student in enumerate(self.students):
            student.rank = idx + 1

    def display_all(self):
        print("\n성적관리 프로그램")
        print("=" * 85)
        print("학번       이름       영어    C-언어    파이썬    총점    평균    학점    등수")
        for s in self.students:
            print(f"{s.student_id:<10}{s.name:<10}{s.english:<7}{s.c_lang:<7}{s.python:<7}"
                  f"{s.total:<7}{s.average:.2f}   {s.grade:<5} {s.rank:<5}")
        print("=" * 85)

    def display_student(self, student):
        print("=" * 85)
        print("학번       이름       영어    C-언어    파이썬    총점    평균    학점    등수")
        print(f"{student.student_id:<10}{student.name:<10}{student.english:<7}{student.c_lang:<7}{student.python:<7}"
              f"{student.total:<7}{student.average:.2f}   {student.grade:<5} {student.rank:<5}")
        print("=" * 85)


def main():
    import traceback
    gb = Gradebook()
    try:
        personnel = int(input("총원: "))
        for _ in range(personnel):
            gb.insert_student()
        gb.display_all()

        while True:
            print("\n1. 학생 삽입")
            print("2. 학생 삭제")
            print("3. 학생 탐색")
            print("4. 학생 총점 정렬")
            print("5. 평균 80점 이상 학생 카운트")
            print("6. 나가기")

            choice = int(input("입력>> "))
            if choice == 1:
                gb.insert_student()
                gb.display_all()
            elif choice == 2:
                gb.delete_student()
                gb.display_all()
            elif choice == 3:
                gb.search_student()
            elif choice == 4:
                gb.sort_by_total()
                gb.display_all()
            elif choice == 5:
                gb.count_above_80()
            elif choice == 6:
                print("메뉴를 나갑니다.")
                break
            else:
                print("잘못된 입력입니다. 다시 시도하세요.")
    except Exception:
        print("🔥 예외 발생! 아래 에러 메시지를 확인하세요:")
        traceback.print_exc()


if __name__ == "__main__":
    main()

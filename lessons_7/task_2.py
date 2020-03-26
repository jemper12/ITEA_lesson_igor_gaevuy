"""
Создать базу данных студентов. У студента есть факультет, группа, оценки, номер студенческого билета.
Написать программу, с двумя ролями: Администратор, Пользователь.
Администратор может добавлять, изменять существующих студентов.
Пользователь может получать список отличников, список всех студентов, искать студентов по по номеру студенческого,
    получать полную информацию о конкретном студенте (включая оценки, факультет)
"""

from lessons_7.task_1 import ContexSqlManager

sql_get_all_student = """
select student.id,
       first_name,
       last_name,
       student_ticket,
       group_name,
       faculty_name,
       (select GROUP_CONCAT(evaluation_num) from  evaluation where student_id = student.id) as evaluation
from student
         left join student_group on student.group_id = student_group.id
         left join faculty on faculty.id = student_group.faculty_id
"""

sql_find_student_ticket = """
select student.id as id,
       first_name,
       last_name,
       student_ticket,
       group_name,
       faculty_name,
       (select GROUP_CONCAT(evaluation_num) from  evaluation where student_id = student.id) as evaluation
from student
         left join student_group on student.group_id = student_group.id
         left join faculty on faculty.id = student_group.faculty_id
where student.student_ticket = ?
"""

sql_add_new_student = """
insert into student (first_name, last_name, group_id, student_ticket)
values (?, ?, ?, ?)
"""

sql_add_evaluation_on_student = """
insert into evaluation (evaluation_num, student_id)
values (?,?)
"""

sql_delete_student = """
delete from student where id = ?;
"""

sql_delete_evaluation_on_student = """
delete from evaluation where student_id = ?;
"""

sql_edit_student = """
update student
set first_name = ?,
    last_name  = ?,
    group_id   = ?
where id = ?
"""

sql_select_excellent_students = """
select distinct student.id,
                first_name,
                last_name,
                student_ticket
from student
         left join evaluation on student.id = evaluation.student_id
where evaluation.evaluation_num is 5
"""

sql_select_all_group = """
select id, group_name from student_group
"""


class User:
    def __init__(self, db):
        self._db = db

    @property
    def get_all_student(self):
        result = self._db.my_select(sql_get_all_student)
        return result


class Admin(User):

    def add_new_student(self, first_name, last_name, group, student_ticket):
        self._db.my_execute(sql_add_new_student, first_name, last_name, group, student_ticket)

    def add_evaluation_to_student(self, evaluation_num, student_id):
        self._db.my_execute(sql_add_evaluation_on_student, evaluation_num, student_id)

    def edit_student(self, student_id, first_name, last_name, group_id):
        self._db.my_execute(sql_edit_student, first_name, last_name, group_id, student_id)

    @property
    def get_all_group(self):
        result = self._db.my_select(sql_select_all_group)
        return result

    def delete_student(self, student_id):
        self._db.my_execute(sql_delete_student, student_id)
        self._db.my_execute(sql_delete_evaluation_on_student, student_id)


class Student(User):

    @property
    def excellent_students(self):
        result = self._db.my_select(sql_select_excellent_students)
        return result

    def find_student_ticket(self, student_ticket):
        result = self._db.my_select(sql_find_student_ticket, student_ticket)
        return result


def admin_logic(db):
    admin = Admin(db)
    while True:
        response_admin = input('Ok, you are admin, what do you want to do?\n\t'
                               '1) Add new student\n\t'
                               '2) Get all student\n\t'
                               '3) Add evaluation on student\n\t'
                               '4) Edit student\n\t'
                               '5) Delete user\n\t'
                               '6) Logout\n')

        if response_admin == '1':
            # first_name, last_name, group, student_ticket
            # Add new student
            first_name = input('Please enter first name\n')
            last_name = input('Please enter last name\n')

            groups = admin.get_all_group
            print('Group list:')
            for group_to in groups:
                print(f'\t{group_to[0]}) {group_to[1]}')
            group = input('Enter number correct group\n')

            student_ticket = input('Enter numbers student ticket, enter 9 numbers\n')

            admin.add_new_student(first_name, last_name, group, student_ticket)

        elif response_admin == '2':
            # Get all student
            all_student = admin.get_all_student

            print(f''.ljust(100, '-'))
            print(f'|ID|{"Ful name".ljust(30)}|{"Ticket".ljust(9)}|'
                  f'{"Group".ljust(7)}|{"Faculty".ljust(20)}|'
                  f'{"Evaluation".ljust(25)}|')
            print(f''.ljust(100, '-'))

            for student in all_student:
                print(f'|{str(student[0]).ljust(2)}|'
                      f'{(student[1] + " " + student[2]).ljust(30)}|{student[3]}|'
                      f'{student[4].ljust(7)}|{student[5].ljust(20)}|{str(student[6]).ljust(25)}|')

            print(f''.ljust(100, '-'))

        elif response_admin == '3':
            id_ = input('Enter id student\n')
            evaluation = input('Enter evaluation to student\n')
            admin.add_evaluation_to_student(evaluation, id_)

        elif response_admin == '4':
            id_ = input('Enter id student\n')

            first_name = input('Please enter first name\n')
            last_name = input('Please enter last name\n')

            groups = admin.get_all_group
            print('Group list:')
            for group_to in groups:
                print(f'\t{group_to[0]}) {group_to[1]}')
            group = input('Enter number correct group\n')

            admin.edit_student(id_, first_name, last_name, group)

        elif response_admin == '5':
            id_ = input('Enter id student\n')
            admin.delete_student(id_)

        elif response_admin == '6':
            break
        else:
            print('You need to make the right choice')


def student_logic(db):
    student_user = Student(db)
    while True:
        response_student = input('Ok, you are student, what do you want to do?\n\t'
                                 '1) Get excellent student\n\t'
                                 '2) Get all student\n\t'
                                 '3) Find student ticket\n\t'
                                 '4) Logout\n')
        if response_student == '1':
            # Get excellent student
            excellent_students = student_user.excellent_students

            print(f''.ljust(39, '-'))
            print(f'|{"Ful name".ljust(30)}|{"Ticket".ljust(9)}|')
            print(f''.ljust(39, '-'))

            for excellent in excellent_students:
                print(f'|{(excellent[1] + " " + excellent[2]).ljust(30)}|{excellent[3]}|')
            print(f''.ljust(39, '-'))

        elif response_student == '2':
            # Get all student
            all_student = student_user.get_all_student

            print(f''.ljust(97, '-'))
            print(f'|{"Ful name".ljust(30)}|{"Ticket".ljust(9)}|'
                  f'{"Group".ljust(7)}|{"Faculty".ljust(20)}|'
                  f'{"Evaluation".ljust(25)}|')
            print(f''.ljust(97, '-'))

            for student in all_student:
                print(f'|{(student[1] + " " + student[2]).ljust(30)}|{student[3]}|'
                      f'{student[4].ljust(7)}|{student[5].ljust(20)}|{str(student[6]).ljust(25)}|')

            print(f''.ljust(97, '-'))

        elif response_student == '3':
            # Find student ticket
            findet_ticket = input('Enter number ticket\n')
            find_student = student_user.find_student_ticket(findet_ticket)

            print(f''.ljust(97, '-'))
            print(f'|{"Ful name".ljust(30)}|{"Ticket".ljust(9)}|'
                  f'{"Group".ljust(7)}|{"Faculty".ljust(20)}|'
                  f'{"Evaluation".ljust(25)}|')
            print(f''.ljust(97, '-'))

            for student in find_student:
                print(f'|{(student[1] + " " + student[2]).ljust(30)}|{student[3]}|'
                      f'{student[4].ljust(7)}|{student[5].ljust(20)}|{str(student[6]).ljust(25)}|')

            print(f''.ljust(97, '-'))

        elif response_student == '4':
            break

        else:
            print('You need to make the right choice')


if __name__ == '__main__':
    with ContexSqlManager('students.sqlite') as db:
        while True:
            response = input('Who are you?\n\t1) Admin\n\t2) Student\n\t3) This is a mistake. Where is the solution?\n')
            if response == '1':
                # Admin
                admin_logic(db)

            elif response == '2':
                # Student
                student_logic(db)

            elif response == '3':
                break
            else:
                print('You need to make the right choice')

# 2	Andrey	Lutuyi	2	423487287

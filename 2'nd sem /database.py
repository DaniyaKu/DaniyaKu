import sqlite3


conn = sqlite3.connect('students.db')
cursor = conn.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS students 
                  (id INTEGER PRIMARY KEY, name TEXT, grade INTEGER)''')
conn.commit()

def add_student():
    name = input("Введите имя студента: ")
    grade = int(input("Введите оценку студента: "))
    cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", (name, grade))
    conn.commit()
    print("Студент успешно добавлен!")

def delete_student():
    student_id = int(input("Введите ID студента, которого нужно удалить: "))
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    print("Студент успешно удален!")

def edit_grade():
    student_id = int(input("Введите ID студента, оценку которого нужно изменить: "))
    new_grade = int(input("Введите новую оценку: "))
    cursor.execute("UPDATE students SET grade=? WHERE id=?", (new_grade, student_id))
    conn.commit()
    print("Оценка успешно изменена!")

while True:
    print("1. Добавить студента")
    print("2. Удалить студента")
    print("3. Изменить оценку студента")
    print("4. Вывести список всех студентов")
    print("5. Выйти из программы")
    choice = int(input("Выберите действие: "))
    if choice == 1:
        add_student()
    elif choice == 2:
        delete_student()
    elif choice == 3:
        edit_grade()
    elif choice == 4:
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        print("ID\tИмя\tОценка")
        for student in students:
            print(student[0], "\t", student[1], "\t", student[2])
    elif choice == 5:
        break
    else:
        print("Некорректный ввод! Попробуйте еще раз.")
        
# Закрывает соединение с базой данных
conn.close()

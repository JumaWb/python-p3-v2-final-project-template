from models.__init__ import CURSOR, CONN

class Student:
    all = {}

    def __init__(self, name, age, year):
        self._name = name
        self._age = age
        self._year = year
    def __repr__(self):
        f"name:{self.name} age: {self.age} year: {self.year}"
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Student name is not valid!")
    
    def get_age(self):
        return self._age
    
    def set_age(self, age):
        if isinstance(age, int) and age > 0:
            self._age = age
        else:
            raise ValueError("Student age is not valid!")
    
    def get_year(self):
        return self._year
    
    def set_year(self, year):
        if isinstance(year, int) and year > 2000:
            self._year = year
        else:
            raise ValueError("Student year is not valid!")

    name = property(get_name, set_name)
    age = property(get_age, set_age)
    year = property(get_year, set_year)

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            year INTEGER)
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        sql = """
            INSERT INTO students (name, age, year)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.age, self.year))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, age, year):
        student = cls(name, age, year)
        student.save()
        return student

    def update(self):
        sql = """
            UPDATE students
            SET name = ?, age = ?, year = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.age, self.year, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM students
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        student = cls.all.get(row[0])
        if student:
            student.name = row[1]
            student.age = row[2]
            student.year = row[3]
        else:
            student = cls(row[1], row[2], row[3])
            student.id = row[0]
            cls.all[student.id] = student
        return student

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM students
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM students
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM students
            WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    @classmethod
    def view_students(cls):
        sql = """
            SELECT students.id, students.name, students.age, students.year, courses.course_title, courses.course_duration
            FROM enrollments
            JOIN students ON enrollments.student_id = students.id
            JOIN courses ON enrollments.course_id = courses.id
        """
        rows = CURSOR.execute(sql).fetchall()
        students = []
        if rows:
            for row in rows:
                student_info = {
                    'student_id': row[0],
                    'name': row[1],
                    'age': row[2],
                    'year': row[3],
                    'course_title': row[4],
                    'course_duration': row[5]
                }
                students.append(student_info)
        return students
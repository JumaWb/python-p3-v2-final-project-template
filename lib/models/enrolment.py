from models.__init__ import CURSOR, CONN
from models.Student import Student
from models.course import Course

class Enrollment:
    def __init__(self, student_id, course_id):
        self._student_id = student_id
        self._course_id = course_id

    def get_student_id(self):
        return self._student_id

    def set_student_id(self, student_id):
        if isinstance(student_id, int) and Student.find_by_id(student_id):
            self._student_id = student_id
        else:
            raise ValueError("Student ID is not valid or does not exist!")

    def get_course_id(self):
        return self._course_id

    def set_course_id(self, course_id):
        if isinstance(course_id, int) and Course.find_by_id(course_id):
            self._course_id = course_id
        else:
            raise ValueError("Course ID is not valid or does not exist!")

    student_id = property(get_student_id, set_student_id)
    course_id = property(get_course_id, set_course_id)

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS enrollments (
            id INTEGER PRIMARY KEY,
            student_id INTEGER,
            course_id INTEGER,
            FOREIGN KEY(student_id) REFERENCES students(id),
            FOREIGN KEY(course_id) REFERENCES courses(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO enrollments (student_id, course_id)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.student_id, self.course_id))
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, student_id, course_id):
        enrollment = cls(student_id, course_id)
        enrollment.save()
        return enrollment

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM enrollments
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls(*row[1:]) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM enrollments
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls(*row[1:]) if row else None

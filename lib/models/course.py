from models.__init__ import CURSOR, CONN



class Course:
    all = {}
    def __init__(self, course_title, course_duration):

        self._course_title = course_title  
        self._course_duration = course_duration  
    def __repr__(self):
        return f"course title: {self.course_title} course duration: {self.course_duration}"
    
    def get_course_title(self):
        return self._course_title  
    
    def set_course_title(self, course_title):
        if isinstance(course_title, str) and len(course_title) > 0:
            self._course_title = course_title  
        else:
            raise ValueError("Course title not valid!")
        
    def get_course_duration(self):
        return self._course_duration  
    
    def set_course_duration(self, course_duration):
        if isinstance(course_duration, int) and course_duration > 0:
            self._course_duration = course_duration 
        else:
            raise ValueError("Course duration not valid!")
    
    course_title = property(get_course_title, set_course_title)  
    course_duration = property(get_course_duration, set_course_duration)

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY,
            course_title TEXT,
            course_duration INTEGER)
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        sql = """
            INSERT INTO courses (course_title, course_duration)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self._course_title, self._course_duration))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, course_title, course_duration):
        course = cls(course_title, course_duration)
        course.save()
        return course

    def update(self):
        sql = """
            UPDATE courses
            SET course_title = ?, course_duration = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self._course_title, self._course_duration, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM courses
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        course = cls.all.get(row[0])
        if course:
            course._course_title = row[1]
            course._course_duration = row[2]
        else:
            course = cls(row[1], row[2])
            course.id = row[0]
            cls.all[course.id] = course
        return course

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM courses
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM courses
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_title(cls, course_title):
        sql = """
            SELECT *
            FROM courses
            WHERE course_title = ?
        """
        row = CURSOR.execute(sql, (course_title,)).fetchone()
        return cls.instance_from_db(row) if row else None

"""
@author: Janki patel
CWID : 10457365
"""


"""This file we will do  the University, Student and Instructor. """

"""This is importing some of the in-built functions"""




import os
from prettytable import PrettyTable
from collections import defaultdict
from typing import Iterator, Tuple, Dict, List, DefaultDict, IO
class University:
    """It will store student and instructor recorde"""

    def file_reader(self, path: str, fields: int, sep: str = ",", header: bool = False) -> Iterator[Tuple[str]]:
        """in this method we will do separat all the items in which we gave file in the file path"""
        try:
            file_open: IO = open(path, "r", encoding="utf=8")
            if not (file := file_open):
                raise FileNotFoundError
            """this will do when we open the file after that we will close that"""
            with file:
                for line_n, line in enumerate(file, 1):
                    r_line: List[str] = line.rstrip("\n").split(sep)
                    r_linecount: int = len(r_line)

                    if r_linecount != fields:
                        raise ValueError(
                            f"The file path is {path} have {r_linecount} on line {line_n} but expected {fields}")

                    if not header:
                        yield tuple(r_line)
                    elif line_n != 1:
                        yield tuple(r_line)
        except FileNotFoundError:
            print(f"path of {path} could not able to find it try it again!!!")

    def __init__(self, dir: str, d=True) -> None:
        """ this method will initialize directory and dictionary for students as well as instructor"""
        self._dir: str = dir
        self._students: Dict[str, Student] = dict()
        self._instructors: Dict[str, Instructor] = dict()
        stud: str = 'students.txt'
        inst: str = 'instructors.txt'
        grade: str = 'grades.txt'

        try:
            self._getstudent(os.path.join(dir, stud))
            self._getinstructor(os.path.join(dir, inst))
            self._getgrade(os.path.join(dir, grade))
        except (FileNotFoundError, ValueError) as err:
            print(err)
        else:
            if d:
                self.s_table()
                self.i_table()

    def _getstudent(self, path: str) -> None:
        """In this method we will get student details from the file store in to dictionary"""
        try:
            for cwid, name, major in self.file_reader(path, 3, sep='\t', header=False):
                self._students[cwid] = Student(cwid, name, major)
        except ValueError as ve:
            print(ve)

    def _getinstructor(self, path: str) -> None:
        """In this method we will get instructor details from the file store in to dictionary"""
        try:
            for cwid, name, dept in self.file_reader(path, 3, sep='\t', header=False):
                self._instructors[cwid] = Instructor(cwid, name, dept)
        except ValueError as ve:
            print(ve)

    def _getgrade(self, path: str) -> None:
        """In this method we will get student grade from the file store in to dictionary"""
        g_info: Iterator[Tuple[str]] = self.file_reader(
            path, 4, sep='\t', header=False)
        try:
            for stu_cwid, course, grade, inst_cwid in g_info:
                if stu_cwid in self._students:
                    self._students[stu_cwid].a_course(course, grade)
                else:
                    print(f'unknown student of their grade{stu_cwid}')

                if inst_cwid in self._instructors:
                    self._instructors[inst_cwid].add_s(course)
                else:
                    print(f'unknown instructor of their grade{inst_cwid}')
        except ValueError as ve:
            print(ve)

    def s_table(self) -> PrettyTable:
        """ Pretty table for students """
        pt_table: PrettyTable = PrettyTable(
            field_names=Student.prettytable_header)
        for s in self._students.values():
            pt_table.add_row(s.pt_table_row())
        return pt_table

    def i_table(self) -> PrettyTable:
        """ Pretty table for instructors """
        pt_table: PrettyTable = PrettyTable(
            field_names=Instructor.prettytable_header2)

        for instructor in self._instructors.values():
            for r in instructor.pt_table_row():
                pt_table.add_row(r)

        print(pt_table)


class Student:
    """ This is Student class """
    prettytable_header: list = ['CWID', 'Name', 'Completed Courses']

    def __init__(self, cwid, name, major) -> None:
        """ in that we will initialize student table details """
        self._cwid: int = cwid
        self._name: str = name
        self._major: str = major
        self._courses: Dict[str, str] = dict()

    def a_course(self, course, grade) -> None:
        """in that we will add courses with grades of student """
        self._courses[course] = grade

    def pt_table_row(self) -> None:
        """ in that we return a row for student's prettytable """
        return [self._cwid, self._name, sorted(self._courses.keys())]


class Instructor:
    """This is Instructor class """
    prettytable_header2 = ['CWID', 'Name', 'Dept', 'Course', 'Students']

    def __init__(self, cwid: int, name: str, dept: str) -> None:
        """ Initialize instructor table details """
        self._cwid: int = cwid
        self._name: str = name
        self._dept: str = dept
        self._courses_i: DefaultDict[str, int] = defaultdict(int)

    def add_s(self, course) -> None:
        """ This method we will counting number of students who took the course with this instructor """
        self._courses_i[course] = self._courses_i[course] + 1

    def pt_table_row(self) -> None:
        """ in that we yield the rows for instructor prettytable """
        for course, count in self._courses_i.items():
            yield [self._cwid, self._name, self._dept, course, count]

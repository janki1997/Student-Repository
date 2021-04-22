"""
@author: Janki patel
CWID : 10457365
"""


"""This file we will do  the University, Student, Mejor and Instructor. """

"""This is importing some of the in-built functions"""

# from HW_08 import file_reader




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

    """ Repository to store information of students and instructors """

    def __init__(self, dire: str, d: bool) -> None:
        """ this method will initialize directory and dictionary for students as well as instructor"""

        self._dir: str = dir
        self._students: Dict[str, Student] = dict()
        self._instructors: Dict[str, Instructor] = dict()
        self._majors: Dict[str, Major] = dict()
        stud: str = 'students.txt'
        inst: str = 'instructors.txt'
        grade: str = 'grades.txt'
        mejor: str = 'majors.txt'

        try:
            self._getmajor(os.path.join(dire, mejor))
            self._getstudent(os.path.join(dire, stud))
            self._getinstructor(os.path.join(dire, inst))
            self._getgrade(os.path.join(dire, grade))

        except (FileNotFoundError, ValueError) as err:
            print(err)
        else:
            if d:
                self.s_table()
                self.i_table()
                self.m_table()

    def _getstudent(self, path: str) -> None:
        """In this method we will get student details from the file store in to dictionary"""
        try:
            for cwid, name, major in self.file_reader(path, 3, sep=';', header=True):
                if major not in self._majors:
                    print(
                        f"Student {cwid} '{name}' has unknown major '{major}'")
                else:
                    self._students[cwid] = Student(
                        cwid, name, self._majors[major])
        except ValueError as ve:
            print(ve)

    def _getinstructor(self, path: str) -> None:
        """In this method we will get instructor  details from the file store in to dictionary"""
        try:
            for cwid, name, dept in self.file_reader(path, 3, sep='|', header=True):
                self._instructors[cwid] = Instructor(cwid, name, dept)
        except ValueError as ve:
            print(ve)

    def _getgrade(self, path: str) -> None:
        """In this method we will get student grade from the file store in to dictionary """
        g_info: Iterator[Tuple[str]] = self.file_reader(
            path, 4, sep='|', header=True)
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

    def _getmajor(self, path: str) -> None:
        """in this method we will get information from mejor file"""
        try:
            for major, flag, course in self.file_reader(path, 3, sep='\t', header=True):
                if major not in self._majors:
                    self._majors[major] = Major(major)
                self._majors[major].a_course(course, flag)
        except ValueError as ve:
            print(ve)

    def s_table(self) -> PrettyTable:
        """  Pretty table for students """
        pt_table: PrettyTable = PrettyTable(
            field_names=Student.prettytable_header)
        for s in self._students.values():
            pt_table.add_row(s.pt_table_row())
        return pt_table

    def i_table(self) -> PrettyTable:
        """  Pretty table for instructor table """
        pt_table: PrettyTable = PrettyTable(
            field_names=Instructor.prettytable_header)
        for Instructor in self._instructors.values():
            for row in Instructor.pt_table_row():
                pt_table.add_row(row)

        return pt_table

    def m_table(self) -> PrettyTable:
        """ Pretty table for major table """
        pt_table: PrettyTable = PrettyTable(
            field_names=Major.prettytable_header)
        for major in self._majors.values():
            pt_table.add_row(major.pt_table_row())
        return pt_table


class Student:
    """ This is Student class """
    prettytable_header: list = ['CWID', 'Name', 'major',
                                'Completed Courses', 'rem_required', 'rem_electives', 'gpa']

    def __init__(self, cwid: int, name: str, major: str) -> None:
        """ in that we will initialize student table details"""
        self._cwid: int = cwid
        self._name: str = name
        self._major: str = major
        self._courses: Dict[str, str] = defaultdict()

    def a_course(self, course, grade) -> None:
        """in that we will add courses with grades of student"""
        self._courses[course] = grade

    def gpa(self) -> None:
        """in that method we will calculate the GPA using dictionary"""
        grades: Dict[str, float] = {"A": 4.00, "A-": 3.75, "B+": 3.25, "B": 3.00, "B-": 2.75, "C+": 2.25, "C": 2.00, "C-": 0.00,
                                    "D+": 0.00, "D": 0.00, "D-": 0.00, "F": 0.00}
        try:
            amount: float = sum(
                [grades[grade] for grade in self._courses.values()]) / len(self._courses.values())
            return round(amount, 2)
        except ZeroDivisionError as z:
            print(z)

    def pt_table_row(self) -> None:
        """  in that we return a row for student's prettytable """
        major, passed, rem_required, rem_electives = self._major.remaining(
            self._courses)
        return [self._cwid, self._name, major, sorted(passed), sorted(rem_required), sorted(rem_electives), self.gpa()]


class Instructor:
    """This is Instructor class """
    prettytable_header = ['CWID', 'Name', 'Dept', 'Course', 'Students']

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



class Major:
    """ this is major class"""
    prettytable_header: list = ['Major', 'Require Cources', 'Elective']
    min_grades = {'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C'}

    def __init__(self, major: str) -> None:
        """ in that we will initialize mejor details """
        self._major: str = major
        self._Requirecourses: Set = set()
        self._Electivecourses: Set = set()

    def a_course(self, course: str, req: str) -> None:
        """in that method we will add course with grade """
        if req == 'R':
            self._Requirecourses.add(course)
        elif req == "E":
            self._Electivecourses.add(course)

        else:
            print(f'it will grade for unknolwn instructor')

    def remaining(self, completed: defaultdict()) -> None:
        """in this method we will adding remaining courses as well as electives"""
        success = {course for course, grade in completed.items()
                   if grade in Major.min_grades}
        rem_re = self._Requirecourses - success
        rem_ele = self._Electivecourses

        if self._Electivecourses.intersection(success):
            rem_ele = set()

        return self._major, success, rem_re, rem_ele

    def pt_table_row(self) -> None:
        """in that we yield the rows for Mejor prettytable """
        return [self._major, sorted(self._Requirecourses), sorted(self._Electivecourses)]

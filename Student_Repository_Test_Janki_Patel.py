"""
@author: Janki patel
CWID : 10457365
"""

""" this file contain testing the code which we already made the fuction in another file call here to test it"""
"""This is importing some of the in-built functions"""




import os
import unittest
from typing import Iterator, Tuple, Dict, List
from HW10_Janki_Patel import  University, Student, Instructor, Major
class TestRepository(unittest.TestCase):
    """in that we will setup Path """

    def setUp(self) -> None:
        self.test_path = "C:/Users/Janki/Desktop/Masterin/Sem-3/CS-810/HW_10"
        self.repo = University(self.test_path, False)

    def test_majors(self) -> None:
        """ Testcase for mejor"""
        ex = [['SFEN', ['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'], ['CS 501', 'CS 513', 'CS 545']],
              ['SYEN', ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810']]]

        calculated = [majors.pt_table_row()
                      for majors in self.repo._majors.values()]

        self.assertEqual(ex, calculated)

    def test_Student_attributes(self) -> None:
        """ Testcase for student"""
        ex = {'10103': ['10103', 'Baldwin, C', 'SFEN', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687'], ['SSW 540', 'SSW 555'], [], 3.44],
              '10115': ['10115', 'Wyatt, X', 'SFEN', ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687'], ['SSW 540', 'SSW 555'], [], 3.81],
              '10172': ['10172', 'Forbes, I', 'SFEN', ['SSW 555', 'SSW 567'], ['SSW 540', 'SSW 564'], ['CS 501', 'CS 513', 'CS 545'], 3.88],
              '10175': ['10175', 'Erickson, D', 'SFEN', ['SSW 564', 'SSW 567', 'SSW 687'], ['SSW 540', 'SSW 555'], ['CS 501', 'CS 513', 'CS 545'], 3.58],
              '10183': ['10183', 'Chapman, O', 'SFEN', ['SSW 689'], ['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'], ['CS 501', 'CS 513', 'CS 545'], 4.0],
              '11399': ['11399', 'Cordova, I', 'SYEN', ['SSW 540'], ['SYS 612', 'SYS 671', 'SYS 800'], [], 3.0],
              '11461': ['11461', 'Wright, U', 'SYEN', ['SYS 611', 'SYS 750', 'SYS 800'], ['SYS 612', 'SYS 671'], ['SSW 540', 'SSW 565', 'SSW 810'], 3.92],
              '11658': ['11658', 'Kelly, P', 'SYEN', [], ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810'], 0.0],
              '11714': ['11714', 'Morton, A', 'SYEN', ['SYS 611', 'SYS 645'], ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810'], 3.0],
              '11788': ['11788', 'Fuller, E', 'SYEN', ['SSW 540'], ['SYS 612', 'SYS 671', 'SYS 800'], [], 4.0]}

        calculated = {cwid: Student.pt_table_row()
                      for cwid, Student in self.repo._students.items()}

        self.assertEqual(ex, calculated)

    def test_Instructor_attributes(self) -> None:
        """Testcase for instrucor"""
        ex = {('98765', 'Einstein, A', 'SFEN', 'SSW 567', 4),
              ('98765', 'Einstein, A', 'SFEN', 'SSW 540', 3),
              ('98764', 'Feynman, R', 'SFEN', 'SSW 564', 3),
              ('98764', 'Feynman, R', 'SFEN', 'SSW 687', 3),
              ('98764', 'Feynman, R', 'SFEN', 'CS 501', 1),
              ('98764', 'Feynman, R', 'SFEN', 'CS 545', 1),
              ('98763', 'Newton, I', 'SFEN', 'SSW 555', 1),
              ('98763', 'Newton, I', 'SFEN', 'SSW 689', 1),
              ('98760', 'Darwin, C', 'SYEN', 'SYS 800', 1),
              ('98760', 'Darwin, C', 'SYEN', 'SYS 750', 1),

              ('98760', 'Darwin, C', 'SYEN', 'SYS 611', 2),
              ('98760', 'Darwin, C', 'SYEN', 'SYS 645', 1)}
        calculated = {tuple(detail) for Instructor in self.repo._instructors.values(
        ) for detail in Instructor.pt_table_row()}
        self.assertEqual(ex, calculated)


# it wil executed from here
if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)

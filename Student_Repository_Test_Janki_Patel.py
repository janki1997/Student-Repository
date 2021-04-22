"""
@author: Janki patel
CWID : 10457365
"""

""" this file contain testing the code which we already made the fuction in another file call here to test it"""
"""This is importing some of the in-built functions"""

import os
import unittest
from typing import Iterator, Tuple, Dict, List
from HW09_Janki_Patel import University, Student, Instructor
class TestRepository(unittest.TestCase):
    """in that we will setup Path """

    def test_Student_attributes(self) -> None:
        """Testcase for student"""
        self.repo = University(
            "C:/Users/Janki/Desktop/Masterin/Sem-3/CS-810/HW", False)
        calculated = {cwid: students.pt_table_row()
                      for cwid, students in self.repo._students.items()}
        ex = {'10103': ['10103', 'Baldwin, C', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687']],
              '10115': ['10115', 'Wyatt, X', ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687']],
              '10172': ['10172', 'Forbes, I', ['SSW 555', 'SSW 567']],
              '10175': ['10175', 'Erickson, D', ['SSW 564', 'SSW 567', 'SSW 687']],
              '10183': ['10183', 'Chapman, O', ['SSW 689']],
              '11399': ['11399', 'Cordova, I', ['SSW 540']],
              '11461': ['11461', 'Wright, U', ['SYS 611', 'SYS 750', 'SYS 800']],
              '11658': ['11658', 'Kelly, P', ['SSW 540']],
              '11714': ['11714', 'Morton, A', ['SYS 611', 'SYS 645']],
              '11788': ['11788', 'Fuller, E', ['SSW 540']]}

        self.assertEqual(ex, calculated)

    def test_Instructor_attributes(self) -> None:
        """Testcase for instructor"""
        self.repo = University(
            "C:/Users/Janki/Desktop/Masterin/Sem-3/CS-810/HW", False)
        calculated = {tuple(detail) for instructor in self.repo._instructors.values(
        ) for detail in instructor.pt_table_row()}

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
        self.assertEqual(ex, calculated)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)

"""
@author: Janki patel
CWID : 10457365
"""

""" this file contain testing the code which we already made the fuction in another file call here to test it"""
"""This is importing some of the in-built functions"""




import os
import unittest
from typing import Iterator, Tuple, Dict, List
from HW11_Janki_Patel import  University, Student, Instructor, Major
class TestRepository(unittest.TestCase):
    """in that we will setup Path """

    def setUp(self) -> None:
        """add database path and file path here"""
        self.test_path = "C:/Users/Janki/Desktop/Masterin/Sem-3/CS-810/HW_11/files"
        self.db_path = "C:/Users/Janki/Desktop/Masterin/Sem-3/CS-810/HW_11/Janki.db"
        self.repo = University(self.test_path,self.db_path,False)
    
    def test_majors(self) -> None:
        """ Testcase for major"""
        ex = [['SFEN', ['SSW 540', 'SSW 555', 'SSW 810'], ['CS 501', 'CS 546']], ['CS', ['CS 546', 'CS 570'], ['SSW 565', 'SSW 810']]]

        calculated = [majors.pt_table_row()
                      for majors in self.repo._majors.values()]

        self.assertEqual(ex, calculated)

    def test_Student_attributes(self) -> None:
        """ Testcase for student"""
        ex = {'10103': ['10103', 'Jobs, S', 'SFEN', ['CS 501', 'SSW 810'], ['SSW 540', 'SSW 555'], [], 3.38],
                   '10115': ['10115', 'Bezos, J', 'SFEN', ['SSW 810'], ['SSW 540', 'SSW 555'], ['CS 501', 'CS 546'], 2.0],
                   '10183': ['10183', 'Musk, E', 'SFEN', ['SSW 555', 'SSW 810'], ['SSW 540'], ['CS 501', 'CS 546'], 4.0],
                   '11714': ['11714', 'Gates, B', 'CS', ['CS 546', 'CS 570', 'SSW 810'], [], [], 3.5]}

        calculated = {cwid: Student.pt_table_row()
                      for cwid, Student in self.repo._students.items()}

        self.assertEqual(ex, calculated)

    def test_Instructor_attributes(self) -> None:
        """Testcase for instrucor"""
        ex = {('98762', 'Hawking, S', 'CS', 'CS 501', 1),
                   ('98764', 'Cohen, R', 'SFEN', 'CS 546', 1),
                   ('98763', 'Rowland, J', 'SFEN', 'SSW 555', 1),
                   ('98762', 'Hawking, S', 'CS', 'CS 546', 1),
                   ('98762', 'Hawking, S', 'CS', 'CS 570', 1),
                   ('98763', 'Rowland, J', 'SFEN', 'SSW 810', 4)}
        calculated = {tuple(detail) for Instructor in self.repo._instructors.values(
        ) for detail in Instructor.pt_table_row()}
        self.assertEqual(ex, calculated)

    def test_s_grades(self) -> None:
        
        """Testcase for grades"""
        ex = [('Bezos, J', '10115', 'SSW 810', 'A', 'Rowland, J'),
                    ('Bezos, J', '10115', 'CS 546', 'F', 'Hawking, S'), 
                    ('Gates, B', '11714', 'SSW 810', 'B-', 'Rowland, J'),
                    ('Gates, B', '11714', 'CS 546', 'A', 'Cohen, R'),
                    ('Gates, B', '11714', 'CS 570', 'A-', 'Hawking, S'),
                    ('Jobs, S', '10103', 'SSW 810', 'A-', 'Rowland, J'),
                    ('Jobs, S', '10103', 'CS 501', 'B', 'Hawking, S'),
                    ('Musk, E', '10183', 'SSW 555', 'A', 'Rowland, J'),
                    ('Musk, E', '10183', 'SSW 810', 'A', 'Rowland, J')]
        calculated = [studs for studs in self.repo._studentgrade_db(self.db_path)]
        self.assertEqual(ex, calculated)


# it wil executed from here
if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)



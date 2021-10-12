import unittest
from student_report import student_grade

class TestStudentReport(unittest.TestCase):
	def test_grade(self):
		testcase = "Reed", 80
		expected = "Reed received 80%  in th exam"
		self.assertEqual(student_grade(testcase), expected)

	def test_nograde_format(self):
		testcase = "Jain"
		expected = "No grade given"
		self.assertEqual(student_grade(testcase), expected)

	def test_noname_format(self):
		testcase = 78
		expected = "No name given"
		self.assertEqual(student_grade(testcase), expected)


unittest.main()
import unittest
import Syntax as student_processing


class TestStudentProcessing(unittest.TestCase):

    def test_create_student(self):
        student = student_processing.create_student()

        self.assertIsInstance(student, dict)
        self.assertIn("name", student)
        self.assertIn("age", student)
        self.assertIn("marks", student)

        self.assertIsInstance(student["name"], str)
        self.assertIsInstance(student["age"], int)
        self.assertIsInstance(student["marks"], list)
        self.assertEqual(len(student["marks"]), 5)


    def test_calculate_average(self):
        self.assertEqual(student_processing.calculate_average([50, 60, 70]), 60.0)
        self.assertEqual(student_processing.calculate_average([]), 0)
        self.assertAlmostEqual(
            student_processing.calculate_average([80, 90]),
            85.0
        )


    def test_get_grade(self):
        self.assertEqual(student_processing.get_grade(80), "Distinction")
        self.assertEqual(student_processing.get_grade(65), "Pass")
        self.assertEqual(student_processing.get_grade(55), "Supplementary")
        self.assertEqual(student_processing.get_grade(40), "Fail")


    def test_clean_numbers(self):
        values = ["10", 20, "30", "bad", 40.5]
        cleaned = student_processing.clean_numbers(values)

        self.assertEqual(cleaned, [10, 20, 30, 40])


    def test_even_numbers_only(self):
        numbers = [1, 2, 3, 4, 5, 6]
        result = student_processing.even_numbers_only(numbers)

        self.assertEqual(result, [2, 4, 6])


if __name__ == "__main__":
    unittest.main()

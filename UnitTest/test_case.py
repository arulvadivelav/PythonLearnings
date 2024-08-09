import unittest
import calculator

""" Command to run the python test cases 

    py -m unittest test_case.py

"""

""" Test cases for Function based """

# Unittest Skip 
@unittest.skip("Skipping this test case for a reason")
class FunctionTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(23,56), 79)
        self.assertEqual(calculator.sub(23,56), -33)
        self.assertEqual(calculator.mul(5,16), 80)
        self.assertEqual(calculator.div(36,2), 18)
    
    def test_sub(self):
        self.assertEqual(calculator.sub(56,23), 33)
        self.assertEqual(calculator.sub(23,56), -33)


""" Test cases for Class based """
class ClassTestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.calci = calculator.Calculator()
        
    def tearDown(self) -> None:
        print("This is tearDown function, executes after each test case")
    
    def test_add(self):
        self.assertEqual(self.calci.add(5, -5),10)

    # Skip for specific function
    @unittest.skipIf(True, "Skip the function because it's condition is Ture") 
    def test_sub(self):
        self.assertEqual(self.calci.sub(5, 5),0)

    def test_mul(self):
        self.assertEqual(self.calci.mul(5, 5),25)

    def test_div(self):
        self.assertEqual(self.calci.div(5, 5),1)

if __name__=="__main__":
    unittest.main()
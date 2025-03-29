import unittest
from database_methods import defineTables, PROJECT, SELECT, JOIN

class TestRelationalDatabase(unittest.TestCase):

    def setUp(self):
        self.dept, self.emp, self.emp2 = defineTables()

    def test_defineTables(self):
        print("Department Table:")
        self.dept.display()
        print("Employee Table 1:")
        self.emp.display()
        print("Employee Table 2:")
        self.emp2.display()
        
        self.assertEqual(len(self.dept.tuples()), 3)
        self.assertEqual(len(self.emp.tuples()), 3)
        self.assertEqual(len(self.emp2.tuples()), 2)

    def test_PROJECT(self):
        projected_dept = PROJECT(self.dept, ["DNO", "DNAME"])
        print("Projected Department Table:")
        projected_dept.display()
        
        self.assertEqual(len(projected_dept.tuples()), 3)
        for tup in projected_dept.tuples():
            self.assertIn("DNO", tup)
            self.assertIn("DNAME", tup)
            self.assertNotIn("BUDGET", tup)

    def test_SELECT(self):
        selected_emp = SELECT(self.emp, lambda tup: tup["SALARY"] == "40K")
        print("Selected Employee Table (SALARY == 40K):")
        selected_emp.display()
        
        self.assertEqual(len(selected_emp.tuples()), 1)
        self.assertEqual(selected_emp.tuples().__next__()["ENAME"], "Lopez")

    def test_JOIN(self):
        joined = JOIN(self.emp, self.emp2)
        print("Joined Employee Table:")
        joined.display()
        
        self.assertEqual(len(joined.tuples()), 2)  # E3 from emp and emp2 should join
        self.assertIn(("E3", "Finzi", "D2", "30K", "E3", "Finzi", "D2", "30K"), joined.tuples())

if __name__ == '__main__':
    unittest.main()
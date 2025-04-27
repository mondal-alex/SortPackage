import unittest

from main import sort

class TestSort(unittest.TestCase):
  def test_standard(self):
    self.assertEqual(sort(99.0, 99.0, 99.0, 10.0), "STANDARD")
    print("PASSED")

  def test_special_dim1(self):
    self.assertEqual(sort(150.0, 99.0, 99.0, 10.0), "SPECIAL")
    print("PASSED")

  def test_special_dim2(self):
    self.assertEqual(sort(99.0, 150.0, 99.0, 10.0), "SPECIAL")
    print("PASSED")

  def test_special_dim3(self):
    self.assertEqual(sort(99.0, 99.0, 150.0, 10.0), "SPECIAL")
    print("PASSED")

  def test_special_volume(self):
    self.assertEqual(sort(101.0, 101.0, 101.0, 10.0), "SPECIAL")
    print("PASSED")

  def test_special_heavy(self):
    self.assertEqual(sort(99.0, 99.0, 99.0, 20.0), "SPECIAL")
    print("PASSED")

  def test_rejected_dim1(self):
    self.assertEqual(sort(150.0, 99.0, 99.0, 20.0), "REJECTED")
    print("PASSED")

  def test_rejected_dim2(self):
    self.assertEqual(sort(99.0, 150.0, 99.0, 20.0), "REJECTED")
    print("PASSED")

  def test_rejected_dim3(self):
    self.assertEqual(sort(99.0, 99.0, 150.0, 20.0), "REJECTED")
    print("PASSED")

  def test_rejected_volume(self):
    self.assertEqual(sort(101.0, 101.0, 101.0, 20.0), "REJECTED")
    print("PASSED")

if __name__ == "__main__":
    unittest.main()


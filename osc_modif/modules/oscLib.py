Class oscGenerator:
  def copyTo(self):
    pass

Class bboxGenerator(oscGenerator):
  def copyTo(self):
    pass

Class polyGenerator(oscGenerator):
  def copyTo(self):
    pass

Class Test(unittest.TestCase):
  def test_bboxGenerator(self):
    bbox = bboxGenerator('001.osc').copyTo()

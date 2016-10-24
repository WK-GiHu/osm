Class oscGenerator:
  def __init__(self,fpath):
    self.fname = os.basename(fpath)
    self.source = fpath
    self.dest = ?


  def copyTo(self):
    pass

Class bboxGenerator(oscGenerator):
  def __init__(self,fpath,osm):
    oscGenerator.__init__(self,fpath) 
    self.osm = osm

  def copyTo(self,dest):
    saxOsmWriter(self.source).CopyTo(saxOsmBbox(dest+self.fname))
#end Class bboxGenerator 

Class polyGenerator(oscGenerator):
  def copyTo(self):
    pass

Class Test(unittest.TestCase):
  def test_bboxGenerator(self):
    bbox = bboxGenerator(self.source+'001.osc').copyTo(self.dest)
    assertTrue(hash_file(bbox.dest,'12345'))

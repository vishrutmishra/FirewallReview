class File:
  class Obj:
    def __init__(self, line, depth):
      self.depth = depth
      self.line = line
      self.Child = []

    def parse(self):
      print self.line

    def addChild(self, line):
      self.child.append(Obj(line))

  def __init__(self, file):
    self.file =  open(file, 'r')
    self.line = []

  def readLine(self):
    line = self.file.readline()
    depth = File.calcDepth(line)
    print depth
    self.line.append(self.Obj(line, depth))
    return self.line[-1]

  @staticmethod
  def calcDepth(line):
    depth = len(line) - len(line.lstrip())
    return depth

  # def parseLine():

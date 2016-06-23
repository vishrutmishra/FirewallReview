class File:
  class Line:
    def __init__(self, line):
      self.line = line
  def __init__(self, file):
    self.file =  open(file, 'r')
    self.line = Line

  def readLine(self):
    return self.file.readline()

  # def parseLine():

class File:
  class Line:
    def __init__(self, line):
      self.line = line
  def __init__(self, file):
    self.file =  open(file, 'r')
    self.line = []

  def readLine(self):
    self.line.append(self.file.readline())
    return self.line[-1]

  # def parseLine():

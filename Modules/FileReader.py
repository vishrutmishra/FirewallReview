from DS import Stack
class File:
  def __init__(self, file):
    self.file =  open(file, 'r')
    self.objList = []
    self.lastParentDepth = Stack()

  class Obj:
    def __init__(self, line, depth):
      self.depth = depth
      self.line = line
      self.child = []

    def parse(self):
      self.objList

    def addChild(self, obj):
      self.child.append(obj)
      return self.child[-1]

  def parseLine(self, line):
    depth = File.calcDepth(line)
    obj = self.Obj(line, depth)
    self.addObj(obj)

  def addObj(self, obj):
    if self.lastParentDepth.isEmpty():
      self.objList.append(obj)
      self.lastParentDepth.push(self.objList[-1])
    elif obj.depth > self.lastParentDepth.peek().depth:
      child = self.Obj(obj.line, obj.depth)
      chld = self.lastParentDepth.peek().addChild(child)
      self.lastParentDepth.push(chld)
    else:
      self.lastParentDepth.pop()
      self.addObj(obj)

  def read(self):
    line = self.file.readline().rstrip()
    while line:
      self.parseLine(line)
      line = self.file.readline().rstrip()
    return self.objList

  def printAll(self):
    self.printObj(self.objList)

  def printObj(self, objList):
    for obj in objList:
      print obj.line
      self.printObj(obj.child)
    print

  @staticmethod
  def calcDepth(line):
    depth = len(line) - len(line.lstrip())
    return depth
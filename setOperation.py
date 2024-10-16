setA={1,2,3,4,5,6,7}
setB={5,6,7,8,9}
def setOperation():
   union=setA.union(setB)
   print(union)
   intersection=setA.intersection(setB)
   print(intersection)
   difference=setB.difference(setA)
   print(difference)
setOperation()

from z3 import *

s = Solver()
# Working on 5 elements
SIZE = 5

# a is the original arary, sortedA will be the sorted version of it
a       = IntVector('A', SIZE)
sortedA = IntVector('S', SIZE)

# Assert that sortedA is indeed sorted
for i in range(SIZE-1):
    s.add(sortedA[i] <= sortedA[i+1])

# convert them to bags:
bagA = K(IntSort(), 0)
bagS = K(IntSort(), 0)
for i in range(SIZE):
    bagA = Store(bagA, a[i],       1 + Select(bagA, a[i]))
    bagS = Store(bagS, sortedA[i], 1 + Select(bagS, sortedA[i]))

# assert that the bags are the same
s.add(bagA == bagS)

# set the elements in the unsorted array
s.add(a[0] == 9984) 
s.add(a[1] == 4) 
s.add(a[2] == -5) 
s.add(a[3] == 75)    
s.add(a[4] == -9)    

# get and print the model
r = s.check()
if r == sat:
    m = s.model()
    finalA = []
    finalS = []
    for i in range(SIZE):
        finalA.append(m.evaluate(a[i],       model_completion=True))
        finalS.append(m.evaluate(sortedA[i], model_completion=True))
    print("A = %s" % finalA)
    print("S = %s" % finalS)
else:
    print("Solver said: %s" % r)
class Difference:
    def __init__(self, a):
        self.__elements = a
    
    def computeDifference(self):
        sort_elements = sorted(self.__elements)
        self.maximumDifference = abs(sort_elements[-1]-sort_elements[0])
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)

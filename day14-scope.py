class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

	# Add your code here
    #[3,4,1]
    def computeDifference(self):
        l = len(self.__elements)
        i=0
        j=0
        k=0
        suma=0
        temp=0
        #print(self.__elements[0]-self.__elements[1])
        #print(self.__elements[0]-self.__elements[2])
        #print(self.__elements[1]-self.__elements[2])
        for i in range(len(self.__elements)):
            for j in range(i + 1, len(self.__elements)):
                #print(self.__elements[i], self.__elements[j])
                #suma = abs(self.__elements[i] - self.__elements[j])
                if suma < abs(self.__elements[i] - self.__elements[j]):
                    #print(self.__elements[i], self.__elements[j])
                    suma=abs(self.__elements[i] - self.__elements[j])
            
        self.maximumDifference=suma
        #print(suma)
        return self.maximumDifference

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
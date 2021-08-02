import math
class point:
    coordinates=[]
    def __init__(self,coordinates=None):
        self.coordinates=coordinates

    def set_point(self,coordinates):
        self.coordinates=coordinates

    def dimentions(self):
        return len(self.coordinates)

    def get_dimention(self,dim):
            return self.coordinates[dim]

    def distance(self,point):
        sum=0
        if(point.dimentions()==self.dimentions()):
            for i in range(self.dimentions()):
                sum+=(self.coordinates[i]-point.coordinates[i])**2
            return math.sqrt(sum)
        else:
            raise ValueError('ERROR:data points with different dimentions')

    def print_point(self):
        for i in range(self.dimentions()):
            print(" p"+str(i)+":"+str(self.coordinates[i]),end='')
        print("")



    
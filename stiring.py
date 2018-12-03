import math
import numpy as np

class stiring_sets:
    def __init__(self,sets=[]):
        self.sets=sets
        self.min_number=[]
        self.index=-1
        for i in range(0,len(self.sets)):
            self.min_number.append(min(self.sets[i]))

    def find_element_set(self,element):
        for i in range(0,len(self.sets)):
            for ele in self.sets[i]:
                if(ele==element):
                    return i
        return -1

    def get_sort_index(self,index):
        min_number=np.array(self.min_number)
        sort_index=np.argsort(min_number)
        for i in range(0,len(sort_index)):
            if(sort_index[i]==index):
                return i
        return -1

    def add_new_set(self,value):
        self.min_number.append(min(value))
        self.sets.append(value)

    def add_to_set(self,value,a):
        min_number=np.array(self.min_number)
        index=np.argsort(min_number)
        self.sets[index[a]].append(value)

    def get_set_length(self):
        return len(self.sets)

    def set_index(self,index):
        self.index=index

    def __str__(self):
        min_number=np.array(self.min_number)
        sort_index=np.argsort(min_number)
        string="index "+str(self.index)+": "
        for ind in sort_index:
            set=self.sets[ind]
            sort_set=np.sort(np.array(set))
            string+="{"
            for element in sort_set:
                string+=str(element)
                string+=","
            string=string[:-1]
            string+="}; "
        return string


def stiring_number(n,k):
    if(n<k or k==0 or n==0):
        return int(0)
    if(n==k):
        return int(1)
    S=0
    for i in range(k,-1,-1):
        current=math.pow(k-i,n)/math.factorial(i)/math.factorial(k-i)
        if(i%2==0):
            S+=current
        else:
            S-=current
    e=1e-4
    return int(S+e)


def index_to_stiring(n,m,index):

    if(index>=stiring_number(n,m)):
        return None

    if(n>=1 and m==1):
        sets=[]
        sets.append([])
        for i in range(1,n+1):
            sets[0].append(i)
        result=stiring_sets(sets=sets)
        return result

    s=stiring_number(n-1,m-1)
    if(index<s):
        result=index_to_stiring(n-1,m-1,index)
        result.add_new_set([n])
        return result
    else:
        s2=stiring_number(n-1,m)
        a=(index-s)//s2
        b=(index-s)%s2
        result=index_to_stiring(n-1,m,b)
        result.add_to_set(n,a)
        return result

def stiring_to_index(n,m,sets):
    c_set=stiring_sets(sets=[])
    index=0
    for number in range(1,n+1):
        if(c_set.find_element_set(number)==-1):
            set_index=sets.find_element_set(number)
            c_set.add_new_set(sets.sets[set_index])
        else:
            b=index
            s=stiring_number(number-1,c_set.get_set_length())
            a=c_set.find_element_set(number)
            a=c_set.get_sort_index(a)
            index=a*s+b
            index+=stiring_number(number-1,c_set.get_set_length()-1)
    return index

if __name__ == '__main__':
    m=5
    n=7
    total=stiring_number(n,m)
    print(total)
    for i in range(0,total):
        result=index_to_stiring(n,m,i)
        result.set_index(i)
        print(result)
        c_i=stiring_to_index(n,m,result)
        if(c_i!=i):
            print("error in detect (%d,%d)"%(i,c_i))

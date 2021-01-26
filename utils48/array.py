class array:
    def __init__(self,*args,listOfLists=False):
        if len(args)==0:
            self.data = None
        elif len(args)==1 and listOfLists:
            self.data = args[0]
        else:self.data= list(args)
        self.___update___()
    def ___update___(self):
        self.getsize()
        self.rows = self.data
        self.cols = []
        for i in range(len(self.data[0])):
            self.cols+=[[]]
        for i in self.data:
            for j in range(len(self.cols)):
                self.cols[j]+=[i[j]]
    def getsize(self):
        y=len(self.data)
        x=len(self.data[0])
        for i in self.data:
            if len(i)!=x:
                raise ValueError("not a square array, fill gaps with None...")
        return (x,y)
    def __add__(self,other):
        if type(other)==list:
            if type(other[0])== list:
                return self + array(other,listOfLists=True)
        elif type(other)==type(self):
            if self.getsize()[0]==other.getsize()[0]:
                return array(self.data + other.data,listOfLists=True)
            else:raise ValueError("arrays' X axis not the same size.\n did you mean to merge ALONG the Y axis? use - not + ")
    def __sub__(self,other):
        if type(other)==list:
            if type(other[0])== list:
                return self - array(other,listOfLists=True)
        elif type(other)==type(self):
            if self.getsize()[1]==other.getsize()[1]:
                result = []
                for i in range(len(self.data)):
                    result.append(self.data[i]+other.data[i])
                return array(result,listOfLists=True)
            else:raise ValueError("arrays' Y axis not the same size.\n did you mean to merge ALONG the X axis? use + not - ")
    def __getitem__(self,key):
            return self.data[key.stop][key.start]#get xy coords
    def __iadd__(self,other):
        self.data = (self+other).data
        self.___update___()
    def __isub__(self,other):
        self.data = (self-other).data
        self.___update___()

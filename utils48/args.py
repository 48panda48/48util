import sys
args = sys.argv
class ArgRetriever:
    def __init__(self):
        self.args=args[1:]
        self.positional=[]
        self.keyword=[]
        self.boolean=[]
    def add_arg(self,name,argtype="positional"):
        if argtype!= "positional" and argtype!="keyword" and argtype!="boolean":
            raise ValueError(f"argtype {argtype} is invalid. Use 'positional', 'keyword' or'boolean' instead.")
        exec(f"self.{argtype}.append(name)",{"self":self,"name":name,"argtype":argtype})
    def parse_args(self):
        returning={}
        for i in self.keyword:
            returning[i]=None
        for i in self.keyword:
            nextone=False
            k=-1
            for j in self.args:
                if nextone:
                    self.args.pop(k)
                    self.args.pop(k)
                    returning[i]=j
                    nextone=False
                if "-"+i == j:
                    nextone=True
                k+=1
        print(self.args)
        for i in self.boolean:
            if "--"+i in self.args:
                returning[i]=True
                self.args.remove("--"+i)
            else:returning[i]=False
        if len(self.args) <= len(self.positional):
            for i in self.positional:
                returning[i]=None
            for a,p in zip(self.args,self.positional[:len(self.args)]):
                returning[p]=a
            returning["other"]=None
        else:
            for a,p in zip(self.args[:len(self.positional)],self.positional):
                returning[p]=a
            returning["other"]=self.args[len(self.positional):]
        return returning
a=ArgRetriever()
a.add_arg("test1","boolean")
a.add_arg("test3","positional")
a.add_arg("test2","keyword")
print(a.parse_args())

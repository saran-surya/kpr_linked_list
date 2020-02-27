"""
class node:
    def __init__(self,data):
        self.data=data
        self.left=None 
        self.right=None 
class tree(node):
    def __init__(self):
        self.root = None 
    def insert(self,data):
        if(self.root == None):
            self.root=node(data)
        else:
            self._insert(data,self.root)

    def _insert(self,data,c_node):
        if(c_node.left == None):
            c_node.left=node(data)
        elif(c_node.right == None):
            c_node.right=node(data)
        else:
            self._insert(data,c_node.left)


        

a=tree()
a.insert(1)
a.insert(2)
a.insert(3)
a.insert(4)
"""
a=int(input())
b=list(map(int,input().split()))
i=0
j=1
l1=[]
while(i<len(b)):
    tem=b[i:j]
    l1.append(abs(sum(tem)))
    if(j==len(b)):
        i+=1
        j=i+1
    else:
        j+=1
print(max(l1))
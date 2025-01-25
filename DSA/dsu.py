# Disjoint union set provides to main function in O(1) time
# union(a,b) - unions a and b
# find(a) - returns the parent of a

# A common implmentation is to use a tree data structure
# We need to ensure that the height of the tree is as low as possible
# We can do this by using path compression


class DisjointSet:
    def __init__(self,size):
        self.parent = list(range(size))
        self.size=[1]*size

    def find(self, x):
        while self.parent[x]!=x:
            self.parent[x] = self.parent[self.parent[x]]
            x=self.parent[x]
        return x

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.size[x] > self.size[y]:
            self.parent[y] = x
            self.size[x]+=self.size[y]
        else:
            self.parent[x] = y
            self.size[y]+=self.size[x]
        return

    def connected(self, x, y):
        return self.find(x) == self.find(y) 
    
    def __repr__(self):
        return f'{self.parent}\n{self.size}\n'

if __name__ =='__main__':
    ds = DisjointSet(5)
    ds.union(1,2)
    ds.union(2,3)
    print(ds.connected(1,3))
    print(ds.connected(1,4))
    print(ds)
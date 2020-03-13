from tkinter import *
import queue as Q
from functools import partial 
import time #importing time module to delay the animation by 0.05 seconds
global canvas
global wall
class Block:
    def __init__(self,i,j,size):
        self.x=i
        self.y=j
        self.flag=True #to know the present state 
        self.block=False
    def add_block(self,event):
        if self.flag==True:
            canvas[self.x][self.y].configure(bg="black")
            self.flag=False
            self.block=True
        else:
            canvas[self.x][self.y].configure(bg="white")
            self.flag=True
            self.block=False
def clear(wall,size):
    for i in range(size):
        for j in range(size):
            canvas[i][j].configure(bg="white")
            wall[i][j].flag=True
            wall[i][j].block=False
def set_source_dest(a,b,c,d):
    [x,y]=get_source(a,b)
    [u,v]=get_dest(c,d)
    canvas[x][y].configure(bg="green")
    canvas[u][v].configure(bg="red")
def get_source(a,b):
    x=a.get()
    y=b.get()
    return [int(x),int(y)]
def get_dest(c,d):
    x=c.get()
    y=d.get()
    return [int(x),int(y)]
def Set(a,b,c,d,wall,size):
    [x,y]=get_source(a,b)
    [u,v]=get_dest(c,d)
    clear(wall,size)
    canvas[x][y].configure(bg="green")
    canvas[u][v].configure(bg="red")
def valid(x,y,n):
    if x>=0 and y>=0 and x<n and y<n:
        return True
    else:
        return False
def DFS_until(x,y,u,v,size,visited,p,wall,flag):
    if visited[x][y]==True:
        return None
    else:
        if visited[x][y]!=True and visited[u][v]!=True:
            canvas[x][y].configure(bg="blue")
            canvas[x][y].update()
        visited[x][y]=True
        time.sleep(0.05)
        if valid(x+1,y,size)==True and visited[x+1][y]!=True and wall[x+1][y].block!=True:
            if visited[u][v]==True:
                return True
            p[x+1][y]=[x,y]
            flag=DFS_until(x+1,y,u,v,size,visited,p,wall,flag)
        if valid(x,y+1,size)==True and visited[x][y+1]!=True and wall[x][y+1].block!=True:
            if visited[u][v]==True:
                return True
            p[x][y+1]=[x,y]
            flag=DFS_until(x,y+1,u,v,size,visited,p,wall,flag)
        if valid(x,y-1,size)==True and visited[x][y-1]!=True and wall[x][y-1].block!=True:
            if visited[u][v]==True:
                return True
            p[x][y-1]=[x,y]
            flag=DFS_until(x,y-1,u,v,size,visited,p,wall,flag)
        if valid(x-1,y,size)==True and visited[x-1][y]!=True and wall[x-1][y].block!=True:
            if visited[u][v]==True:
                return True
            p[x-1][y]=[x,y]
            flag=DFS_until(x-1,y,u,v,size,visited,p,wall,flag)
        return True
def DFS(a,b,c,d,size,wall):
    [x,y]=get_source(a,b)
    [u,v]=get_dest(c,d)
    canvas[x][y].configure(bg="green")
    canvas[u][v].configure(bg="red")
    visited=list()#visited array to keep track of visited nodes
    p=list()#to keep track of prev node visited
    for i in range(size):
        visited.append([])
        p.append([])
    for i in range(size):
        for j in range(size):
            visited[i].append(False)
            p[i].append([-1,-1])
    flag=True
    f=DFS_until(x,y,u,v,size,visited,p,wall,flag)
    if f==True or f==None:
        while p[u][v]!=[-1,-1]:
            canvas[u][v].configure(bg="yellow")
            canvas[u][v].update()
            [A,B]=p[u][v]
            u=A
            v=B
            time.sleep(0.05)
    else:
        print("source is not found")
    set_source_dest(a,b,c,d)
def BFS(a,b,c,d,size,wall):
    [x,y]=get_source(a,b)
    A=[x,y]
    [u,v]=get_dest(c,d)
    canvas[x][y].configure(bg="green")
    canvas[u][v].configure(bg="red")
    visited=list()#visited array to keep track of visited nodes
    p=list()#to keep track of parent nodes
    d=list()#to keep track of distance from souce node
    for i in range(size):
        visited.append([])
        p.append([])
        d.append([])
    for i in range(size):
        for j in range(size):
            visited[i].append(False)
            p[i].append([-1,-1])
            d[i].append(500)
    q=Q.Queue()
    q.push([x,y])
    d[x][y]=0
    visited[x][y]=True
    while q.isempty!=True:
        temp=q.front()
        x=temp[0]
        y=temp[1]
        if x==u and y==v:
            break
        if x!=A[0] or  y!=A[1]:
            canvas[x][y].configure(bg="blue")
        canvas[x][y].update()
        if valid(x+1,y,size):
            if visited[x+1][y]==False and wall[x+1][y].block!=True:
                if d[x+1][y]>d[x][y]+1:
                    d[x+1][y]=d[x][y]+1
                    p[x+1][y]=[x,y]
                    #canvas[x+1][y].configure(bg="blue")
                    #canvas[x+1][y].update()
                    q.push([x+1,y])
                visited[x+1][y]=True
        if valid(x,y-1,size):
            if visited[x][y-1]==False and wall[x][y-1].block!=True:
                if d[x][y-1]>d[x][y]+1:
                    d[x][y-1]=d[x][y]+1
                    p[x][y-1]=[x,y]
                    #canvas[x][y-1].configure(bg="blue")
                    #canvas[x][y-1].update()
                    q.push([x,y-1])
                visited[x][y-1]=True
        if valid(x-1,y,size):
            if visited[x-1][y]==False and wall[x-1][y].block!=True:
                if d[x-1][y]>d[x][y]+1:
                    d[x-1][y]=d[x][y]+1
                    p[x-1][y]=[x,y]
                    #canvas[x-1][y].configure(bg="blue")
                    #canvas[x-1][y].update()
                    q.push([x-1,y])
                visited[x-1][y]=True
        if valid(x,y+1,size):
            if visited[x][y+1]==False and wall[x][y+1].block!=True:
                if d[x][y+1]>d[x][y]+1:
                    d[x][y+1]=d[x][y]+1
                    p[x][y+1]=[x,y]
                    #canvas[x][y+1].configure(bg="blue")
                    #canvas[x][y+1].update()
                    q.push([x,y+1])
                visited[x][y+1]=True
        q.pop()
        time.sleep(0.02)
    front=p[u][v]
    canvas[u][v].configure(bg="yellow")
    while front!=[-1,-1]:
        x=front[0]
        y=front[1]
        canvas[x][y].configure(bg="yellow")
        canvas[x][y].update()
        print(x," ",y)
        front=p[x][y]
        time.sleep(0.02)
    canvas[u][v].configure(bg="red")
    canvas[A[0]][A[1]].configure(bg="green")
root=Tk()
canvas=[]
wall=[]
root.configure(background="black")
a=IntVar()
b=IntVar()
c=IntVar()
d=IntVar()
Label(root,text="source cooridnates",background="white").grid(row=0,column=0,padx=10,pady=10)
Label(root,text="destination cooridnates",background="white").grid(row=1,column=0,padx=10,pady=10)
#x1 y1 represent source corodinates and x2 and y2 represent destination coordinates
Entry(root,textvariable=a).grid(row=0,column=1,padx=10,pady=10)
Entry(root,textvariable=b).grid(row=0,column=2,padx=10,pady=10)
Entry(root,textvariable=c).grid(row=1,column=1,padx=10,pady=10)
Entry(root,textvariable=d).grid(row=1,column=2,padx=10,pady=10)
size=20
for i in range(size):
    canvas.append([])
    wall.append([])
for i in range(size):
    for j in range(size):
        canvas[i].append(0)
        wall[i].append(0)
for i in range(size):
    for j in range(size):
        wall[i][j]=Block(i,j,size)
for i in range(size):
    for j in range(size):
        w=wall[i][j]
        canvas[i][j]=Canvas(root,background="white",width=25,height=25)
        canvas[i][j].grid(row=j+3,column=i+3,padx=1,pady=1)
        canvas[i][j].bind("<Button-1>",w.add_block)
bfs=partial(BFS,a,b,c,d,size,wall)
dfs=partial(DFS,a,b,c,d,size,wall)
SET=partial(Set,a,b,c,d,wall,size)
Clear=partial(clear,wall,size)
Button(root,text="SET",command=SET,width=10,height=1).grid(row=3,column=0,padx=1,pady=1)
Button(root,text="BFS",command=bfs,width=10,height=1).grid(row=4,column=0,padx=1,pady=1)
Button(root,text="DFS",command=dfs,width=10,height=1).grid(row=5,column=0,padx=1,pady=1)
Button(root,text="Clear",command=Clear,width=10,height=1).grid(row=6,column=0,padx=1,pady=1)       
root.mainloop()
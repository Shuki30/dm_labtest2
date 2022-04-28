import collections as cc
from itertools import combinations

def innerJoin(temp):
    freq = cc.defaultdict(int)
    for i in range(len(temp)):
        for j in range(i+1,len(temp)):
            if list(list(temp.keys())[i][:len(list(temp.keys())[i])-1:]) == list(list(temp.keys())[j][:len(list(temp.keys())[j])-1:]):
                dummy = list(list(temp.keys())[i])
                dummy.append(list(temp.keys())[j][-1])
                freq[tuple(dummy)] = 0
    return freq

def itemSet(temp):  
    freq = cc.defaultdict(int)      
    for i in temp:
        for j in dic:
            if set(i).issubset(set(dic[j])):
                freq[i] += 1
    return freq
        
def checkSigma(freq):
    temp = cc.defaultdict(int)
    for i in sorted(freq):
        if freq[i] >= sigma:
            temp[i] = freq[i]
    return temp

dic = cc.defaultdict(list)
dic = {10:['A','C','D','E'], 20:['B','C','E'], 30:['A','B','C','E'], 40:['B','E']}
'''
file = open("C:\\Users\\jeswa\\Desktop\\dm.txt",'r')
lines = file.readlines()

for i in range(len(lines)):
    dic[i] = list(lines[i].rstrip('\n').split(';'))    
'''
sigma = 2

freq = cc.defaultdict(int)

ans = []

for i in dic:
    for j in dic[i]:
        freq[j] += 1
print("C 1")
for x in freq:
    print(x,"=",freq[x])
ans.append(checkSigma(freq))
print("L 1")    
for x in ans[-1]:
    print(x,"=",ans[-1][x]) 
freq = cc.defaultdict(int)
comb = combinations(ans[0].keys(), 2)
freq = itemSet(comb)
print("C 2")          
for x in freq:
    print(x,"=",freq[x])
ans.append(checkSigma(freq))
print("L 2")    
for x in ans[-1]:
    print(x,"=",ans[-1][x]) 

while(1):
    if len(ans[-1]) <= 1:
        break
    freq = cc.defaultdict(int)
    freq = innerJoin(ans[-1])
    
    freq = itemSet(sorted(freq))
    
    temp = checkSigma(freq)
    if len(temp) > 0:
        ans.append(temp)
    else:
        break
    print("C",len(ans))    
    for x in freq:
        print(x,"=",freq[x])
    print("L",len(ans))    
    for x in ans[-1]:
        print(x,"=",ans[-1][x]) 
con = []
for i in ans[-1]:
    conf = cc.defaultdict(float)
    for j in range(1,len(ans)):
        c = combinations(i, j)
        for k in c:
            if len(k) == 1:
                conf[''.join(k)] = round(ans[-1][i]/ans[j-1][''.join(k)]*100,2)
            else:
                conf[k] = round(ans[-1][i]/ans[j-1][k]*100,2)
    con.append(conf)
print("Confidence")
for i in range(len(ans[-1])):
    temp = list(list(ans[-1].keys())[i])
    print(temp)
    for j in con[i]:
        temp1 = list(j)
        dummy = []
        for k in temp:
            if k not in temp1:
                 dummy.append(k)
        print(list(j),"->",dummy,"=",con[i][j])

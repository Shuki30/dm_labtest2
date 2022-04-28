import collections as cc
from itertools import combinations

def innerJoin(temp):
    freq = cc.defaultdict(list)
    for i in range(len(temp)):
        for j in range(i+1,len(temp)):
            if list(list(temp.keys())[i][:len(list(temp.keys())[i])-1:]) == list(list(temp.keys())[j][:len(list(temp.keys())[j])-1:]):
                dummy = list(list(temp.keys())[i])
                dummy.append(list(temp.keys())[j][-1])
                freq[tuple(dummy)] = []
    return freq

def itemSet(temp):  
    freq = cc.defaultdict(list)      
    for i in temp:
        for j in dic:
            if set(i).issubset(set(dic[j])):
                freq[i].append(j)
    return freq
        
def checkSigma(freq):
    temp = cc.defaultdict(int)
    for i in sorted(freq):
        if len(freq[i]) >= sigma:
            temp[i] = freq[i]
    return temp

dic = cc.defaultdict(list)
dic = {100:['F','A','C','D','G','I','M','P'], 200:['A','B','C','F','L','M','O'], 300:['B','F','H','J','O','W'], 400:['B','C','K','S','P'], 500:['A','F','C','E','L','P','M','N']}

sigma = 3

freq = cc.defaultdict(list)

ans = []

for i in dic:
    for j in dic[i]:
        freq[j].append(i)
print("C 1")
for x in freq:
    print(x,"=",freq[x])
ans.append(checkSigma(freq))
print("L 1")    
for x in ans[-1]:
    print(x,"=",ans[-1][x])    
freq = cc.defaultdict(list)
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
    freq = cc.defaultdict(list)
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
                conf[''.join(k)] = len(ans[-1][i])/len(ans[j-1][''.join(k)])*100
            else:
                conf[k] = len(ans[-1][i])/len(ans[j-1][k])*100
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

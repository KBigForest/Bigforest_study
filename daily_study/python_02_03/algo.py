class Solution(object):
def longestCommonPrefix(self, strs):
"""
:type strs: List[str]
:rtype: str
"""
output = ""
y = ""
if len(strs)> 1:
    for i in range(0, len(strs)-1):
        if i == 0:
            output = strs[i]
        for u in output:
            if u in strs[i+1]:
                y += u
        output = y
        y = ''
    return output
else:
    return strs[0]
strs = ["cir","car"]
a = Solution()
a.longestCommonPrefix(strs)

class Solution(object):
def longestCommonPrefix(self, strs):
"""
:type strs: List[str]
:rtype: str
"""
output = ""
y = ""
if len(strs)> 1:
    for i in range(0, len(strs)-1):
        if i == 0:
            output = strs[i]
        for u in output:
            if u in strs[i+1]:
                y += u
                if 
        output = y
        y = ''
    return output
else:
    return strs[0]      


class Solution(object):
def longestCommonPrefix(self, strs):
"""
:type strs: List[str]
:rtype: str
"""
output = ""
y = ""
if len(strs) > 1:
    for i in range(0, len(strs)-1):
        if i == 0:
            output = strs[i]
        for u in output:
            if u in strs[i+1]:
                y += u
        output = y
        y = ''
    return output
else:
    return strs[0]     
strs = ["cir","car"]
a = Solution()
a.longestCommonPrefix(strs)










strs = ["flower","flow","flight", 'fla','asfa' 'flssa']
strs.sort()
strs
for i in range(0, len(strs)):
for j in range(len(strs[i])):
for z in range(0,len(strs[i])):
    print(strs[i][j:z+1])
    if strs[i][j:z+1] in strs[i]
strs = ["acar","racecar","car"]          

print(zip(*strs))
for i in zip(*strs):
print(i)



import numpy as np
x = []
if len(l1)>= len(l2):
    for i in range(0,len(l1)):
        x.append(10^i)
    x = np.array(x)        
    np.array(l1) + x
    np.array(l2) + y

elif len(l1)<len(l2)
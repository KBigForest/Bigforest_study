strs = ["flower","flow","flight"]
output = ''
for i in range(0, len(strs)):
    for j in str[i]:
        if j in str[i+1:]:
            output += j
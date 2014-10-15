import re

s = 'xxxSPAMxxxSPAMxxxSPAMSPAMxSPAMspamSPAM'
print(len(s))
print(s.find('SPAM'))
print(s.rfind('SPAM'))


#re method
for a in list(re.finditer('SPAM', s)):
	print(a.start(), a.end())

print()


#no import method
def allindices(string, sub, listindex=[], offset=0):
    i = string.find(sub, offset)
    while i >= 0:
        listindex.append(i)
        i = string.find(sub, i + 1)
    return listindex
    
print(allindices(s, 'SPAM'))

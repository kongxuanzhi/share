
# -*- coding: UTF-8 -*-
import re
import json
 
start = r'^\s{8}function\s(.*)?\('
end = r'^\s{8}\}'
# 将正则表达式编译成Pattern对象
startpattern = re.compile(start)
endpattern = re.compile(end)
# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
 
file = open('../static/jquery.fullpage.js', 'r')

fm = {}

i = 0
findFunction = False
for line in file:
    i = i + 1
    # print(i, line)
    # 使用Match获得分组信息
    # print(i, match.group())
    if not findFunction:
        fmarch = startpattern.match(line)
        if fmarch:
            functionName = fmarch.group(1) 
            fm[functionName] = [i]
            findFunction = True
    else:
        endmatch = endpattern.match(line)
        if endmatch:
            fm[functionName].append(i)
            findFunction = False
file.close()

for key in fm.keys():
    functionPattern = re.compile('(' + key + ')\s?\(')
    # print(functionPattern)
    row = 0
    file = open('../static/jquery.fullpage.js', 'r')
    fm[key].append(0)
    for line in file:
        row = row + 1
        line = line.lstrip()
        if not line.startswith(r'\s*?//'):
            useMatch = functionPattern.match(line)
            if useMatch:
                # print(key, row)

                for f in fm.keys():
                    if row > fm[f][0] and row < fm[f][1]:
                        fm[key][2] = fm[key][2] + 1
                        fm[key].append(f)
    file.close()
for key in fm.keys():
    print(fm[key][2], key)
# print(json.dumps(fm))
file_object = open('function-relationship.json', 'w')
file_object.write(json.dumps(fm))
file_object.close()

# 题目描述
# 开发一个简单错误记录功能小模块，能够记录出错的代码所在的文件名称和行号。
# 处理：
# 1、 记录最多8条错误记录，循环记录（或者说最后只输出最后出现的八条错误记录），对相同的错误记录（净文件名称和行号完全匹配）只记录一条，错误计数增加；
# 2、 超过16个字符的文件名称，只记录文件的最后有效16个字符；
# 3、 输入的文件可能带路径，记录文件名称不能带路径。

import sys

result = []
d = {}
while True:
    try:
        s = raw_input().split(' ')
        s1 = s[0].split('\\')[-1]
        if len(s1) > 16:
            s1 = s1[-16:]
        s1 = s1 + ' ' +  str(s[-1])

        if s1 not in d.keys():
            d[s1] = 1
            result.append(s1)
        else:
            d[s1] += 1
    except:
        break

for i in result[-8:]:
    sys.stdout.write(i+' '+str(d[i])+'\n')
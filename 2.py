def 输入():
    str = input()
    s = str.split()
    #print(s)
    if len(s)>0:
        if (s[0] == '整数') and (s[1] == '小杨年龄'):
            xiaoyang[s[1]] = None
        elif (s[0] == '整数') and (s[1] == '小杨零花钱'):
            xiaoyang[s[1]] = None
        return s
    else:
        return None
#将汉字数字转换为阿拉伯数字
def 转换1(s):
    if len(s) <= 2:
        s[1] = s[1]
    elif s[2] == '零':
        s[2] = 0
    elif s[2] == '一':
        s[2] = 1
    elif s[2] == '二':
        s[2] = 2
    elif s[2] == '三':
        s[2] = 3
    elif s[2] == '四':
        s[2] = 4
    elif s[2] == '五':
        s[2] = 5
    elif s[2] == '六':
        s[2] = 6
    elif s[2] == '七':
        s[2] = 7
    elif s[2] == '八':
        s[2] = 8
    elif s[2] == '九':
        s[2] = 9
    elif s[2] == '十':
        s[2] = 10
    elif s[3] == '零':
        s[3] = 0
    elif s[3] == '一':
        s[3] = 1
    elif s[3] == '二':
        s[3] = 2
    elif s[3] == '三':
        s[3] = 3
    elif s[3] == '四':
        s[3] = 4
    elif s[3] == '五':
        s[3] = 5
    elif s[3] == '六':
        s[3] = 6
    elif s[3] == '七':
        s[3] = 7
    elif s[3] == '八':
        s[3] = 8
    elif s[3] == '九':
        s[3] = 9
    elif s[3] == '十':
        s[3] = 10
    return s
#将阿拉伯数字转换为汉字数字

def 转换2(a):
    if xiaoyang[a] == 0:
        xiaoyang[a] = '零'
    elif xiaoyang[a] == 1:
        xiaoyang[a] = '一'
    elif xiaoyang[a] == 2:
        xiaoyang[a] = '二'
    elif xiaoyang[a] == 3:
        xiaoyang[a] = '三'
    elif xiaoyang[a] == 4:
        xiaoyang[a] = '四'
    elif xiaoyang[a] == 5:
        xiaoyang[a] = '五'
    elif xiaoyang[a] == 6:
        xiaoyang[a] = '六'
    elif xiaoyang[a] == 7:
        xiaoyang[a] = '七'
    elif xiaoyang[a] == 8:
        xiaoyang[a] = '八'
    elif xiaoyang[a] == 9:
        xiaoyang[a] = '九'
    elif xiaoyang[a] == 10:
        xiaoyang[a] = '十'
    return s

def 使用(s):
    #整数 小杨年龄 等于 八
    if (s[0]=='整数') and (s[2]=='等于'):
        xiaoyang[s[1]] = s[3]
    #小杨年龄 增加 一
    if s[0] == '小杨年龄':
        xiaoyang[s[0]] = xiaoyang[s[0]] + s[2]
    #如果 小杨年龄 大于 八 则 小杨零花钱 增加 一 否则 无
    if s[0] == '如果':
        if s[2] == '大于':
            if xiaoyang[s[1]] > s[3]:
                xiaoyang[s[5]] = xiaoyang[s[5]] + 1
                转换2(s[5])
                print(xiaoyang[s[5]])
            else:
                None
    #看看 小杨零花钱
    if s[0] == '看看':
        转换2(s[1])
        print(xiaoyang[s[1]])
if __name__ == '__main__':
    xiaoyang = {}
    while (1):
        s = 输入()
        if s != None:
            s = 转换1(s)
            使用(s)
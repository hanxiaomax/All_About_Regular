#coding:utf-8
import re

re_list = [#-----字符匹配------#
        "a....c", #匹配除\n之外任意
        "a.\..c", #转义
        "a[b-z][^c][0-9]",#匹配字符集内字符，^取反
        #-----数量词匹配------#
        "abc*vb*",#匹配前一个字符0-无穷次
        "abc+",#匹配前一个字符1-无穷次
        "ab?c?",#匹配前一个字符0-1次
        "ab{2}",#匹配前一个字符2次
        "ab{2,4}",#匹配前一个字符2-4次，可以省略下限或上限
        #-----边界匹配,不消耗带匹配字符串中字符------#
        "^abc", #匹配开头,必须是a开头
        "abc$",#匹配结尾,必须是c
        "\Aabc",
        "abc\Z"
        "a\b!bc",
        "a\Bbc",
        #-----逻辑，分组------#
        "abc|def",#或，左边优先，默认完整表达式可以用括号分割
        "a(av){2}(12|45)5",
        "(?P<id>abc){2}",#(?P<id>)分组
        "(\d)abc\1",#
        "(?P<id>\d)abc(?P=id)"
        ]

str_list=["ab%#1c","a1..c","aqw8","abccv","ab","ab","abb","abbb","cbc",
            "abd","abd","11c","a!bc","def","aavav455","abcabc","8abc8","1abc1"]

for i in xrange(0 , len(re_list)):
    m=re.search(re_list[i],str_list[i])
    if m is not None:
        print re_list[i]+"<---->"+str_list[i]+"\t"+m.group()
    else:
        print re_list[i]+"<---->"+str_list[i]+"\t"+"None"

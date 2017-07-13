#!/usr/bin/env python
# encoding=utf-8
import re

target = "\"http://link.zhihu.com/?target=https%3A//www.quora.com/How-do-you-avoid-procrastination/answer/Oliver-Emberton\""
target2 = ""
if __name__ == '__main__':

    obj = target.replace(r'"http://link.zhihu.com/?target=https%3A//','').replace(r'"','')
    obj_link = r"http://"+obj
    print(obj)
    print(obj_link)

    matchObj = re.match(r'\"http://link.zhihu.com/\?target=https%3A//',target)

    print(matchObj)

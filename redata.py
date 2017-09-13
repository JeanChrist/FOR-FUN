# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 12:51:42 2017

@author: C
"""

from random import randrange, choice
from string import ascii_lowercase as lc
from sys import maxsize
from time import ctime

tlds = ('com', 'gov', 'edu', 'org', 'cn', 'net')

for i in range(randrange(5,11)):
    dtint = str(randrange(maxsize))[:9]
    dtstr = ctime(int(dtint))
    llen = randrange(4,8)
    login = ''.join(choice(lc) for j in range(llen))
    dlen = randrange(llen, 13)
    dom = ''.join(choice(lc) for j in range(dlen))
    print ('%s::%s@%s.%s::%d-%d-%d' % (dtstr, login,
                dom,choice(tlds), int(dtint), llen, dlen))
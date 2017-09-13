# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 18:53:08 2017

@author: C
"""

from time import ctime, sleep
import threading

loops = [4,2]

def loop(nloop, nsec):
    print ('start loop', nloop, 'at:', ctime())
    sleep(nsec)
    print ('loop', nloop, 'done at:', ctime())

def main():
    print ('starting at:', ctime())
    threads = []
    nloops = range(len(loops))
    
    for i in nloops:
        t = threading.Thread(target=loop,
                             args=(i, loops[i]))
        threads.append(t)
    for i in nloops:
        threads[i].start()
            
    for i in nloops:
        threads[i].join()
            
    print ('all Done at:', ctime())
                
if __name__ == '__main__':
    main()

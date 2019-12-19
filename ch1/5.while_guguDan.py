# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 09:48:40 2019

@author: shkim
"""

dan = 1
while(dan):
    dan = int(input('\ndan? '))
    if dan==0 : break
    if not(1<=dan<=9):
        print("dan input error!!")
        continue
    else:
        print('구구단(%d) 계산...' % dan)
        for i in range(1, 10):
            print('%d*%d = %d' %(dan,i,(dan*i)))

print("구구단 게임을 종료합니다.")


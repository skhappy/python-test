#!/usr/bin/env python
# coding=utf-8
import random
secret =random.randint(1,10)
print('----------孙凯----------')
temp = input('who am i \n')
guess = int(temp) 
while guess != secret:
    temp = input("错了\n")
    guess = int(temp)
    if guess == secret:
        	print("你牛")
	        print("猜中了也没奖励。")
    else:
        if guess >secret :
            print("大了\n")
        else:
            print("小了\n")

print("Game Over!")


# -*- coding: utf-8 -*-
import random
answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('please enter: '))
    if number < answer:
        print ("more")
    elif number > answer:
        print ("less")
    else:
        print ("well done")
        break
print('the totaly number you guess%d' % counter)
if counter > 7:
    print('sorry about your IQ')

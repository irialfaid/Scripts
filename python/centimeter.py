#!/usr/bin/env python

from __future__ import print_function

a = raw_input('cm for centimeters, inch for inches --> ')
if a == 'inch':

    inches = float(raw_input('Enter inches ammount--> '))
    cent = 2.54 * inches 
    print (inches, 'in equals', cent, 'cm')
elif a == 'cm':
    cent = float(raw_input('Enter centimeter ammount--> '))
    inches = cent * 0.3937008
    print (cent, 'cm equals', inches, 'inches')
else:
    print ('Invalid input.')


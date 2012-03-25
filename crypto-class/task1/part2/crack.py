#!/usr/bin/python

import sys

prand1 = 210205973L
prand2 = 22795300L
prand3 = 58776750L
P = 295075153L

def next(x,y):
  result =  ((2*x+5) % P)^((3*y+7) % P)
  return result, ((2*x+5) % P),((3*y+7) % P)


def main():
  found = False
  i = 192000000L
  while not found and i < P:
    changed_x = ((2*i+5)%P)
    changed_y = prand1 ^ changed_x
    result, new_x, new_y = next(changed_x, changed_y)
    if result == prand2:
      print "CANDIDATE!"
      result, new_x, new_y = next(new_x, new_y)
      if result == prand3:
        print "FOUND"
        found = True
      else:
        i+= 1
    else:
      i += 1
      if i % 100000 == 0:
        print i
  
  x = (2*i+5)%P
  y = prand1^x

  print "ANSWER:\nprand1 = %d" % (x^y)

  for i in range(2,11):
    result, new_x, new_y = next(x,y)
    print "prand%d = %d" % (i, result)
    x = new_x
    y = new_y


if __name__ == '__main__':
  main()

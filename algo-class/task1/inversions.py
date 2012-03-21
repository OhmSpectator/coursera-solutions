#!/usr/bin/python

import sys

def main():
  source = open( sys.argv[1], 'r' )
  numbers = []
  for number in source:
    numbers.append( number.replace('\n','') )
  print numbers

if __name__ == '__main__':
  main()

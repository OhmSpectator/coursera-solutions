#!/usr/bin/python

import sys

def load_numbers():
  result = []
  source = open(sys.argv[2], 'r')
  for number in source:
    result.append(int(number.replace('\n','')))
  return result


def choose_pivot(numbers):
  if sys.argv[1] == '-f':
    return 0
  if sys.argv[1] == '-l':
    numbers[0], numbers[-1] = numbers[-1], numbers[0]
  if sys.argv[1] == '-m':
    middle = (len(numbers)+1)/2-1
    pivot_pos = 0
    if(numbers[0] < numbers[middle] ):
      if(numbers[middle] < numbers[-1] ):
        pivot_pos = middle;
      else: 
        if(numbers[0] < numbers[-1]):
          pivot_pos = -1
        else:
          pivot_pos = 0
    else:
      if(numbers[0] < numbers[-1]):
        pivot_pos = 0
      else:
        if(numbers[-1] < numbers[middle] ):
          pivot_pos = middle
        else:
          pivot_pos = -1
       
    numbers[0], numbers[pivot_pos] = numbers[pivot_pos], numbers[0]

def partitions(numbers):
  first_bigger = 1
  for first_unlooked in range(1,len(numbers)):
    if numbers[first_unlooked] < numbers[0]:
      numbers[first_unlooked], numbers[first_bigger] = numbers[first_bigger], numbers[first_unlooked]
      first_bigger += 1
  numbers[0], numbers[first_bigger-1] = numbers[first_bigger-1], numbers[0]
  return first_bigger - 1

def quick_sort(numbers):
  cmp_num = len(numbers) - 1
  if len(numbers) == 1:
    return 0, numbers
  choose_pivot(numbers)
  pivot_pos = partitions(numbers)
  cmp_left, cmp_right = 0, 0


  if pivot_pos != 0:
    cmp_left, numbers[:pivot_pos] = quick_sort(numbers[:pivot_pos])
  if pivot_pos != len(numbers) - 1:
    cmp_right, numbers[pivot_pos+1:] = quick_sort(numbers[pivot_pos+1:])

  return cmp_num + cmp_left + cmp_right, numbers

def main():
  if len(sys.argv) != 3:
    print "Bad arguments!"
    return -1
  numbers = load_numbers()
  cmp_num, numbers = quick_sort(numbers)
  print "Cmp: ", cmp_num

if __name__ == '__main__':
  main()

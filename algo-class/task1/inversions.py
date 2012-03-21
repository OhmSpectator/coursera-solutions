#!/usr/bin/python

import sys

def get_numbers():
  source = open(sys.argv[1], 'r')
  numbers = []
  for number in source:
    numbers.append(int(number.replace('\n','')))
  return numbers 

def merge_inversions(left_list,right_list):
  invers_num = 0
  sorted_list = []
  while(len(left_list) != 0 and len(right_list) != 0):
    if left_list[0] < right_list[0]:
      sorted_list.append(left_list[0])
      del left_list[0]
    else:
      invers_num += len(left_list)
      sorted_list.append(right_list[0])
      del right_list[0]
  if len(right_list)>0:
    sorted_list.extend(right_list)
    del right_list
  else:
    sorted_list.extend(left_list)
    del left_list
  return invers_num, sorted_list

def count_inversions(numbers):
  invers_num = 0
  if len(numbers) == 1:
    return invers_num, numbers
  else:
    left_invers_num, sorted_left = count_inversions(numbers[:len(numbers)/2])
    right_invers_num, sorted_right = count_inversions(numbers[len(numbers)/2:])
    merged_invers_num, sorted_list = merge_inversions(sorted_left,sorted_right)
    invers_num += left_invers_num + right_invers_num + merged_invers_num
    return invers_num, sorted_list

def main():
  numbers = get_numbers()
  inversions = count_inversions(numbers)[0]
  print inversions

if __name__ == '__main__':
  main()

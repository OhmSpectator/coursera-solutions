#!/usr/bin/python

from Crypto.Hash import SHA256
import random
import sys

def compute_hash(text):
  result = SHA256.new()
  result.update(text)
  return int(bin(int(result.hexdigest(),16))[-50:],2)

def main():
    random.seed()
    found = False
    while not found:
      i = 0
      hashes = {}
      while not found and i < 2**25:
        current_string = hex(random.randint(0, 2**25))[2:]
        current_hash = compute_hash(current_string)
        if current_hash in hashes and hashes[current_hash] != current_string:
          found = True
          print "Answer: %s, %s (hash is %s)" % (current_string.encode('hex'), hashes[current_hash].encode('hex'), current_hash)
        else:
          hashes[current_hash] = current_string
          i += 1
          if i % 10000 == 0:
            print i, current_string
        

if __name__ == '__main__':
  main()

#!/usr/bin/python

import sys
import operator

def strxor(a, b):     # xor two strings of different lengths
  a = a.decode('hex')
  b = b.decode('hex')
  if len(a) > len(b):
    return ("".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])).encode('hex')
  else:
    return ("".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])).encode('hex')

def get_textes():
  source = open(sys.argv[1], 'r')
  texts = []
  for line in source:
    texts.append(line.replace('\n',''))
  return texts

def show_xor(texts):
  interests = list(int(x)-1 for x in sys.argv[2:])
  result = texts[interests[0]]
  for index in interests[1:]:
    result = strxor(texts[index],result)

  space_num = 0
  for symbol in result.decode('hex'):
    if symbol == ' ':
      space_num += 1
  print "SPACES: ", space_num
  
  text = result.decode('hex')
  i = 0
  for symbol in text:
    if symbol > 'A' and symbol < 'Z':
      sys.stdout.write("\033[1;32m")
      sys.stdout.write(symbol.encode('hex'))
      sys.stdout.write("\033[0m")
    else:
      if symbol == '\0':
        sys.stdout.write("\033[1;36m")
        sys.stdout.write(symbol.encode('hex'))
        sys.stdout.write("\033[0m")
      else:
        sys.stdout.write(symbol.encode('hex'))
    if i != len(text)-1:
      sys.stdout.write(":")
    else:
      sys.stdout.write("\n")
    i += 1
  
  #print "HEX: ", ":".join(x.encode('hex') for x in result.decode('hex'))#, "\nASCII: ", result.decode('hex')

def count_spaces(texts,index,toprint):
  spaces = {}
  non_src_texts = texts[:index]
  non_src_texts.extend(texts[index+1:])
  for text in non_src_texts:
    xor = strxor(text, texts[index])
    i = 0
    for symbol in xor.decode('hex'):
      if symbol >= 'A' and symbol <= 'Z':
        if i in spaces:
          spaces[i] += 1
        else:
          spaces[i] = 1
      i += 1
  sorted_spaces = dict(sorted(spaces.iteritems(), key=operator.itemgetter(1), reverse=True)[:int(len(texts[index].decode('hex'))/4.5)])
  text = texts[index]
  if toprint:
    i = 0
    for symbol in text.decode('hex'):
      if i in sorted_spaces:
        sys.stdout.write("\033[1;32m")
        sys.stdout.write(symbol.encode('hex'))
        sys.stdout.write("\033[0m")
      else:
        sys.stdout.write(symbol.encode('hex'))
      if i != len(text.decode('hex'))-1:
        sys.stdout.write(":")
      else:
        sys.stdout.write("\n")
      i += 1

  poses = sorted_spaces.keys()
  return poses
  
def decode(texts):
  key = {}
  i = 0
  for text in texts:
    space_poses = count_spaces(texts,i,False)
    decoded_text = text.decode('hex')
    for pos in space_poses:
      key_char = chr((ord(decoded_text[pos])^ord(' '))).encode('hex')
      if pos in key:
        if key_char in key[pos]:
          key[pos][key_char] += 1
        else:
          key[pos][key_char] = 1
      else:
        key[pos] = {key_char:1} 
    i += 1
  for char in key:
    key[char] = sorted(key[char].iteritems(), key=operator.itemgetter(1), reverse=True)[0]
    print "key[",char,"] = ", key[char]
  result = []
  for i in range(0,len(key)):
    if i in key:
      result.append(key[i][0])
    else:
      result.append('\0'.encode('hex'))

  return "".join( result )
           
def main():
  texts = get_textes()

  if sys.argv[2] == '-f':
    print strxor(texts[0],texts[2]).decode('hex')
  return 1

  if len(sys.argv) == 3:
    if sys.argv[2] == '-t':
      key = decode(texts)
      print "KEY: ", key
      for text in texts:
        print "DECODE: ", strxor(text,key).decode('hex')
    else:
      if sys.argv[2] != '-h':
        count_spaces(texts,int(sys.argv[2])-1,True)
      else:
        print texts[0].encode('hex')
  else:
    show_xor(texts)
      
  
if __name__ == '__main__':
  main()
    

#!/usr/bin/python

import sys
import random

def get_graph():
  result = {}
  source = open(sys.argv[1])
  for line in source:
    result[int(line.split()[0])] = {}
    for i in list( int(x) for x in line.split()[1:] ):
      result[int(line.split()[0])][i] = 1
  return result

def merge(a, b):
  result = a
  for i in b:
    if i not in result:
      result[i] = b[i]
    else:
      result[i] += b[i]
  return result

def choose_edge(graph):
  max_node = max(graph.keys())
  a = random.randint(1, max_node)
  b = random.randint(1, max_node)
  found = False
  while not found:
    if b in graph and a in graph[b]:
      found = True
    else:
      a = random.randint(1, max_node)
      b = random.randint(1, max_node)
  return (a, b)

def contraction(graph):
  if len(graph) != 2:
    edge = choose_edge(graph)
    graph[edge[1]] = merge(graph[edge[0]],graph[edge[1]])
    del graph[edge[0]]
    for node in graph.items():
      if edge[0] in node[1]:
        if edge[1] not in node[1]:
          node[1][edge[1]] = node[1][edge[0]] 
        else:
          node[1][edge[1]] += node[1][edge[0]]
        del node[1][edge[0]]
    del graph[edge[1]][edge[1]]
    return contraction(graph)
  else:
    return graph.values()[0].values()[0]

def main():
  random.seed()
  length = len(get_graph())
  result = []
  for i in range(length*length):
    result.append(contraction(get_graph()))
 
  print min(result)

if __name__ == '__main__':
  main()

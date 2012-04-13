#!/usr/bin/python

import sys 
import resource
import operator
from time import time

t = 0
s = 0
leaders = {}

def get_graphs(node_num = 875714):
  print "Reading graphs...", 
  start = time()
  sys.stdout.flush()
  g = {}
  g_r = {}
  for i in range(1, node_num + 1):
    g[i] = [[], False, i, False]
    g_r[i] = [[], False, i, False]
  source = open(sys.argv[1])
  for line in source:
    g[int(line.split()[0])][0].append(int(line.split()[1]))
    g_r[int(line.split()[1])][0].append(int(line.split()[0]))
  print "completed in", time() - start, "s."
  sys.stdout.flush()
  return g, g_r

def DFS(graph, node):
  graph[node][1] = True
  global leaders
  leaders[node] = s
  for j in graph[node][0]:
    if not graph[j][1]:
      DFS(graph, j)
  global t
  t += 1
  graph[node][2] = t
# print node

def DFS_loop(graph):
  global t
  global s
  t, s = 0, 0
  sys.stdout.flush()
  sorted_graph = sorted(graph.iteritems(), key = lambda node : node[1][2], reverse=True)
  for node in sorted_graph:
    if not node[1][1]:
      s = node
      DFS(graph, node[0])


def main():
  sys.setrecursionlimit(300000)
  resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
  graph, graph_rev = get_graphs()
  print "Computing 1st DFS loop...", 
  start = time()
  sys.stdout.flush()
  DFS_loop(graph_rev)
  print "completed in", time() - start, "s."
  print "Preparing label for forward graph...", 
  start = time()
  sys.stdout.flush()
  for i in range(1, len(graph) + 1):
    graph[i][2] = graph_rev[i][2]
  print "completed in", time() - start, "s."
  sys.stdout.flush()
  print "Computing 2nd DFS loop...", 
  start = time()
  sys.stdout.flush()
  DFS_loop(graph)
  print "completed in", time() - start, "s."
  sys.stdout.flush()
  sccs = {}
  print "Computing SCCs..", 
  start = time()
  sys.stdout.flush()
  for i in leaders:
    leader = leaders[i][0] 
    if leader not in sccs:
      sccs[leader] = 1
    else:
      sccs[leader] += 1
  print "completed in", time() - start, "s."
  sys.stdout.flush()
  sorted_sccs = sorted(sccs.iteritems(), key = lambda label : label[1], reverse = True)
  print "Answer: ", ",".join(list(str(x[1]) for x in sorted_sccs[:5]))

if __name__ == '__main__':
  main()

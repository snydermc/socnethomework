'''
utilities.py

Some utility functions for CSS 692 project

Matt Snyder
Brendon Fuhs

Methods:
writeDictToCSV(reporterDict, filename)
readFromCSV(filename)
add_or_inc_edge(g,f,t)
createBipartite(persons, groups, typeNames = ["person", "group"])
def createWeightedFromBipartite(biGraph, keepAttr)

Usage example:
testDict = reporterDict
filename = "textCSV.csv"
writeDictToCSV(testDict, "textCSV.csv")
'''

import csv
import networkx as nx
import itertools as it

DELIM = "/t"

def writeDictToCSV(reporterDict, filename):
    '''
    filename should be string
    reporterDict should be
    key = numerical index
    list is outlet, byline, wordcount, sublist of organizations mentioned in story, possibly other stuff

    '''
    with open(filename, 'wb') as targetFile:
        file_writer = csv.writer( targetFile, delimiter = DELIM ) # or dialect='excel-tab' ?
        for i in range(1, len(reporterDict)+1):
            file_writer.writerow(reporterDict[i])

def readFromCSV(filename):
    '''
    filename is a string
    return a list of columns
    '''
    bigfile = []
    file_reader = csv.reader( open(filename, 'rb'), delimiter = DELIM ) ### delimiter?
    for row in file_reader:
        bigfile.append(row)
    return zip(*bigfile) # return transposed


def add_or_inc_edge(g,f,t):
    """
    STEALING MAX METHOD!!!
    Adds an edge to the graph IF the edge does not exist already. 
    If it does exist, increment the edge weight.
    Used for quick-and-dirty calculation of projected graphs from 2-mode networks.
    """
    if g.has_edge(f,t):
        g[f][t]['weight']+=1
    else:
        g.add_edge(f,t,weight=1) #### Does weight need to be in quotes here?


def createBipartite(persons, groups, typeNames = ["person", "group"]): ##### UNTESTED # Should this read a dict instead?
    '''
    feed a list of "persons", a list of groups for each person,
     and optionally a length two list of typeName strings
     (what to call persons and groups)
    returns a bimodal graph
     from a list of "persons",
     and a list of "groups" to which each "person" belongs
    '''
    G = nx.Graph()    

    for i in xrange(len(persons)):
        person = persons[i]
        for group in groups[i]:
            G.add_edge(person, group)
            G.node[person]['nodeType'] = typeName[0] # what kind of critter
            G.node[group]['nodeType'] = typeName[1]  # These will get called more than necessary but that's okay.

    return G

def createWeightedFromBipartite(biGraph, keepAttr): ###### UNTESTED
    '''
    feed a bimodel graph, and the name of the node-type fo keep (like "person" or "group")
    returns a weighted graph of the kept node-type
     with edges determined by number of members in common
    '''
    wG = nx.Graph()

    for node in biGraph.nodes():
        if biGraph[node]['nodeType'] != keepAttr:
            for neigh1, neigh2 in it.combinations( nx.all_neighbors(biGraph, node) ):
                add_or_inc_edge(wG, neigh1, neigh2) # Max's method

    return wG

##### Need to scrape twitter

##### Need to do directed graph
"""Objectives:
1. Import csv file data as reporterDict
2. Take byline column and clean it
3. Return a new Dict, identical, except with cleaned up bylines
4. Create a new nested Dict with each reporter as a Key
5. The inner Dict will have groups as a Key and value as total stories
    citing the group.
6. Export this new nested Dict as CSV file:

Reporter1, Org1, # of citations
Reporter1, Org2, # of citations
Reporter1, Org3, # of citations
Reporter2, Org1, # of citations
Reporter2, Org4, # of citations"""

import utilities2 as util
import csv

messfile = 'C:/Users/Naironi/Documents/School Docs 6/SocNet/output1.txt'


def csv_to_list(filename):
    """reads the csv file and then creates a list where each entry is one
    row from the csv file.

    Also creates a blank first line -- that way calling 'storylist[1]' brings
    up the FIRST row in the file rather than the SECOND."""

    file_reader = csv.reader( open(filename, 'rb'), delimiter = '\t')
    storylist = []
    storylist.append(['Blank row', 'NA'])
    for row in file_reader:
        storylist.append(row)

    return storylist

def get_bylines(filename):
    """Reads the csv file and then returns a list of bylines to clean up."""

    storylist = csv_to_list(filename)
    bylinelist = []
    for line in storylist:
        bylinelist.append(line[1])
    return bylinelist

def remove_by(lines_list):
    """ (List) -> List

    Input a list of bylines and then strip each one of "by " """

    newlist = []
    for line in lines_list:
        a = line.lstrip('''By ''')
        newlist.append(a)

    return newlist

def remove_contrib(lines_list):
    """ (List) -> List

    Input a list of bylines and then strip each one of " contributed" verbage
    """

    newlist = []
    for line in lines_list:
        if 'contributed' in line:
            a = line.index('contributed')
            b = line.replace(line[a:], '')

        else:
            b = line

        newlist.append(b)

    return newlist

def remove_inquirer(lines_list):
    """ (List) -> List

    Input a list of bylines and then strip each one of "Inquirer" verbage
    """

    newlist = []
    for line in lines_list:
        if 'Inquirer' in line:
            a = line.index('Inquirer')
            b = line.replace(line[a:], '')

        else:
            b = line

        newlist.append(b)

    return newlist


def clean_up(filename):
    """Cleans up the bylines for the file, removing excess and returning a
    result that's all caps."""

    newlines = get_bylines(filename)
    newlines = remove_by(newlines)
    newlines = remove_contrib(newlines)
    newlines = remove_inquirer(newlines)

    return newlines



finished = clean_up(messfile)

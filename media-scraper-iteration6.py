import csv
from calais import Calais
import utilities

calais_api = 'placeholder key'
calais = Calais(calais_api, submitter='journo-calais-study')

itr = 16
while itr <= 16:
    journo_filename ='C:/Users/Naironi/Documents/School Docs 6/SocNet/feb' + str(itr) + '.txt'
    journo_file = open(journo_filename, 'r')
    journolist = journo_file.readlines()

    #Open and read. Create calais variable.

    reporterDict = {}
    kc = 0
    articlelist = []
    linecount = []
    length_count = []
    endbody_count= []
    bodylist= []
    opinionlist = []


    #Open some Dicts and lists. Counter is used to form Dict keys below.


    for line in journolist:
        if 'DOCUMENTS' in line:
            linecount.append(journolist.index(line))

    #Making a list that saves index for start of each new article in journolist.

    ticker = 0
    while ticker <= len(linecount) - 1:
        if ticker < len(linecount) - 1:
            articlelist.append(journolist[linecount[ticker]:
                                      linecount[ticker+1]- 1])
        if ticker == len(linecount) - 1:
            articlelist.append(journolist[linecount[ticker]:])
        ticker = ticker + 1

    #Nested list of lines into a list of articles.

    for article in articlelist:
        kc = kc + 1
    
        for line in article:
            if 'DOCUMENTS' in line:
                medialine = journolist[journolist.index(line)+3]
            
                if medialine == '\n':
                    medialine = journolist[journolist.index(line)+4]

                medialine.strip("'")
                medialine.strip('\n')

            if 'LENGTH' in line:
                length_count.append(articlelist[kc-1].index(line))
                stripped_length = line.strip('LENGTH:')
                stripped_length.strip('\n')

            
    #Save outlet, lengths, and index for LENGTH and "All rights..." to a variable
        
            if 'BYLINE' in line:
                stripped_line = line.strip('BYLINE:')
                stripped_line.strip('\n')

            if 'SECTION' in line:
                opinion_line = line.lower()
                if 'editorial' in opinion_line or 'commentary' in opinion_line:
                    opinion = 'Opinion'
                else:
                    opinion = 'Not Opinion'


    #Save bylines and whether or not opinion to a variable

        if 'BYLINE' not in str(article):
            stripped_line = 'NA'

        if 'LENGTH' not in str(article):
            length_count.append('NA')

        if 'SECTION' not in str(article):
            opinion = 'Not Opinion'

    #Mark as NA for those without byline.

        body = articlelist[kc-1][length_count[kc-1] + 2:-3]

        bodystring = ''.join(body)
        result = calais.analyze(bodystring)

    #Saves the body between LENGTH line and Copyright line, then analyzes in Calais.

        itemlist = []
        for item in result.entities:
            if 'Organization' in item['_type']:
                itemlist.append(item['name'])

        orglist = []
        for a in itemlist:
            b = a.replace('\n', ' ')
            orglist.append(b)

        topiclist = []
        try:
            for sublist in result.topics:
                topiclist.append(sublist['categoryName'])

        except AttributeError:
            topiclist = ['None']

    #Pull Calais results for Organizations out and save to orglist.

        reporterDict[kc] = [medialine.strip()]
        reporterDict[kc].append(stripped_line.strip())
        reporterDict[kc].append(stripped_length.strip())
        reporterDict[kc].append(orglist)
        reporterDict[kc].append(opinion)
        reporterDict[kc].append(topiclist)
        
    #Drop variables into dictionary.

    export_name = 'C:/Users/Naironi/Documents/School Docs 6/SocNet/output' + str(itr) + '.csv'

    utilities.writeDictToCSV(reporterDict, export_name)

    itr = itr + 1

    #Iterate up the export.


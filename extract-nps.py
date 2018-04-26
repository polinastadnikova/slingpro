"""
extracting NPs from parse trees 
designed for both the RSC and the OBC corpora

author: Polina Stadnikova


for each corpus, the input directory contains a folder with 5 diffent folders (according to the time period)
usage: run the script and follow the instructions

"""


import os
from nltk import tree


def extract(inputdir, outputdir, corpus):
    os.makedirs(outputdir)
    #create a file for statistics
    stat = open(outputdir + '/statistics.txt', 'w')
    #create a file for text names
    names = open(outputdir + '/names.txt', 'w')
    i = 0
    #count only big nps
    overall_big_np = 0
    #count all nps
    overall_all_np = 0
    overall_length = 0
    overall_depth = 0
    #extract from each folder
    for folder in os.listdir(inputdir):
        # outputpath=os.path.join(outputdir,folder)
        # os.makedirs(outputpath)
        dirr = inputdir + '/' + folder
	#take first 10 files
        for file in os.listdir(dirr)[:10]:
            names.write(str(folder)+'\t'+str(file)+'\n')
            i += 1
	    #get parse trees
            if corpus == 'obc':
                content = open(dirr + '/' + file).readlines()[1][10:]
            elif corpus == 'rsc':
                content = open(dirr + '/' + file).readlines()[1][8:]
            tr = tree.Tree.fromstring(content)
            stat.write('**************' + '\n')
            stat.write('Sentence: ' + str(i) + '\n')
            stat.write(content + '\n')
            stat.write('\n')
	    #filter out
            subtrees = tr.subtrees(lambda tr: tr.label() == 'NP')
            agenda = []
            stat.write('NPs: ' + '\n')
            bignp = 0
            nps = 0
            for st in subtrees:
                wr = True
                for t in agenda:
                    if st in t:
                        wr = False
                if wr:
                    bignp += 1
                    stat.write(str(st) + '\n')
                    num_of_nps = len(list(st.subtrees(lambda tr: tr.label() == 'NP'))) - 1
                    stat.write('depth: ' + str(st.height()) + ' ,length: ' + str(len(st.leaves())) + '\n')
                    stat.write('number of NPs: ' + str(num_of_nps) + '\n')
                    stat.write('\n')
                    nps += num_of_nps
                    nps += 1
                    overall_length += len(st.leaves())
                    overall_depth += st.height()
                agenda.append(st.subtrees())
            overall_big_np += bignp
            overall_all_np += nps
            stat.write('Number of big NPs: ' + str(bignp) + ', overall number of NPs: ' + str(nps) + '\n')
            stat.write('\n')
    stat.write('******** Final statistics ********' + '\n')
    stat.write('Number of big NPs for this time period: ' + str(overall_big_np) + ', average per sentence: ' + str(
        overall_big_np / i) + '\n')
    stat.write('Number of all NPs for this time period: ' + str(overall_all_np) + ', average per sentence: ' + str(
        overall_all_np / i) + '\n')
    stat.write('Average length of NPs: ' + str(overall_length / overall_big_np) + '\n')
    stat.write('Average depth of NPs: ' + str(overall_depth / overall_big_np) + '\n')


if __name__ == '__main__':
    inputdir = input("Give the input directory: ")
    outputdir = input("Give the output directory: ")
    corpus = input("Specify the corpus (type obc or rsc): ")
    time = input("Specify the time period (for rsc 1650, 1700, 1750, 1800, 1850, for obc 1700, 1750, 1800, 1850, 1900) :")
    extract(inputdir+'/'+time, outputdir+'/'+time,corpus)



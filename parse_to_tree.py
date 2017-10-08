"""
visualization of the parse trees

author: Polina Stadnikova
"""

import nltk
from nltk import tree
from nltk.draw.tree import draw_trees
from nltk.draw.tree import TreeView
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
import os
merger=PdfFileMerger()

inputdir='shiftreduce-parsed'
outputdir='visualized/shiftreduce'
#treeee=nltk.tree.Tree.fromstring('(ROOT (S (S (INTJ (UH Yes)) (, ,) (NP (NP (DT the) (JJ deceased)) (, ,) (CC and) (NP (QP (CD three) (CC or) (CD four)) (JJR more))) (VP (VBD followed) (NP (NNP Mr.) (NNP Bamber)))) (: ;) (CC but) (S (NP (PRP they)) (VP (VBD took) (NP (DT no) (NN notice)) (PP (IN at) (NP (NP (DT all)) (PP (IN of) (NP (DT any) (NN body))))))) (. .)))')
#TreeView(treeee)._cframe.print_to_file('bla.pdf')


for folder in os.listdir(inputdir):
    newpath=os.path.join(inputdir, folder)
    newoutputpath = os.path.join(outputdir, folder)
    os.makedirs(newoutputpath)
    for file in os.listdir(newpath):
        content=open(newpath+'/'+file)
        id=1
        for line in content.readlines():
            #if 'parse' in line and 'metadata' not in line and 'JJR <' not in line:
                #parse=line[10:]
                parse=line
                parse_tree=nltk.tree.Tree.fromstring(parse)
                #temppath=os.path.join(newoutputpath, 'sentence'+str(id))
                #print(temppath)
                name = newoutputpath+'/sentence'+str(id)+'.pdf'
                TreeView(parse_tree)._cframe.print_to_file(name)
                merger.append(name)
                id+=1
        merger.write(newoutputpath+'/'+file)

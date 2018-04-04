

import os
from nltk import tree

inputdir='new-1700-parsed'
outputdir='np/1700'
stat = open(outputdir+'/statistics.txt', 'w')
i = 0
overall_big_np = 0
overall_all_np = 0
overall_length = 0
overall_depth = 0
for folder in os.listdir(inputdir):
        #outputpath=os.path.join(outputdir,folder)
        #os.makedirs(outputpath)
        dirr= inputdir+'/'+folder
        #print(dirr)
        for file in os.listdir(dirr)[:10]:
                i += 1
                #print(file)
                content=open(dirr+'/'+file).readlines()[1][10:]
                tr = tree.Tree.fromstring(content)
                #tr.draw()
                stat.write('**************'+'\n')
                stat.write('Sentence: '+ str(i)+'\n')

                stat.write(content + '\n')
                stat.write('\n')
                subtrees = tr.subtrees(lambda tr: tr.label()=='NP')
                agenda = []
                stat.write('NPs: ' + '\n')
                bignp= 0
                nps = 0
                for st in subtrees:
                        wr = True
                        for t in agenda:
                                if st in t:
                                        wr = False
                        if wr:
                                bignp += 1
                                stat.write(str(st) + '\n')
                                num_of_nps = len(list(st.subtrees(lambda tr: tr.label()=='NP')))-1
                                stat.write('depth: ' + str(st.height())+' ,length: '+str(len(st.leaves()))+ '\n')
                                stat.write('number of NPs: '+ str(num_of_nps)+'\n')
                                stat.write('\n')
                                nps += num_of_nps
                                nps += 1
                                overall_length += len(st.leaves())
                                overall_depth += st.height()

                        agenda.append(st.subtrees())
                overall_big_np += bignp
                overall_all_np += nps
                #overall_all_np += bignp
                stat.write('Number of big NPs: ' + str(bignp)+', overall number of NPs: '+ str(nps)+'\n')
                stat.write('\n')
stat.write('******** Final statistics ********'+'\n')
stat.write('Number of big NPs for this time period: '+str(overall_big_np) + ', average per sentence: '+str(overall_big_np/i)+'\n')
stat.write('Number of all NPs for this time period: '+str(overall_all_np)+', average per sentence: '+str(overall_all_np/i)+'\n')
stat.write('Average length of NPs: '+str(overall_length/overall_big_np)+'\n')
stat.write('Average depth of NPs: '+str(overall_depth/overall_big_np)+'\n')
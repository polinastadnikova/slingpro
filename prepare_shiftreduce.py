"""
the format for the Shift Reduce Parser

author: Polina Stadnikova
"""

import os
outputdir='shiftreduce_prepared'
inputdir='processed/obc'

#name=os.path.dirname(__file__)
for folder in os.listdir(inputdir):
    outputpath=os.path.join(outputdir,folder)
    os.makedirs(outputpath)
    dirr= inputdir+'/'+folder
    for file in os.listdir(dirr):
        content=open(dirr+'/'+file)
        new_content= ''
        for line in content.readlines():
            for word in line.split(' '):
                if '<s' in word:
                    for w in line.split(' ')[line.split(' ').index(word):]:
                        new_content += w+' '
                    break
                else:
                    if '_' in word:
                        new_word = ''
                        if 'â€”' in word:
                            new_word= word.replace('â€”','.')
                            new_word=new_word.replace('_','/')
                        else:
                            new_word = word.replace('_', '/')
                        new_content+=new_word+' '

        new=open(outputpath+'/'+file, 'w')
        new.write(new_content)
        new.close()

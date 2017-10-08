"""
delete PoS-tags from the text files

author: Polina Stadnikova
"""

import os

outputdir='withoutPostags'
inputdir='processed/obc'
#name=os.path.dirname(__file__)
for folder in os.listdir(inputdir):
    outputpath=os.path.join(outputdir,folder)
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
                        if 'â€”' in word:
                            new_content += word[word.index('_')+1:] + ' '
                        else:
                            new_content += word[:word.index('_')]+' '
        new=open(outputpath+'/'+file, 'w')
        new.write(new_content)
        new.close()

import xml.etree.cElementTree as ET
import sys
import os
import sys
import pandas as pd
# step one put the name of the input folder
foldername = sys.argv[1] # testdatafolder
outputfilename = 'metadata.csv'
#get a list of all filenames from the folder
all_filepaths =  [os.path.join(path, name) for path, subdirs, files in os.walk(foldername) for name in files if name.endswith('xml')]
relevant_filepaths = [filepath.replace(foldername, 'corpus/').rstrip('.nxml')+'.json' for filepath in all_filepaths]



def get_pub_year(filepath):
    '''get pub-date-year based on filepath'''
    root = ET.fromstring(open(filepath).read())
    year = root.findall(".//pub-date/year")[0].text
    return year

def get_pmcid(filepath):
    '''get pub-date-year based on filepath'''
    root = ET.fromstring(open(filepath).read())
    pmcid = root.findall(".//article-id[@pub-id-type='pmc']")[0].text
    return pmcid



files_metadata =  [(all_filepaths[i], relevant_filepaths[i], get_pub_year(all_filepaths[i]), get_pmcid(all_filepaths[i])) for i in range(len(all_filepaths))]

#print files_metadata

df = pd.DataFrame(files_metadata, columns=['filepath', 'new_filepaths','year', 'PMCID'])
print df.head()

df.to_csv(outputfilename, sep=',', encoding='utf-8', index = False)

## Extracts the metadata from files and put the data into a pandas data frame.
### Saves the info as a csv file for later use


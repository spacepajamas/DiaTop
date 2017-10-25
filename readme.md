## Welcome to DiaTop


There are 3 sections to this work.
- Part 1: [Data Extraction](https://gitlab.cl.uzh.ch/pghoshal/DiaTop/tree/master#part-1-data-extraction) 
- Part 2: [Creating LDA models](https://gitlab.cl.uzh.ch/pghoshal/DiaTop/tree/master#part-2-creating-lda-models)
- Part 3: [Mapping data from the LDA model to the corpus](https://gitlab.cl.uzh.ch/pghoshal/DiaTop/tree/master#part-3-mapping-data-from-the-lda-model-to-the-corpus)

## Part 1: Data Extraction 
###  1.1 Metadata extraction
In this section, the metadata is extracted from the input corpus, and saved in  a file called **metadata.csv** .

The metadata is then used for in part 3 for mapping purposes.

Run the following command to extract the metadata :

```sh
$ python Data_Extraction/ExtractMetadata.py inputcorpusfolder/

```
This command runs the **ExtractMetadata.py** script from the **Data_Extraction** folder.


**inputcorpusfolder**: refers to the folder which should contain PubMed XML data files.


For experimental purposes, I have added a folder to this repository called **testdatafolder**. It contains some articles from  PMC Open Access Subset. 
 
###  1.2 Text Extraction and Corpus creation. 
#### 1.2.1 Text pre-processing and filtering
In this section, the article text from the input XML files is extracted and pre-processed here. 
 The text undergoes sentence segmentation, tokenization, and lemmatization. Then the tokens are filtered based on multiple criteria. 
#### 1.2.2 Corpus creation
After the aforementioned pre-processing and filtering, a new corpus is created that will be used to create the LDA model. Moreover, this corpus will be used in **Part 3**, for calculating word frequencies.

Run the following command to pre-process the text and create a new corpus:
```sh
$  python Data_Extraction/ExtractData.py inputcorpusfolder  yes
```
This command runs the **ExtractData.py** script from the **Data_Extraction** folder.
This script takes 2 command line variables 
- **inputcorpusfolder** : path to the input corpus folder
- POS-tagging option, valid input **yes**, or **no**. This variable is used by the script to verify if a POS-tagging and filtering will be done during the data extraction process. 

The output from this process will be saved as individual JSON files in a folder called **corpus**.






## Part 2: Creating LDA models
### 2.1 Create LDA dictionary

The dictionary for the LDA model is created here.
Run the following command to create the LDA dictionary :
```sh
$ python LDA/LDA_1_make_dictionary.py corpus
```
This command runs the **LDA_1_make_dictionary.py** script from the **LDA** folder.

**corpus** : This is the corpus folder that was created during  [Corpus creation](https://gitlab.cl.uzh.ch/pghoshal/DiaTop/tree/master#122-corpus-creation). 

The script usues the data in this folder to generate the dictionary. Learn more about the dictionary format used by Gensim [here](https://radimrehurek.com/gensim/corpora/dictionary.html).
The output of this script is in the folder **LDA_modeldata**, which will be created by this script ( if it does not exist already). 

The dictionary file will be named as follows : 

**original_dict_**\<DATE\>**.dictionary**

**original_dict_**: Denotes that this is the original dictionary created from the corpus.

**.dictionary** : Denotes that this is a dictionary file.

**\<DATE\>** : This is the date on which the dictionary files is created.

**_Example:_** original_dict_2017-06-30.dictionary



### 2.2.1 Optional: Edit  LDA dictionary
The dictionary for the LDA model is modified here.
Run the following command to create a modified LDA dictionary :


```sh
$ python LDA/LDA_2_reduce_dictionary.py <LDA_model_dictionary> <num_mostfrequent_words>
```

This command runs the **LDA_2_reduce_dictionary.py** script from the LDA folder.
The script uses the previously generated dictionary and runs certain fucntions on the script to improve the quality of the dictionary.
**\<LDA_model_dictionary\>** : This is the LDA dictionary that was created during [Create LDA dictionary](https://gitlab.cl.uzh.ch/pghoshal/DiaTop/tree/master#21-create-lda-dictionary). 

**\<num_mostfrequent_words\>** : Refers to the number of most frquent words that one wishes to remove from the dictionary. 

The output of this script can also be found in the folder **LDA_modeldata**.


The new dictionary file will be named as follows :

**mod_dict_**\<DATE\>**.dictionary**


**mod_dict_**: Denotes that this is the modified dictionary created from the original dictionary.

**.dictionary** : Denotes that this is a dictionary file.

**\<DATE\>** : This is the date on which the dictionary files is created.

**_Example:_** mod_dict_2017-06-30.dictionary


## 2.2 Create LDA corpus
The corpus for the LDA model is created here.
Learn more about the corpus created by Gensim [here](https://radimrehurek.com/gensim/corpora/mmcorpus.html).
Run the following command to create the LDA corpus :
```sh
$ python LDA/LDA_3_make_corpus.py corpus LDA_modeldata/<dictionary file>
```
This command runs the **LDA_3_make_corpus.py** script from the LDA folder.

**corpus** : This is the corpus folder that was created during  [Corpus creation](https://gitlab.cl.uzh.ch/pghoshal/DiaTop/tree/master#122-corpus-creation). 

**LDA_modeldata/\<dictionary file\>**: This is the **.dictionary** file  (in the LDA_modeldata folder) that one wishes to use to create the corpus. 

The output of this script can also be found in the folder **LDA_modeldata**.

The new corpus file will be named as follows :
**corp_**\<DATE\>**.corpus**

**corp_**: Denotes that this is the corpus.

**.corpus** : Denotes that this is a corpus file.

**\<DATE\>** : This is the date on which the corpus file is created.

**_Example_**: corp_2017-06-30.corpus




## 2.3 Create LDA model
The LDA model is created here.

Run the following command to create the LDA corpus :

```sh
$ python LDA/LDA_4_create_LDA_Model.py <workers> <chunksize> <passes> <numtopics> <version> <LDA_model_dictionary> <LDA_model_corpus>
```

This command runs the **LDA_4_create_LDA_Model.py** script from the LDA folder.

Learn more about the parametres uses by Gensim to create the LDA model [here](https://radimrehurek.com/gensim/models/ldamulticore.html).

**\<workers\>** : Denotes the number of processes to use for parallelization.


**\<chunksize\>** : Denotes the number of documents used for each step of online training. 


**\<passes\>** : Denotes the number of times the model goes through the entire corpus


**\<numtopics\>** : Denotes the number latent topics to be extracted from the  corpus.

**\<version\>** : Denotes the version of the model. Can be used to distinguish multiple models. Valid input: any string.


**\<passes\>** : Denotes the number of times the model goes through the entire corpus.


**\<LDA_model_dictionary\>** : This is the **.dictionary** file (in the LDA_modeldata folder) that one wishes to use generate the model.


**\<LDA_model_corpus\>** : This is the **.corpus** file (in the LDA_modeldata folder) that one wishes to use generate the model.

The new LDA model file will be named as follows :

**model_\<DATE\>**\_\_**\<numtopics\>**\_**\<workers\>**\_**\<chunksize\>**\_**\<passes\>_v-\<version\>.LDA**'

**model_** : enotes that this is the LDA model.
**\<DATE\>** : This is the date on which the LDA model file is created.
**.LDA** : Denotes that this is a model file, and the .LDA is used the mark the file as the _main_ model file.

See above fot the explanation of the other parameters.


**_Example_** : model_2017-06-30__10_2_20_50_v-1.LDA



## Part 3: Mapping data from the LDA model to the corpus

### 3.1 Get document topic distribution
Generates the document topic distribtuion of all files from the corpus using the LDA model, LDA corpus and the metadata. 


Run the following command to get the  document topic distribution :

This command runs the **Mapping_1_get_document_topic_distribution.py** script from the Mapping folder.


```sh
$ python Mapping/Mapping_1_get_document_topic_distribution.py  <LDA_model_corpus>  <LDA_model> metadata.csv
```
**\<LDA_model_corpus\>** : This is the **.corpus** file (in the LDA_modeldata folder) that one wishes to use generate the model.

**\<LDA_model\>** : This is the **.LDA** file (in the LDA_modeldata folder) which is the LDA model file.

**metadata.csv**: This is the file that contains all the metadata information about the corpus during [Metadata extraction](https://gitlab.cl.uzh.ch/pghoshal/DiaTop/tree/master#11-metadata-extraction).

The new output file will be named as follows :

**_Example_** : M1_topic_distr_df_2017-06-30.csv

**M1_topic_distr_df_** : Denotes that this is the output of the first mappping procedure (**M1**), and that it is a dataframe containing the topic distribution data .

**\<DATE\>** : This is the date on which this file is created.

**.csv** : Denotes that this is a CSV file.


#### 3.1.1 Average yearly topic distribuition 
Generates a CSV file that shows the average yearly topic distrubution of LDA model using the topic distribution of the topics from  [Get document topic distribution](https://gitlab.cl.uzh.ch/pghoshal/DiaTop/blob/master/readme.md#31-get-document-topic-distribution).

Run the following command to get the average yearly topic distrubution :


```sh
$ python Mapping/Mapping_1_1_yearly_doc_top.dist.py M1_topic_distr_df_<DATE>.csv <LDA_model>
```



This command runs the Mapping_1_1_yearly_doc_top.dist.py script from the Mapping folder.

**M1_topic_distr_df_\<DATE\>.csv** : This is the output (CSV file) of [Get document topic distribution](https://gitlab.cl.uzh.ch/pghoshal/DiaTop/blob/master/readme.md#31-get-document-topic-distribution)

**\<LDA_model\>** : This is the **.LDA** file (in the LDA_modeldata folder) which is the LDA model file.


The new output file will be named as follows :

M1_1_yearly_average_topic_distrbution_\<DATE\>.csv

**M1_1_yearly_average_topic_distrbution_** : Denotes that this is the output of the first mappping procedure (**M1**), and that it is a dataframe containing average yearly topic distrubution of LDA model.

**\<DATE\>** : This is the date on which this file is created.

**.csv** : Denotes that this is a CSV file.

**_Example_** : M1_1_yearly_average_topic_distrbution_2017-06-30.csv



## 3.2 Topic word distribution

Generates the document topic distribtuion of all files from the corpus using the [corpus](https://gitlab.cl.uzh.ch/pghoshal/DiaTop/edit/master/readme.md#122-corpus-creation), the topics from the LDA model, and the metadata.


Run the following command to get the topic word distribution for each topic word :



```sh
$ python Mapping/Mapping_2_get_topic_word_distribution.py <LDA_model> <inputcorpusfolder> metadata.csv
```

This command runs the Mapping_2_get_topic_word_distribution.py script from the Mapping folder.

**\<LDA_model\>** : This is the **.LDA** file (in the LDA_modeldata folder) which is the LDA model file.

**inputcorpusfolder**: refers to the folder which should contain PubMed XML data files.

**metadata.csv**: This is the file that contains all the metadata information about the corpus during [Metadata extraction](https://gitlab.cl.uzh.ch/pghoshal/DiaTop/tree/master#11-metadata-extraction).


The new output file will be named as follows :


'M2_topic_word_dist_df_\<DATE\>.csv



**M2_topic_word_dist_df_** : Denotes that this is the output of the sencond mappping procedure (**M2**), and that it is a dataframe containing the topic word distribution of all the documents in the LDA model.

**\<DATE\>** : This is the date on which this file is created.

**.csv** : Denotes that this is a CSV file.

**_Example_** : M2_topic_word_dist_df_2017-06-30.csv












### 3.2.1 Relative yearly topic word distribuition 

Generates a CSV file that shows the relative yearly topic word distribuition  of the LDA model using the topic word distribution of the topics from  [Topic word distribution](https://gitlab.cl.uzh.ch/pghoshal/DiaTop/blob/master/readme.md#32-topic-word-distribution).



Run the following command to get the topic relative yearly topic word distribuition for each topic word for a given topic:

```sh
$ python Mapping/Mapping_2_1_get_yearly_topic_word_distribution.py <LDA_model> <inputcorpusfolder> M2_topic_word_dist_df_<DATE>.csv <topicnumber>
```
This command runs the **Mapping_2_1_get_yearly_topic_word_distribution.py** script from the Mapping folder.


**\<LDA_model\>** : This is the **.LDA** file (in the LDA_modeldata folder) which is the LDA model file.

**inputcorpusfolder**: refers to the folder which should contain PubMed XML data files.


**M2_topic_word_dist_df_\<DATE\>.csv**: This is the output (CSV file) of [Topic word distribution](https://gitlab.cl.uzh.ch/pghoshal/DiaTop/blob/master/readme.md#32-topic-word-distribution)


**\<topicnumber\>** : Denotes the topic number for which the CSV file will be generated






## 3.3 Distribution of top _n_ most popular words


In this section, for each topic in the LDA model, this script divides the corpus into topic subcorpora. 
For each subcorpus, the script calculates the top **n** most common words. This is calculates if the word occurs in the document that make up this subcorpus. 
The script uses the data from [Get document topic distribution](https://gitlab.cl.uzh.ch/pghoshal/DiaTop/blob/master/readme.md#31-get-document-topic-distribution).


Run the following command to get the distribution of top _n_ most popular words each topic topic:


```sh
$ python Mapping/Mapping_3_get_TOP_word_distribution.py M1_topic_distr_df_<DATE>.csv <LDA_model> <number of top words>

```
This command runs the **Mapping_3_get_TOP_word_distribution.py** script from the Mapping folder.



**M1_topic_distr_df_** : Denotes that this is the output of the first mappping procedure (**M1**), and that it is a dataframe containing the topic distribution data .

**\<LDA_model\>** : This is the **.LDA** file (in the LDA_modeldata folder) which is the LDA model file.

**\<number of top words\>** : number of most popular words in the corpus



### 3.3.1 Relative frequency of top _n_ most popular words for each year




Run the following command to get the yearly relative frequency of top _n_ most popular words for a given topic:


```sh
$ python Mapping/Mapping_3_1_get_TOP_word_distribution_giventopic.py <LDA_model> <topicnumber>
```
This command runs the **Mapping_3_1_get_TOP_word_distribution_giventopic.py** script from the Mapping folder.

**\<LDA_model\>** : This is the **.LDA** file (in the LDA_modeldata folder) which is the LDA model file.

**\<topicnumber\>** : Denotes the topic number for which the CSV file will be generated


This repository contains the scripts that were used to generate the results for my [MA thesis](http://www.mlta.uzh.ch/dam/jcr:493e6e0d-cea7-4eff-ab5b-28550ef59b7a/Masterarbeit_PGhoshal_FS2017.pdf).

Link to [slides](https://drive.google.com/open?id=1N1HZMpcsKksZbKS2X-IpbzoFliwQl11_fHHKzAL6bCU).


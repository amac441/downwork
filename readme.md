# Down Work

These are a collection of .py and ipython scripts and data file for 3/30/17 upwork research project.

### Prerequisites

Prereq's to running these scripts include:
```
python 3+ # for scraping scripts
python 2.7 # for upwork API calls
Selenium # for web scraping / automation
ipython # for interactive development (I'm usining the jupyter anaconda distribution)
pandas
numpy
```
[chromedriver.exe](https://sites.google.com/a/chromium.org/chromedriver/) will need to be downloaded and placed alongside the main.py script.

### Overview of Files

* [01-17-upwork_master](#main) - Master script
  * **Input.csv** - the input file for the master script - contains login data

* [03_02_Reading_Resources.ipynb](#readAPI) - Aggregating API Reads, Filtering Data, and Marking already used data (Creating a new master)
* [mark_used.py](#supplement) - generalized script for marking used files within a "Master" list
* [api_people_search.py](#supplement) - search people using the API
* **Data Files**
  * **All_Writers_18k.csv** - File from API Pull including "Already Used people"
  * **Merged_Batch_1** - Batch 1 results.
  * **Batch_1_159.csv** - the datafile for master - contains all people to be messaged. Note that this file gets split into sequential groups of 25 for the 6 accounts used in Batch 1

<a name="main"></a>
## Main Upwork Script

This is the main script used to automate the messaging of upwork candidates. This script does the following tasks:

* Logging Into Upwork
* *Create* a Job under a specific account
* *Submit* Invite to Candidates under a specific account (in batches of 25)
* *Read* Responses
* *Decline* a Job and Messaging Candidates
* Reading Employee *Details*

The script argumenta are as follows

```
<login number -comes from input.csv> <command (create|submit|read|iterate|decline|details)>-<Send message (T|F)> <Input File Name (default:input.csv)>
```
So a few examples would be
```
#create a job for login 1
python 01-17-upwork_master.py 1 create-T

#gather details for login 4h candidates, but don't submit the message
4 submit-F

#read the details for a collection candidates, specified in a different input file
1 details input2.csv
```

These commands can be seen in-action in the run.bat file.

## Input Files

Note that the input file contains the following data:

id | email |	password | amount	| skip	| prospectFile | outputfile | negot

The first record (below the header) is a dummy record, which can contain a "test" account. Rows 3->X should contain the production account for the given test batch.

Because input files contain sensetive info, they are not in this repository, but can be found in the gdrive.

<a name="readAPI"></a>
## Evaluating Results

There are several iPython notebooks in the repository with various functions to read, clean, and merge the data.  Generally, I just write these scripts on an ad-hoc basis.

Here's an example of how to load a collection of CSVs and dropping duplicates using python pandas.

```
from MultiProcessDataframe import callfunction
basefolder=r'C:\Users\amac\Documents\GoogleDrive\Washu\01-17-Dai\Upwork\UpworkShared\Batch1\Batch1Input\159'
print ("Calling MultiProcess")
b159 = callfunction(basefolder)
print(b159.shape)
b2=b159.drop_duplicates(subset='id')
print(b2.shape)
```

<a name="supplement"></a>
## Supplement Files

There are a few supplement scripts in the repository that should be self-explanatory in name and execution.

The *api_people_search.py* and the *manual_people_search.py* are related, in that they both retrieve a list of available resources based on some filtering criteria.  

*mark_used.py* is an untested script that takes a list of input files contiaining "Used" people and a file of ALL available people and marks rows as 'used'.

import os
import boto
import boto.s3.connection
#from past import warc
'''
http://stackoverflow.com/questions/9047745/where-is-the-builtin-module-in-python3-why-was-it-renamed

-we solve this by importing builtins as __builtin__

python3 version of warc is warc3---at least the one that will work
-to install a git repo using pip use the following style of commands:
    pip install git+https://github.com/erroneousboat/warc3
    pip install git+git://...


Boto Tutorial Reference:
    1) http://boto.cloudhackers.com/en/latest/s3_tut.html

StringIO module in python3 is instead the io module where you can invoke

    REF) http://stackoverflow.com/questions/11914472/stringio-in-python3

    1) io.StringIO (for text)
    2) io.BytesIO (for data)

gzip Tutorial Reference:
    1) https://pymotw.com/2/gzip/
    2) 

gzipstream
    1) what is it:

    2) pip install git+https://github.com/Smerity/gzipstream.git
    3) this needs to be modified so we have cloned it to a local directory and will
    4) how to install something with pip from a local direcotry
    pip install mypackage --no-index --find-links file:///srv/pkg/mypackage
    OR
    pip install mypackage --no-index --find-links /Users/juhwanyoo/Documents/qadium/gzipstream

WARC Tutorial
    1) http://warc.readthedocs.io/en/latest/
    2) pip3 install warcat
    3) another module that could help: https://pypi.python.org/pypi/Warcat/


'''
#import builtins as __builtin__  # solves python incompatibility in warc module import
#import warc # this import has been causing me issues
import warc
import gzip
from gzip import GzipFile
import gzipstream
from gzipstream import GzipStreamFile

import io

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#filepath = 'crawl-data/CC-MAIN-2016-50/segments/1480698540409.8/warc/CC-MAIN-20161202170900-00000-p-10-31-129-80.ec2.internal.warc.gz'

filepath = 'crawl-data/CC-MAIN-2016-50/segments/1480698540409.8/warc/CC-MAIN-20161202170900-00000-ip-10-31-129-80.ec2.internal.warc.gz'

# establish anonymous connection to commoncrawl warc file bucket
conn = boto.s3.connect_to_region(
        "us-east-1",
        anon=True,
        calling_format=boto.s3.connection.OrdinaryCallingFormat(),
        is_secure=False
    )
bucket = conn.get_bucket('commoncrawl')
#filereader = Key(bucket)
filereader = boto.s3.key.Key(bucket)
filereader.key = filepath

# Updating code to python3 standards, GzipStreamFile is really just GzipFile

warc_file = warc.WARCFile(fileobj=GzipStreamFile(filereader))


for record in warc_file:
    print(record.payload.read())
#warc_file = warc.WARCFile(fileobj=GzipFile(filereader))

#warc_file = warc.WARCFile(fileobj=filereader)

#warc_stream = open_warc_stream(partition["path"])

#for record in warc_stream:
#    print(record.payload.read())
    #payload = record.payload.read()
    #parser = HttpParser()
    #parser.execute(payload, len(payload)()



'''
#for record in wfile: 
for record in warc_file:
    # You can check the record header to see if it's HTML
    # See cosrlib.sources.webarchive.WebarchiveSource.iteritems
    print(record.payload.read())
'''


'''
At this point we would like to know how to process a warc record....Can't convert bytes object to string implicitly:
    -gzipstreamfile.py in 

WARC Help:
Reading a WARC File
Reading a warc file is as simple as reading a simple file. Instead of returning lines, it returns WARC records.

import warc
f = warc.open("test.warc.gz")
for record in f:
    print record['WARC-Target-URI'], record['Content-Length']
The open function is a shorthand for warc.WARCFile.:

f = warc.WARCFile("test.warc.gz", "rb")
f = warc.WARCFile(fileobj=StringIO(text))
Writing WARC File
Writing to a warc file is similar to writing to a regular file.:

f = warc.open("test.warc.gz", "w")
f.write_record(warc_record1)
f.write_record(warc_record2)
f.close()

'''

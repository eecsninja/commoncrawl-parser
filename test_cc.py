'''
1) Question: how do we pull down warc 3 files....
    -cosr-back and cosr-ops seem to be able to do this. Why can't we.
    -in tehory, we could use mrjob, but we would Ideally like to parallelize this operation, so how do we go about solving that particular problem.
    -
    
export IS_SPARK=1
export SPARK_DIST_CLASSPATH=$(hadoop classpath)

# graphframes:graphframes:0.1.0-spark1.6
spark.jars.packages org.apache.hadoop:hadoop-aws:2.7.2,com.amazonaws:aws-java-sdk:1.7.4
spark.jars.ivy /usr/spark/packages/

commoncrawl.py is one of the key methods of connecting to the common crawl data base

The following lines were in spark.py

# http://deploymentzone.com/2015/12/20/s3a-on-spark-on-aws-ec2/
# https://hadoop.apache.org/docs/stable/hadoop-aws/tools/hadoop-aws/index.html

in the setup spark contexrt


from elasticsearch import Elasticsearch
from elasticsearch.client import IndicesClient
from elasticsearch.exceptions import ConnectionTimeout

from .config import config
from .es_mappings import ES_MAPPINGS, ES_SIMILARITIES

'''

'''
# Potentially useful libraries

1) cosr-lib


1) pyspark
2) cosrlib
3) 
'''



'''
Explicit Tasks We Need To Learn
1) How do we pull down commoncrawl data from S3
    -there's the issue of credentials....what else??
'''

'''
Invoking python 3 functionality from within python2
from __future__ import unicode_literals, division, print_function, absolute_import
from __future__ import unicode_literals

https://github.com/qadium/onboard/blob/master/CodingStandards.md
'''



'''
PEP-8 Conventions:

Imports should be grouped in the following order:

standard library imports
related third party imports
local application/library specific imports

JY COMMENT: Import relative versus absolute imports
e.g.

import mypkg.sibling
from mypkg import sibling
from mypkg.sibling import example

from . import sibling
from .sibling import example

do not import modules in a way that cause local name clashes.



Module level dunder names
Module level "dunders" (i.e. names with two leading and two trailing underscores) such as __all__ , __author__ , __version__ , etc. should be placed after the module docstring but before any import statements except from __future__ imports. Python mandates that future-imports must appear in the module before any other code except docstrings.

For example:

"""This is the example module.

This module does stuff.
"""

from __future__ import barry_as_FLUFL

__all__ = ['a', 'b', 'c']
__version__ = '0.1'
__author__ = 'Cardinal Biggles'

import os
import sys

'''


filepath = 'crawl-data/CC-MAIN-2016-50/segments/1480698540409.8/warc/CC-MAIN-20161202170900-00000-p-10-31-129-80.ec2.internal.warc.gz'
conn = boto.s3.connect_to_region(
                "us-east-1",
                anon=True,
                calling_format=boto.s3.connection.OrdinaryCallingFormat(),
                is_secure=False
            )
bucket = conn.get_bucket('commoncrawl')
filereader = Key(bucket)
filereader.key = filepath

warc_file = warc.WARCFile(fileobj=GzipStreamFile(filereader))

 for record in wfile: 
    # You can check the record header to see if it's HTML
    # See cosrlib.sources.webarchive.WebarchiveSource.iteritems
    print(record.payload.read())
```




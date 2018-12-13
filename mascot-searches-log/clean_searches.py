# clean_searches.py
# This script is used to clean Mascot's search log and must be executed in the
# same folder as searches.log.
# Searches from years in variable yearsToKeep will be kept.
# Only one file name will be written to avoid line overflows.
# The clean searches.log can be found in the same folder as clean_searches.log.

import re
import os
import datetime

targetFile = "searches.log"
yearsToKeep = [2017, 2018]

# Reading searches log and creating backup
with open(targetFile, 'r', encoding="ISO-8859-1") as f:
    # Read all lines from searches.log
    data = f.readlines()

with open('clean_'+targetFile, 'w', encoding="ISO-8859-1") as f:
    f.write(data[0])
    # Pattern used to find the search date
    datePattern = re.compile('([A-Za-z]{3}?\s+?){2}[0-9]+?\s+?([0-9]{2}?:){2}'
                                '[0-9]{2}\s+?([0-9]{4}?)')
    # Pattern used to get the first file name
    fileNamePattern = re.compile('(File Name:.*?)File Name')
    for l in data:
        # Keep only one file name
        result = fileNamePattern.search(l)
        if result:
            l = l.split(result.group(1))[0] + result.group(1) + '\n'

        # Eliminate all entries prior to 2017
        result = datePattern.search(l)
        if result and int(result.group(3)) in yearsToKeep:
            f.write(l)

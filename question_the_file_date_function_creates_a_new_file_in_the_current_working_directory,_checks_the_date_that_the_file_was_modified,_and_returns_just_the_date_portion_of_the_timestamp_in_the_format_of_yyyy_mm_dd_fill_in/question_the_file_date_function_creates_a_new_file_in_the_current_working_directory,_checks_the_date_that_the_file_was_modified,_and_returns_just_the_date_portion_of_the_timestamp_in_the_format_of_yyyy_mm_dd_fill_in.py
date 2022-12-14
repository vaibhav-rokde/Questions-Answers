# -*- coding: utf-8 -*-
"""Question :The file_date function creates a new file in the current working directory, checks the date that the file was modified, and returns just the date portion of the timestamp in the format of yyyy-mm-dd. Fill in the gaps to create a file called "nw"

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rXpo-YHwngZ0Tz4GkpQ9cwG9J89BgJSk

### Question 
Question
The file_date function creates a new file in the current working directory, checks the date that the file was modified, and returns just the date portion of the timestamp in the format of yyyy-mm-dd. Fill in the gaps to create a file called "newfile.txt" and check the date that it was modified.
"""

import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  with open (filename,'w') as file:
    pass
  timestamp = os.path.getmtime(filename)
  d=datetime.datetime.fromtimestamp(timestamp)
  # Convert the timestamp into a readable format, then into a string
 
  # Return just the date portion 
  # Hint: how many characters are in “yyyy-mm-dd”? 
  return ("{}".format(d.strftime("%Y-%m-%d")))

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd


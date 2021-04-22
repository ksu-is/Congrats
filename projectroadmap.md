This will be used to update as we go with what we find

For our project the idea is to create a random generator that basically you could use to put in bucket list items or just things someone would like to do and then after running the code it will generate an option for you to do while crossing it off the list as well.
After that once you have visited or completed all the items it will read out the message saying, “Congratulations on completing your Bucket List!” 

We were thinking a random number generator sequence would help populate the start of the python code like this one from github

https://github.com/libmir/mir-random

But also this one as they have it formatted to what seems to be a bucket list sequence

https://github.com/ashratigan/bucket-list-client

What we would like those is that it continues functioning and after one is selected it will not populate that one again all until the last one is complete and again reads out the message congratulating you for completing your bucket list challenge. 

Melisa will be working on finding the item that will be able to cross out items therefore they cannot be chosen again.

Austin will be working on the random generating ability of doing full sentences if needed rather than just one word options

Both of us are focusing on one portion and working to combine them so they will flow together

One code that we have attempted is the following

# Python code to pick a random
# word from a text file
import random
  
# Open the file in read mode
with open("MyFile.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))
  
 # print random string
    print(random.choice(words))
    
    
  Updates as of 4.22.21
  
    After further review it seems that using a text file will be needed in order for this process to work
    In order for this to function a folder will be needed to hold the program and two text files
    one file will be called "completed task" which will be the bucket list items that gets updated each time the
    code is ran.
    
    We have started the beginning of code however still make sure formatting is correct amongst pulling
    correct information from the two files. Outside sources like YouTube, Google, etc.
    has been helping create this file.
    
    #See start of code file

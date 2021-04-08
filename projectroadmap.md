For our project the idea is to create a random generator that basically you could use to put in bucket list items or just things someone would like to do and then after running the code it will generate an option for you to do while crossing it off the list as well.
After that once you have visited or completed all the items it will read out the message saying, “Congratulations on completing your Bucket List!” 

I was thinking a random number generator sequence would help populate the start of the python code like this one from github

https://github.com/libmir/mir-random

But also this one as they have it formatted to what seems to be a bucket list sequence

https://github.com/ashratigan/bucket-list-client

What we would like those is that it continues functioning and after one is selected it will not populate that one again all until the last one is complete and again reads out the message congratulating you for completing your bucket list challenge. 
![image](https://user-images.githubusercontent.com/77759089/114107335-cc03fc00-989e-11eb-945a-194ce86d82a1.png)

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

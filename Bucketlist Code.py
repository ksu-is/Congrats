import random
if __name__=="__main__":
    print("Lets start")
    while True:
        user_input = int(input("1.Do you want to randomly get a task of your bucket list\n2.Add a new item to bucket list\n3.Exit\n"))
        if user_input ==1:
            bucket_list =  open('myBucketList.txt','r')
            lines = bucket_list.readlines()
            get_random_line = random.choice(lines)
            print("Here you go:",get_random_line.strip())
            complete = int(input("1. Are you going to complete it now?\n2. Rerun\n"))
            if complete ==1:
                completed_task = open('completedTasks.txt','a')
                completed_task.write(get_random_line.strip())
                completed_task.close()
                lines.remove(get_random_line)
            bucket_list.close()
            bucket_list =  open('myBucketList.txt','w')
            bucket_list.write("".join(lines))
            bucket_list.close()
        elif user_input ==2:
            bucket_list =  open('myBucketList.txt','a')
            user_task = input("Enter an item to bucket list")
            bucket_list.write("\n")
            bucket_list.write(user_task)
            bucket_list.close()
            print("Task Added")
        elif user_input ==3:
            break
        else:
            print("Invalid input. Try again")
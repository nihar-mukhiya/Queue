from collections import deque
import sys
queue = deque([])
while(1):
    z = int(input("enter your choice:\n 1.Enqueue:\n2.Dequeue:\n 3.Print\n 4. Exit\n"))
    if(z == 1):
        n = int(input("enter number of elements to be inserted: "))
        for i in range(n):
            inputter = input("enter element: ")
            queue.append(inputter)
    elif(z == 2):
        queue.popleft()
    elif(z == 3):
        print(queue)
    elif(z == 4):
        sys.exit()
    else:
        print("invalid input!!")

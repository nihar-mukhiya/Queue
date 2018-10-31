import heapq
import sys
list1 = []
inputter = int(input("enter the number of elements to be inserted in list: "))
for i in range(inputter):
    inputter1 = int(input("enter elements: "))
    list1.append(inputter1)
while(1):
    z = int(input("1.push\n 2.pop\n 3.pushpop\n 4.replace\n 5.print\n"))
    if z == 1:
        g = int(input("enter element: "))
        heapq.heappush(list1, g)
    if z == 2:
        temp = heapq.heappop(list1)
        print(str(temp)+" popped!!")
    if z == 3:
        h= int(input("enter element: "))
        heapq.heapify(list1)
        temp1 = heapq.heappushpop(list1, h)

        print(str(temp1) + " popped!!")
    if z == 4:
        j = int(input("enter element to be pushed: "))
        heapq.heapify(list1)
        temp2 = heapq.heapreplace(list1, j)
        print(str(temp2) + " popped!!")
    if z == 5:
        heapq.heapify(list1)
        print(list1)
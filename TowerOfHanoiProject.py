    
import sys
import time
import matplotlib.pyplot as plot 

########################Recursive approach using Stacks########################
def RecursiveHanoi(num_of_disks, from_rod, to_rod, aux_rod):
    if num_of_disks == 1:
        print("Move disk 1 from rod",from_rod,"to rod",to_rod)
        return
    RecursiveHanoi(num_of_disks-1, from_rod, aux_rod, to_rod)
    print("Move disk",num_of_disks,"from rod",from_rod,"to rod",to_rod)
    RecursiveHanoi(num_of_disks-1, aux_rod, to_rod, from_rod)

##############Iterative approach using stacks################################## 
# A structure to represent a stack
class Stack:
    # Constructor to set the data of
    # the newly created tree node
    def __init__(self, capacity):
        self.capacity = capacity
        self.top = -1
        self.array = [0]*capacity
 
# function to create a stack of given capacity.
def createStack(capacity):
    stack = Stack(capacity)
    return stack
  
# Stack is full when top is equal to the last index
def isFull(stack):
    return (stack.top == (stack.capacity - 1))
   
# Stack is empty when top is equal to -1
def isEmpty(stack):
    return (stack.top == -1)
   
# Function to add an item to stack.
# It increases top by 1
def push(stack, item):
    if(isFull(stack)):
        return
    stack.top+=1
    stack.array[stack.top] = item
   
# Function to remove an item from stack.
# It decreases top by 1
def Pop(stack):
    if(isEmpty(stack)):
        return -sys.maxsize
    Top = stack.top
    stack.top-=1
    return stack.array[Top]
   
# Function to implement legal
# movement between two poles
def moveDisksBetweenTwoPoles(src, dest, s, d):
    pole1TopDisk = Pop(src)
    pole2TopDisk = Pop(dest)
 
    # When pole 1 is empty
    if (pole1TopDisk == -sys.maxsize):
        push(src, pole2TopDisk)
        moveDisk(d, s, pole2TopDisk)
       
    # When pole2 pole is empty
    elif (pole2TopDisk == -sys.maxsize):
        push(dest, pole1TopDisk)
        moveDisk(s, d, pole1TopDisk)
       
    # When top disk of pole1 > top disk of pole2
    elif (pole1TopDisk > pole2TopDisk):
        push(src, pole1TopDisk)
        push(src, pole2TopDisk)
        moveDisk(d, s, pole2TopDisk)
       
    # When top disk of pole1 < top disk of pole2
    else:
        push(dest, pole2TopDisk)
        push(dest, pole1TopDisk)
        moveDisk(s, d, pole1TopDisk)
   
# Function to show the movement of disks
def moveDisk(fromPeg, toPeg, disk):
    print("Move the disk", disk, "from '", fromPeg, "' to '", toPeg, "'")
   
# Function to implement TOH puzzle
def tohIterative(num_of_disks, src, aux, dest):
    s, d, a = 'A', 'B', 'C'
   
    # If number of disks is even, then interchange
    # destination pole and auxiliary pole
    if (num_of_disks % 2 == 0):
        temp = d
        d = a
        a = temp
    total_num_of_moves = int(pow(2, num_of_disks) - 1)
   
    # Larger disks will be pushed first
    for i in range(num_of_disks, 0, -1):
        push(src, i)
   
    for i in range(1, total_num_of_moves + 1):
        if (i % 3 == 1):
            moveDisksBetweenTwoPoles(src, dest, s, d)
   
        elif (i % 3 == 2):
            moveDisksBetweenTwoPoles(src, aux, s, a)
   
        elif (i % 3 == 0):
            moveDisksBetweenTwoPoles(aux, dest, a, d)
 
# Input: number of disks
num_of_disks = 5
 
# Create three stacks of size 'num_of_disks'
# to hold the disks
src = createStack(num_of_disks)
dest = createStack(num_of_disks)
aux = createStack(num_of_disks)


#################Tower of Hanoi using Queue Data Structure##########
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return "Disc({})".format(self.value)


class Queue:
    def __init__(self, name):
        self.name = name
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def len(self):
        current = self.head
        len = 0
        while current is not None:
            len += 1
            current = current.next
        return len

    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        if self.is_empty():
            return "EMPTY"
        elif self.head == self.tail:
            help = self.head.value
            self.head = None
            self.tail = None
            return help
        else:
            jump = self.head.value
            self.head = self.head.next
            return jump

    def peek(self):
        return self.head.value


class QueueTower:
    def __init__(self, number_of_discs):
        self.number_of_discs = number_of_discs
        self.A, self.B, self.C = Queue("A"), Queue("B"), Queue("C")

        for i in range(number_of_discs, 0, -1):
            self.A.enqueue(i)

    def reverse_queue(self, q):
        if not q.is_empty():
            if q.head != q.tail:
                data = q.peek()
                q.dequeue()
                self.reverse_queue(q)  # recursion
                q.enqueue(data)
                return q
            else:
                data = q.peek()
                q.dequeue()
                q.enqueue(data)
                return q
        return Queue(q.name)

    def valid_move(self, a, b):
        if not a.len():
            a.enqueue(b.dequeue())
        elif not b.len():
            if a.len() == self.number_of_discs:
                d = self.reverse_queue(a)
            else:
                d = a
            b.enqueue(d.dequeue())
        elif a.peek() > b.peek():
            e = b
            a = self.reverse_queue(a)
            a.enqueue(e.peek())
            self.reverse_queue(a)
            b.dequeue()
        else:
            b = self.reverse_queue(b)
            b.enqueue(a.dequeue())
            self.reverse_queue(b)

    def hanoi(self, n):
        if n % 2 == 0:
            self.B, self.C = self.C, self.B
        move = 2 ** n
        for i in range(1, move):
            if i % 3 == 1:
                self.valid_move(self.A, self.C)
            if i % 3 == 2:
                self.valid_move(self.A, self.B)
            if i % 3 == 0:
                self.valid_move(self.B, self.C)

            # Start formatting output.
            tower_a, tower_b, tower_c = self.A, self.B, self.C
            if n % 2 == 0:
                tower_b, tower_c = self.C, self.B
            for j in [tower_a, tower_b, tower_c]:
                print("\n    |", j.name, "|", end=" ")
                current = j.head
                while current:
                    print(current, "|", end=" ")
                    current = current.next
            print()
            # End formatting output.

        print("\nMove needed is: " + str(move - 1))

        
 ######The comparative Analysis###################
        
elements1 = list()    
elements2 = list()
elements3 = list()
times_queue = list()  
times_stack_I = list()  
times_stack_R = list()

for num_of_disks in range(1,12): 
    ####Queue
    time_start_q = time.process_time()
    tower = QueueTower(num_of_disks)
    tower.hanoi(num_of_disks)
    time_end_q = time.process_time()  
    total_time_q = time_end_q - time_start_q 

    print("Number of disks = ", num_of_disks, "Time spent" , + total_time_q, "sec")

    elements1.append(num_of_disks)
    times_queue.append(total_time_q)
    
    #####Stack 
    #RECURSIVE
    time_start_SR = time.process_time()
    RecursiveHanoi(num_of_disks, 'A', 'C', 'B')
    # tohIterative(num_of_disks, src, aux, dest)
    time_end_SR = time.process_time()  
    total_time_stack_R = time_end_SR - time_start_SR 

    print("Number of disks = ", num_of_disks, "Time spent" , + total_time_stack_R, "sec")

    elements2.append(num_of_disks)
    times_stack_R.append(total_time_stack_R)  
    
    #####Stack 
    #ITERATIVE
    time_start_SI = time.process_time()
    tohIterative(num_of_disks, src, aux, dest)
    time_end_SI = time.process_time()  
    total_time_stack_I = time_end_SI - time_start_SI 

    print("Number of disks = ", num_of_disks, "Time spent" , + total_time_stack_I, "sec")

    elements3.append(num_of_disks)
    times_stack_I.append(total_time_stack_I) 
    
plot.xlabel('Number of disks used')
plot.xscale("linear")
plot.ylabel('Time spent by the data structure')
plot.plot(elements1, times_queue, color='red', label='Queue Structure')
plot.plot(elements2, times_stack_I, color='blue', label='Stack Structure (Iterative Method)')
plot.plot(elements3, times_stack_R, color='green', label='Stack Structure (Recursive Method)')
plot.grid()
plot.legend()
plot.show()

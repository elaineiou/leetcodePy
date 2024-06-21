# heapq: https://www.geeksforgeeks.org/heap-and-priority-queue-using-heapq-module-in-python/
# customize sorting https://www.geeksforgeeks.org/heapq-with-custom-predicate-in-python/
# import required module
import heapq as pq

# class definition
class Employee:
	def __init__(self, n, yos):
		self.name = n
		self.yos = yos

    # override the comparison operator
    # __lt__ magic method:  https://www.geeksforgeeks.org/python-__lt__-magic-method/
	def __lt__(self, next):
		# return self.yos < next.yos # '<' operator: min heap
	    return self.yos > next.yos # '>': max heap


# creating objects
e1 = Employee('Anish',  3)
e2 = Employee('kathy', 2)
e3 = Employee('Rina',  5)
e4 = Employee('Vinay',  1)

# list of employee objects
emp = [e1, e2, e3, e4]

# converting to min-heap
# based on yos
pq.heapify(emp)

# printing the results
while emp:
	print(pq.heappop(emp).yos)

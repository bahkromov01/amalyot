# arr = [10,20,30,40,50,60,34,19,154,32]
#
# arr.sort()
#
#
# def binary_search(arr, target):
#     low, high = 0, len(arr) - 1
#
#     while low < high:
#         mid = (low + high) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return False
#
#
# print(binary_search(arr, 34))



# Class Stack
# append
# pop
#  list
from typing import Any

# Stack => push , pop , peek , is_empty,size
# class Stack:
#     def __init__(self):
#         self.stack = []
#
#     def is_empty(self) -> bool:
#         return len(self.stack) == 0
#
#     def push(self, item: Any) -> None:
#         self.stack.append(item)
#
#     def pop(self):
#         if not self.is_empty():
#             self.stack.pop()
#             return
#         raise Exception('Stack is empty')
#
#     def peek(self) -> Any:
#         if not self.is_empty():
#             return self.stack[-1]
#         raise Exception('Stack is empty')
#
#     def size(self) -> int:
#         return len(self.stack)
#
#
# # stack = Stack()
# # stack.push('john')
# # stack.push('anna')
# # stack.push('mike')
# # stack.pop()
# # stack.pop()
# # stack.pop()
# # stack.pop()
# # print(stack.is_empty())
#
#
# from collections import deque
#
#
# # arr = deque()
#
# # arr.appendleft(10)
# # arr.appendleft(20)
# # arr.appendleft(30)
# # print(arr)
# # Queue => dequeue , enqueue
#
# class Queue:
#     def __init__(self):
#         self.queue = deque()
#
#     def enqueue(self, item):
#         self.queue.append(item)
#
#     def dequeue(self):
#         if not self.is_empty():
#             self.queue.popleft()
#             return
#         raise Exception('Stack is empty')
#
#     def is_empty(self):
#         return len(self.queue) == 0
#
#     def peek(self):
#         if not self.is_empty():
#             return self.queue[0]
#         raise Exception('Stack is empty')
#
#     def size(self):
#         return len(self.queue)
#
#
# queue = Queue()
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
# queue.enqueue(4)
# queue.dequeue()
# queue.dequeue()
# print(queue.is_empty())
#


# class Stack:
#     def __init__(self):
#         self.stack = []
#
#     def push(self, item):
#         self.stack.append(item)
#
#     def pop(self):
#         if len(self.stack) > 0:
#             return self.stack.pop()
#         else:
#             return None
#
#     def peek(self):
#         if len(self.stack) > 0:
#             return self.stack[-1]
#         else:
#             return None
#
#     def is_empty(self):
#         return len(self.stack) == 0
#
#     def size(self):
#         return len(self.stack)
#
#
# stack = Stack()
#
# stack.push(10)
# stack.push(20)
# stack.push(30)
# print(stack.pop())
# print(stack.peek())


# class Queue:
#     def __init__(self):
#         self.queue = []
#
#     def enqueue(self, item):
#         self.queue.append(item)
#
#     def dequeue(self):
#         if len(self.queue) > 0:
#             return self.queue.pop(0)
#         else:
#             return None
#
#     def is_empty(self):
#         return len(self.queue) == 0
#
#     def size(self):
#         return len(self.queue)
#
#
# queue = Queue()
#
# queue.enqueue(10)
# queue.enqueue(20)
# queue.enqueue(30)
# print(queue.dequeue())
# print(queue.size())


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             return
#         last_node = self.head
#         while last_node.next:
#             last_node = last_node.next
#         last_node.next = new_node
#
#     def print_list(self):
#         current_node = self.head
#         while current_node:
#             print(current_node.data)
#             current_node = current_node.next
#
#
# llist = LinkedList()
#
# llist.append(1)
# llist.append(2)
# llist.append(3)
# llist.print_list()
#



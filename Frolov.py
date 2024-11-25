import math

class MemoryManager:
    def __init__(self):
        self.memory = 0

    def add(self, value):
        self.memory += value

    def clear(self):
        self.memory = 0

# Экземпляр для управления памятью
memory_manager = MemoryManager()

def square_root(a):
    if a < 0:
        return "Error: Negative input"
    return math.sqrt(a)

def floor_value(a):
    return math.floor(a)

def ceil_value(a):
    return math.ceil(a)

def memory_add(value):
    memory_manager.add(value)

def memory_clear():
    memory_manager.clear()

def get_memory():
    return memory_manager.memory


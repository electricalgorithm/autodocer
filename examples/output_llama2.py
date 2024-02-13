markdown
# Importing necessary libraries
import math
import random

# Functions for basic arithmetic operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def power(base, exponent):
    return base ** exponent

def sqrt(num):
    return math.sqrt(num)

# Classes for geometric shapes
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_origin(self):
        return math.sqrt(self.x**2 + self.y**2)

    def distance_to_point(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def circumference(self):
        return 2 * math.pi * self.radius

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Function for rolling dice
def roll_dice(num_dice, num_faces):
    return sum(random.randint(1, num_faces) for _ in range(num_dice))

# Function for generating passwords
def generate_password(length=8):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()'
    return ''.join(random.choice(characters) for _ in range(length))

# Function for checking if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

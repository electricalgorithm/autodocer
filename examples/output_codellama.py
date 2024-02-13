python
import math
import random

def add(a, b):
    """Add two numbers together.
    
    Args:
        a (int): The first number.
        b (int): The second number.
    
    Returns:
        int: The sum of `a` and `b`.
    """
    return a + b

def subtract(a, b):
    """Subtract one number from another.
    
    Args:
        a (int): The first number.
        b (int): The second number.
    
    Returns:
        int: The difference between `a` and `b`.
    """
    return a - b

def multiply(a, b):
    """Multiply two numbers together.
    
    Args:
        a (int): The first number.
        b (int): The second number.
    
    Returns:
        int: The product of `a` and `b`.
    """
    return a * b

def divide(a, b):
    """Divide one number by another.
    
    Args:
        a (int): The first number.
        b (int): The second number.
    
    Returns:
        float: The result of dividing `a` by `b`.
    """
    return a / b

def power(base, exponent):
    """Raise a number to the power of another number.
    
    Args:
        base (int): The number to be raised.
        exponent (int): The power to which `base` is raised.
    
    Returns:
        int: The result of raising `base` to the power of `exponent`.
    """
    return base ** exponent

def sqrt(num):
    """Return the square root of a number.
    
    Args:
        num (float): The number whose square root is to be found.
    
    Returns:
        float: The square root of `num`.
    """
    return math.sqrt(num)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_origin(self):
        """Return the distance between a point and the origin.
        
        Args:
            self (Point): A Point object.
        
        Returns:
            float: The distance between `self` and the origin.
        """
        return math.sqrt(self.x**2 + self.y**2)

    def distance_to_point(self, other):
        """Return the distance between two points.
        
        Args:
            self (Point): A Point object.
            other (Point): Another Point object.
        
        Returns:
            float: The distance between `self` and `other`.
        """
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def area(self):
        """Return the area of a circle.
        
        Args:
            self (Circle): A Circle object.
        
        Returns:
            float: The area of `self`.
        """
        return math.pi * self.radius**2

    def circumference(self):
        """Return the circumference of a circle.
        
        Args:
            self (Circle): A Circle object.
        
        Returns:
            float: The circumference of `self`.
        """
        return 2 * math.pi * self.radius

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Return the area of a rectangle.
        
        Args:
            self (Rectangle): A Rectangle object.
        
        Returns:
            float: The area of `self`.
        """
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of a rectangle.
        
        Args:
            self (Rectangle): A Rectangle object.
        
        Returns:
            float: The perimeter of `self`.
        """
        return 2 * (self.width + self.height)

def roll_dice(num_dice, num_faces):
    """Simulate rolling a number of dice with a certain number of faces.
    
    Args:
        num_dice (int): The number of dice to roll.
        num_faces (int): The number of faces on each die.
    
    Returns:
        int: The sum of the rolls.
    """
    return sum(random.randint(1, num_faces) for _ in range(num_dice))

def generate_password(length=8):
    """Generate a random password with a certain length.
    
    Args:
        length (int, optional): The desired length of the password. Defaults to 8.
    
    Returns:
        str: A random password string.
    """
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()'
    return ''.join(random.choice(characters) for _ in range(length))

def is_prime(n):
    """Determine whether a number is prime or not.
    
    Args:
        n (int): A positive integer to be tested for primality.
    
    Returns:
        bool: True if `n` is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


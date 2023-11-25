
# Problem 1

def is_even():
    x = int(input("enter a number: "))
    if x % 2 == 0:
        return True
    else:
        return False
    
    
# Problem 2

def calculate_grade(score):
    if score >= 90:
        print('A')
    elif score >= 80:
        print('B')
    elif score >= 70:
        print('C')
    elif score >= 60:
        print('D')
    else:
        print('F')
    

# Problem 3

def calculate_area():
    length = int(input("Enter the length of the rectangle: "))
    width = int(input("Enter the width of the rectangle: "))
    area = length * width
    print("area of rectangle is ", area)
    

# Problem 4

def is_triangle(a, b, c):
    if (a+b)>c and (a+c)>b and (b+c)>a:
        return True
    else:
        return False
    

# Problem 5

def max_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
    

#  Bonus

def reverse_string():
    word = input("enter a word: ")
    reverse_word = word[::-1]
    print(reverse_word)
    

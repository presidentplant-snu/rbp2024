def main():
    print("Let's implement division. Type two numbers for x and y")
    
    x = int(input("x > "))
    y = int(input("y > "))
    
    if y != 0:
        print("%d / %d = %0.3f" % (x, y, divide(x,y)))
    
def add(a, b):
    return a + b
    
def divide(a,b):
    if b != 0:
        return a/b
    else:
        print("Error: cannot divide by zero.")

if __name__ == "__main__":
    main()


# main.py
from utils import square, cube, is_even

def main():
    while True:
        num = input("Enter a number (or any letter to EXIT): ")
        if not num.isdigit():
            print("EXIT program.")
            break
        num = int(num)
        print(f"Square: {square(num)}")
        print(f"Cube: {cube(num)}")
        print(f"Is even? {is_even(num)}")

if __name__ == "__main__":
    main()
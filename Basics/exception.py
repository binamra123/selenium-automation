try:
    print("Enter a number")
    x = int(input())
    print("Enter another number")
    y = int(input())
    print(x/y)

except Exception as e:
    print(e)

finally:
    print("Always executed")


try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1/num
    print(reciprocal)


try:
    num_str = input("Please enter a number: ")

    if num_str.isdigit():
        num = int(num_str)
        
        if num != 0:
            result = 10 / num
            print("Result of division:", result)
        else:
            print("Error: Cannot divide by zero!")
    else:
        print("Error: Please enter a valid number!")

except Exception as e:
    print("e")

finally:
    print("Finally is always executed")
    
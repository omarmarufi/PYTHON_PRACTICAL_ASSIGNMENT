def recur_factorial_recursive(num):
    if num < 0:
        raise ValueError(" Negative values are not allowe")
    
    elif num < 2:
        return 1

    else:
        return num * recur_factorial_recursive(num - 1)
if __name__ == '__main__':
    n = int(input("Enter a number: "))
    print("Factorial is _-_-_ ", recur_factorial_recursive(n))
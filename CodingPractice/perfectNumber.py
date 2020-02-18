import sys

def perfectNumber(num: int) -> bool:
    sum: int = 1
    end_range: int = num
    n = 2

    while n < end_range:
        if num % n == 0:
            end_range = num // n
            sum += (n + end_range)

        if sum > num:
            break

        n += 1
    
    return True if sum == num else False

if __name__ == "__main__":
    num = int(sys.argv[1].strip())

    print(perfectNumber(num))
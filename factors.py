import sys

# Function to find two factors of a number n
def factorize(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return i, n // i
    return n, 1

if len(sys.argv) != 2:
    print("Usage: factors <file>")
    sys.exit(1)

input_file = sys.argv[1]

try:
    with open(input_file, "r") as file:
        output_file = open("output.txt", "w")
        for line in file:
            n = int(line.strip())
            p, q = factorize(n)
            output_file.write(f"{n}={p}*{q}\n")
        output_file.close()
except FileNotFoundError:
    print(f"File '{input_file}' not found.")
    sys.exit(1)
except ValueError:
    print("Invalid input. Please make sure the file contains valid natural numbers greater than 1.")
    sys.exit(1)
except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)


# task1
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line, end='') 
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
read_file('sample.txt')


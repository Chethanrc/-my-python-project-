#task 2
def write_to_file(filename):
    try:
        user_input = input("Enter text to write to the file: ")
        with open(filename, 'w') as file:
            file.write(user_input + '\n') 
            print("Data sucessfully writen to output.txt/n")    
        append_input = input("\nEnter additional text to append: ")
        with open(filename, 'a') as file:
            file.write(append_input + '\n')
            print("Data is sucessfully appended")
        print("\nFinal content of output.txt:")
        with open(filename, 'r') as file:
            for line in file:
                print(line, end='')   
    except IOError as e:
        print(f"An error occurred while handling the file: {e}")
write_to_file('output.txt')

try:
    with open('input.txt', 'r') as input_file:
        content = input_file.read()
    
    word_count = len(content.split())
    
    uppercase_content = content.upper()
    
    with open('output.txt', 'w') as output_file:
        output_file.write(f"WORD COUNT: {word_count}\n\n")
        output_file.write(uppercase_content)
    
    print("File processed successfully! Results saved to output.txt")
    print(f"Total words counted: {word_count}")

except FileNotFoundError:
    print("Error: input.txt not found. Please create it first.")
except Exception as e:
    print(f"An error occurred: {e}")
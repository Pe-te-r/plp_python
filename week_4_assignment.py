def process_file():
    try:
        filename = input("Enter the filename to process: ").strip()
        
        with open(filename, 'r') as input_file:
            content = input_file.read()
            line_count = len(content.splitlines())
            modified_content = content.upper()
        
        output_filename = f"modified_{filename}"
        with open(output_filename, 'w') as output_file:
            output_file.write(f"LINE COUNT: {line_count}\n\n")
            output_file.write(modified_content)
        
        print(f"\n✅ Success! Processed file saved as '{output_filename}'")
        print(f"• Original lines: {line_count}")
        print(f"• Modified content is in uppercase")
    
    except FileNotFoundError:
        print("\n❌ Error: The file was not found. Please check the filename.")
    except PermissionError:
        print("\n❌ Error: Permission denied. You can't read this file.")
    except UnicodeDecodeError:
        print("\n❌ Error: Couldn't decode the file (might be binary).")
    except Exception as e:
        print(f"\n❌ Unexpected error: {str(e)}")
    finally:
        print("\nOperation completed.") 


if __name__ == "__main__":
    print("=== File Processing Tool ===")
    process_file()
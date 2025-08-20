from typing import Optional

def modify_file_content(content: str) -> str:
    """
    Modify the file content by converting it to uppercase.
    
    Args:
        content (str): The original content read from the file.
    
    Returns:
        str: The modified content.
    """
    return content.upper()

def read_and_write_file(input_filename: str) -> Optional[str]:
    """
    Read the input file, modify its content, and write to a new file.
    Handles errors if the file can't be read.
    
    Args:
        input_filename (str): The name of the file to read.
    
    Returns:
        Optional[str]: The name of the output file if successful, None otherwise.
    """
    output_filename = f"modified_{input_filename}"
    
    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        modified_content = modify_file_content(content)
        
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        return output_filename
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist. Please check the filename and try again.")
    except PermissionError:
        print(f"Error: Permission denied when trying to read '{input_filename}'. Ensure you have read access.")
    except IOError as e:
        print(f"Error: An I/O error occurred while handling '{input_filename}': {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    
    return None

if __name__ == "__main__":
    input_filename = input("Enter the filename to read (e.g., example.txt): ").strip()
    
    if not input_filename:
        print("Error: No filename provided. Please enter a valid filename.")
    else:
        output_file = read_and_write_file(input_filename)
        if output_file:
            print(f"Success: Modified file written to '{output_file}'.")
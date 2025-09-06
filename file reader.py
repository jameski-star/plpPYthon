def modify_content(content):
    """
    Modify the content as needed.
    Example: Convert all text to uppercase.
    """
    return content.upper()

def read_and_write_file():
    # Ask the user for the input filename
    input_filename = input("Enter the filename to read: ")

    try:
        # Attempt to read the file
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Modify the content
        modified_content = modify_content(content)

        # Create a new filename for the output
        output_filename = "modified_" + input_filename

        # Write the modified content to the new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"File has been successfully modified and saved as '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except IOError:
        print(f"Error: Could not read or write to the file '{input_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
read_and_write_file()

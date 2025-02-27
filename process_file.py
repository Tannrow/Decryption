# Open the file in read mode
with open("/home/codespace/Decryption/0001193125-11-328935.txt", "r") as file:
    content = file.readlines()

# Process each line in the file
for line in content:
    # Assuming you are parsing the line here
    # Strip leading and trailing whitespaces
    line = line.strip()

    # Process the line to handle the integer conversion
    # Example: If the line has a number with leading zeros, handle it appropriately
    if line.startswith("<SEC-DOCUMENT>"):
        # Extract the part that could be a number
        parts = line.split(":")
        doc_info = parts[0].strip()
        date_info = parts[1].strip()

        # Check if date_info has leading zeros and convert it properly
        if date_info.startswith("0"):
            # Remove leading zeros
            date_info = str(int(date_info))

        # Reconstruct the line
        corrected_line = f"{doc_info} : {date_info}"
        print(corrected_line)  # Or handle the corrected line further as needed

# Continue with the rest of your script logic

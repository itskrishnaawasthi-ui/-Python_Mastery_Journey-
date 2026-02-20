with open("message", "r") as f:
    # Iterating directly over 'f' reads the file line by line
    word = "powerfully"
    line_no = 1
    found = False
    for line in f:
        if word in line:
            print(f"Yes, we found it in line no: {line_no}")
            found = True
        line_no += 1

        if not found:
           print("Word not found in the file.")
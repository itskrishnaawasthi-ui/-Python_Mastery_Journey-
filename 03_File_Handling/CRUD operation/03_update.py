# Update Example: Replacing text
with open("user_data", "w") as f:
    f.write("Are you fine if yes then stand up")


with open("user_data", "r") as f:
    data = f.read()
    print("Original data\n",data)
    new_data = data.replace("Are", "Ram") # Logic to change content

with open("user_data", "w") as f:
    f.write(new_data) # Saving the updated version

with open("user_data", "r") as f:
    data = f.read()
    print("After updata\n",data)

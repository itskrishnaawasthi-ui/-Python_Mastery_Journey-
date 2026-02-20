import csv

# Writing to the file (Fixed filename typo and added newline='')
with open("detail.csv", "w", newline='') as f:
    size = int(input("Enter the number of students: "))
    fobj = csv.writer(f)
    fobj.writerow(["Rollno", "Name", "Total_Marks"])
    for s in range(size):
        Rollno = int(input('Enter rollno: '))
        Name = input("Enter name: ")
        Total_Marks = float(input("Enter total marks: "))
        record = [Rollno, Name, Total_Marks]
        fobj.writerow(record)

# Reading from the file (Fixed the print statement)
print("\n--- Current Records in File ---")
with open("detail.csv", "r") as f:
    fobj = csv.reader(f)
    for row in fobj:
        print(row)
import csv
with open('customers.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["First Name", "Last Name", "Email","Address","Purchased Items","Total Spent"])
    writer.writerow(["Jones", "Sharma", "jones1@gmail.com", "Durgapura", 5, 1000])
    writer.writerow(["Jack", "Gupta", "jackg@gmail.com", "Malviya Nagar", 2, 450])
    writer.writerow(["Jai", "Garg", "jaig@gmail.com", "Pratap Nagar", 4, 2000])
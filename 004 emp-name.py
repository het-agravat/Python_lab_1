# Write a program to add employee names in a list EMPNAME and perform add,remove and append methods.

EMPNAME = []

def add_employee(name):
    EMPNAME.append(name)
    print(f"Added {name} to EMPNAME.")
    
def remove_employee(name):
    if name in EMPNAME:
        EMPNAME.remove(name)
        print(f"Removed {name} from EMPNAME.")
    else:
        print(f"{name} is not found in EMPNAME.")

def append_employee(name):
    EMPNAME.append(name)
    print(f"Appended {name} to EMPNAME.")

add_employee('Het')
add_employee('Yash')
add_employee('Rushap')

print("Current EMPNAME list:", EMPNAME)

remove_employee('Rushap')

print("Current EMPNAME list:", EMPNAME)

append_employee('Mohit')

print("Current EMPNAME list:", EMPNAME)

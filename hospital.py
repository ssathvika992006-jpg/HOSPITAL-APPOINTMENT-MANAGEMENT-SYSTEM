# Hospital Appointment Management System

def check_doctor(available):
    if available:
        return "Appointment Confirmed"
    else:
        return "Doctor Not Available"

# Main Program
print("=== Hospital Appointment Management System ===")

patient = input("Enter Patient Name: ")
doctor = input("Enter Doctor Name: ")

status = input("Is the doctor available? (yes/no): ").lower()

if status == "yes":
    result = check_doctor(True)
else:
    result = check_doctor(False)

print("\nAppointment Details")
print("----------------------------")
print("Patient Name :", patient)
print("Doctor Name  :", doctor)
print("Status       :", result)
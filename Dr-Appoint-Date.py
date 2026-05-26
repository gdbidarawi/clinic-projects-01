# ============================================
# DOCTOR APPOINTMENT MODULE
# Add this module into your existing
# Clinic Management System
# ============================================

from datetime import datetime

# Store appointments
appointments = []


# ============================================
# ADD APPOINTMENT
# ============================================
def add_appointment():

    print("\n========== ADD APPOINTMENT ==========")

    patient_id = input("Enter Patient ID: ")
    patient_name = input("Enter Patient Name: ")
    doctor_name = input("Enter Doctor Name: ")

    appointment_date = input("Enter Appointment Date (YYYY-MM-DD): ")
    appointment_time = input("Enter Appointment Time (HH:MM): ")

    reason = input("Enter Reason for Visit: ")

    try:
        # Validate date and time
        datetime.strptime(appointment_date, "%Y-%m-%d")
        datetime.strptime(appointment_time, "%H:%M")

        appointment = {
            "patient_id": patient_id,
            "patient_name": patient_name,
            "doctor_name": doctor_name,
            "date": appointment_date,
            "time": appointment_time,
            "reason": reason,
            "status": "Scheduled"
        }

        appointments.append(appointment)

        print("\nAppointment Added Successfully!")

    except ValueError:
        print("\nInvalid Date or Time Format!")


# ============================================
# VIEW ALL APPOINTMENTS
# ============================================
def view_appointments():

    print("\n========== ALL APPOINTMENTS ==========")

    if len(appointments) == 0:
        print("No appointments found.")
        return

    for index, appointment in enumerate(appointments, start=1):

        print(f"""
Appointment #{index}
--------------------------------
Patient ID      : {appointment['patient_id']}
Patient Name    : {appointment['patient_name']}
Doctor Name     : {appointment['doctor_name']}
Appointment Date: {appointment['date']}
Appointment Time: {appointment['time']}
Reason          : {appointment['reason']}
Status          : {appointment['status']}
""")


# ============================================
# SEARCH APPOINTMENT
# ============================================
def search_appointment():

    print("\n========== SEARCH APPOINTMENT ==========")

    patient_name = input("Enter Patient Name: ")

    found = False

    for appointment in appointments:

        if appointment["patient_name"].lower() == patient_name.lower():

            found = True

            print(f"""
--------------------------------
Patient ID      : {appointment['patient_id']}
Patient Name    : {appointment['patient_name']}
Doctor Name     : {appointment['doctor_name']}
Appointment Date: {appointment['date']}
Appointment Time: {appointment['time']}
Reason          : {appointment['reason']}
Status          : {appointment['status']}
""")

    if not found:
        print("Appointment not found.")


# ============================================
# UPDATE APPOINTMENT STATUS
# ============================================
def update_appointment_status():

    print("\n========== UPDATE STATUS ==========")

    patient_name = input("Enter Patient Name: ")

    for appointment in appointments:

        if appointment["patient_name"].lower() == patient_name.lower():

            print("\n1. Completed")
            print("2. Cancelled")
            print("3. Pending")

            choice = input("Select Status: ")

            if choice == "1":
                appointment["status"] = "Completed"

            elif choice == "2":
                appointment["status"] = "Cancelled"

            elif choice == "3":
                appointment["status"] = "Pending"

            else:
                print("Invalid Choice")
                return

            print("Appointment Status Updated!")
            return

    print("Appointment not found.")

# DELETE APPOINTMENT
def delete_appointment():

    print("\n DELETE APPOINTMENT ")

    patient_name = input("Enter Patient Name: ")

    for appointment in appointments:

        if appointment["patient_name"].lower() == patient_name.lower():

            appointments.remove(appointment)

            print("Appointment Deleted Successfully!")
            return

    print("Appointment not found.")

# APPOINTMENT MENU
def appointment_menu():

    while True:

        print("""
========== DOCTOR APPOINTMENT SYSTEM ==========
1. Add Appointment
2. View Appointments
3. Search Appointment
4. Update Appointment Status
5. Delete Appointment
6. Back to Main Menu
""")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_appointment()

        elif choice == "2":
            view_appointments()

        elif choice == "3":
            search_appointment()

        elif choice == "4":
            update_appointment_status()

        elif choice == "5":
            delete_appointment()

        elif choice == "6":
            break

        else:
            print("Invalid Choice!")



# CALL THIS FUNCTION FROM MAIN SYSTEM

appointment_menu()
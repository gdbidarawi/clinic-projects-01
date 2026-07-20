class RecoveryPatient:
    def __init__(self, patient_id, name, disease, recovery_status):
        self.patient_id = patient_id
        self.name = name
        self.disease = disease
        self.recovery_status = recovery_status

    def display(self):
        print(f"ID: {self.patient_id}")
        print(f"Name: {self.name}")
        print(f"Disease: {self.disease}")
        print(f"Recovery Status: {self.recovery_status}")
        print("-" * 30)


# List to store recovery patients
recovery_patients = []


# Function to add a recovery patient
def add_patient():
    patient_id = input("Enter Patient ID: ")
    name = input("Enter Patient Name: ")
    disease = input("Enter Disease: ")
    recovery_status = input("Enter Recovery Status (Recovering/Recovered): ")

    patient = RecoveryPatient(patient_id, name, disease, recovery_status)
    recovery_patients.append(patient)

    print("Recovery patient added successfully!\n")


# Function to display all recovery patients
def display_patients():
    if not recovery_patients:
        print("No recovery patients found.\n")
        return

    print("\n--- Recovery Patients List ---")
    for patient in recovery_patients:
        patient.display()


# Function to update recovery status
def update_recovery_status():
    patient_id = input("Enter Patient ID to update: ")

    for patient in recovery_patients:
        if patient.patient_id == patient_id:
            new_status = input("Enter New Recovery Status: ")
            patient.recovery_status = new_status
            print("Recovery status updated successfully!\n")
            return

    print("Patient not found.\n")


# Main menu
while True:
    print("\n=== Hospital Recovery Patient Management ===")
    print("1. Add Recovery Patient")
    print("2. Display Recovery Patients")
    print("3. Update Recovery Status")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_patient()
    elif choice == "2":
        display_patients()
    elif choice == "3":
        update_recovery_status()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.")
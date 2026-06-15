class Patient:
    def __init__(self, patient_id, name, disease):
        self.patient_id = patient_id
        self.name = name
        self.disease = disease
        self.status = "Admitted"

    def discharge(self):
        self.status = "Healthy and Discharged"
        print(f"Patient {self.name} has been discharged successfully.")

# Example
patient1 = Patient("P001", "John Doe", "Malaria")
patient1.discharge()

print("Status:", patient1.status)
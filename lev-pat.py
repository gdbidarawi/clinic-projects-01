class Patient:
    def __init__(self, name, age, fever, oxygen, pain_level):
        self.name = name
        self.age = age
        self.fever = fever
        self.oxygen = oxygen
        self.pain_level = pain_level

    def treatment_level(self):
        # Determine treatment priority
        if self.oxygen < 90 or self.pain_level >= 9:
            return "Critical - Immediate Emergency Treatment"
        elif self.fever >= 39 or self.pain_level >= 7:
            return "Urgent - Doctor Attention Needed"
        elif self.fever >= 37.5 or self.pain_level >= 4:
            return "Moderate - Standard Treatment"
        else:
            return "Mild - Basic Care"

    def display_info(self):
        print("\n--- Patient Information ---")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Fever: {self.fever} °C")
        print(f"Oxygen Level: {self.oxygen}%")
        print(f"Pain Level: {self.pain_level}/10")
        print(f"Treatment Level: {self.treatment_level()}")

# Input patient details
name = input("Enter patient name: ")
age = int(input("Enter patient age: "))
fever = float(input("Enter body temperature (°C): "))
oxygen = int(input("Enter oxygen level (%): "))
pain_level = int(input("Enter pain level (0-10): "))

# Create patient object
patient = Patient(name, age, fever, oxygen, pain_level)

# Display patient information and treatment level
patient.display_info()
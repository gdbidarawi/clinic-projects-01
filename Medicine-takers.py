class Drug:
    def __init__(self, drug_id, name, dosage, frequency):
        self.drug_id = drug_id
        self.name = name
        self.dosage = dosage
        self.frequency = frequency

    def display(self):
        print(f"Drug ID: {self.drug_id}")
        print(f"Drug Name: {self.name}")
        print(f"Dosage: {self.dosage}")
        print(f"Frequency: {self.frequency}")
        print("-" * 30)


class DrugManagement:
    def __init__(self):
        self.drugs = []

    def add_drug(self, drug):
        self.drugs.append(drug)
        print("Drug added successfully!")

    def view_drugs(self):
        if not self.drugs:
            print("No drugs available.")
            return

        print("\nDrug List")
        print("=" * 30)
        for drug in self.drugs:
            drug.display()

    def search_drug(self, drug_id):
        for drug in self.drugs:
            if drug.drug_id == drug_id:
                drug.display()
                return
        print("Drug not found.")

    def delete_drug(self, drug_id):
        for drug in self.drugs:
            if drug.drug_id == drug_id:
                self.drugs.remove(drug)
                print("Drug deleted successfully!")
                return
        print("Drug not found.")


# Main Program
manager = DrugManagement()

while True:
    print("\n=== Hospital Drug Management ===")
    print("1. Add Drug")
    print("2. View Drugs")
    print("3. Search Drug")
    print("4. Delete Drug")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        drug_id = input("Drug ID: ")
        name = input("Drug Name: ")
        dosage = input("Dosage (e.g., 500mg): ")
        frequency = input("Frequency (e.g., Twice Daily): ")

        drug = Drug(drug_id, name, dosage, frequency)
        manager.add_drug(drug)

    elif choice == "2":
        manager.view_drugs()

    elif choice == "3":
        drug_id = input("Enter Drug ID: ")
        manager.search_drug(drug_id)

    elif choice == "4":
        drug_id = input("Enter Drug ID: ")
        manager.delete_drug(drug_id)

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
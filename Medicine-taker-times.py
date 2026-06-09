class Drug:
    def __init__(self, drug_id, name, dosage, take_time):
        self.drug_id = drug_id
        self.name = name
        self.dosage = dosage
        self.take_time = take_time

    def display(self):
        print(f"Drug ID: {self.drug_id}")
        print(f"Drug Name: {self.name}")
        print(f"Dosage: {self.dosage}")
        print(f"Take At: {self.take_time}")
        print("-" * 30)


drug1 = Drug(
    drug_id="D001",
    name="Paracetamol",
    dosage="500mg",
    take_time="08:00 AM"
)

drug1.display()
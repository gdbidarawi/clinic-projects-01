import sqlite3
from datetime import date

DATABASE = "clinic.db"


def connect_db():
    return sqlite3.connect(DATABASE)


def generate_report():

    conn = connect_db()
    cursor = conn.cursor()

    try:

        # Total Patients
        cursor.execute("SELECT COUNT(*) FROM patients")
        total_patients = cursor.fetchone()[0]

        # Total Doctors
        cursor.execute("SELECT COUNT(*) FROM doctors")
        total_doctors = cursor.fetchone()[0]

        # Total Appointments
        cursor.execute("SELECT COUNT(*) FROM appointments")
        total_appointments = cursor.fetchone()[0]

        # Total Inventory Items
        cursor.execute("SELECT COUNT(*) FROM inventory")
        total_inventory = cursor.fetchone()[0]

        # Expired Medicines
        today = str(date.today())

        cursor.execute("""
            SELECT COUNT(*)
            FROM inventory
            WHERE expiry_date < ?
        """, (today,))

        expired_items = cursor.fetchone()[0]

        print("\")
        print("      CLINIC REPORT")
        print(f"Total Patients      : {total_patients}")
        print(f"Total Doctors       : {total_doctors}")
        print(f"Total Appointments  : {total_appointments}")
        print(f"Inventory Items     : {total_inventory}")
        print(f"Expired Medicines   : {expired_items}")
        

    except Exception as e:
        print("Error:", e)

    finally:
        conn.close()


generate_report()
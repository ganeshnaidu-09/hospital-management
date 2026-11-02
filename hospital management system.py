class patient:
    def __init__(self, name, patient_id, age, gender, contact_number, disease, blood_group):
        self.name = name
        self.patient_id = patient_id
        self.age = age
        self.gender = gender
        self.contact_number = contact_number
        self.disease = disease
        self.blood_group = blood_group
    def display_patient_info(self):
        print("Patient Name:", self.name)
        print("Patient ID:", self.patient_id)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Contact Number:", self.contact_number)
        print("Disease:", self.disease)
        print("Blood Group:", self.blood_group)
patients = []
def add_patients():
    try:
        num_patients = int(input("Enter the number of patients to add: "))
        for _ in range(num_patients):
            name = input("Enter patient name: ")
            patient_id = input("Enter patient ID: ")
            age = int(input("Enter patient age: "))
            gender = input("Enter patient gender: ")
            contact_number = input("Enter contact number: ")
            disease = input("Enter disease: ")
            blood_group = input("Enter blood group: ")
            new_patient = patient(name, patient_id, age, gender, contact_number, disease, blood_group)
            patients.append(new_patient)
        print("Patients added successfully!")
    except ValueError:
        print("Invalid input. Please enter valid information for each patient.")
def display_all_patients():
    if not patients:
        print("No patients found.")
    else:
        for patient in patients:
            patient.display_patient_info()
            print("--------------------")
print(add_patients())
def search_patient_by_id(patient_id):
    for patient in patients:
        if patient.patient_id == patient_id:
            print("patient is found", patient.name)
        else:
            print("patient is not found")

print(search_patient_by_id("143")) 
class doctor:
    def __init__(self, name, doctor_id, specialization, contact_number):
            self.name = name
            self.doctor_id = doctor_id
            self.specialization = specialization
            self.contact_number = contact_number

    def display_doctor_info(self):
            print("Doctor Name:", self.name)
            print("Doctor ID:", self.doctor_id)
            print("Specialization:", self.specialization)
            print("Contact Number:", self.contact_number)

    def book_appointment(self, patient, doctor):
            print(f"Appointment booked for patient {patient.name} with Dr. {doctor.name}.")
    def __init__(self, name, doctor_id, specialization, contact_number):
        self.name = name
        self.doctor_id = doctor_id
        self.specialization = specialization
        self.contact_number = contact_number
    def display_doctor_info(self):
        print("Doctor Name:", self.name)
        print("Doctor ID:", self.doctor_id)
        print("Specialization:", self.specialization)
        print("Contact Number:", self.contact_number)
print(doctor("Dr. ganesh", "G0309", "Cardiologist", "123-456-7890").doctor_id,doctor("Dr. ganesh", "G0309", "Cardiologist", "123-456-7890").name)
def book_appointment(self, patient, doctor):
    print(f"Appointment booked for patient {patient.name} with Dr. {doctor.name}.")
date=input("Enter appointment date: ")
time=input("Enter appointment time: ")
print("appointment booked for patient with doctor on",date,"at",time)
print("appointment booked successfully")


consultation_fee = 500
medicine_fee = int(input("Enter medicine fee: "))
lab_test_fee = int(input("Enter lab test fee: "))

total_bill = consultation_fee + medicine_fee + lab_test_fee

if total_bill <= 10000:
    discount = total_bill * 0.10
elif total_bill <= 5000:
    discount = total_bill * 0.05
else:
    discount = 0

final_bill = total_bill - discount

print("Total bill:", total_bill)
print("Discount:", discount)
print("Final bill:", final_bill)

print("Hope you get well soon <3")
    
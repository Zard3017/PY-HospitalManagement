import abc
from abc import ABC, abstractmethod


#encapsulation of class Person
class Person(ABC):
    def __init__(self, name, age, address):
        self._name = name
        self._age = age
        self._address = address

    @property # property decorator to define getter method
    def name(self):
        return self._name

    @property # property decorator to define getter method
    def age(self):
        return self._age

    @property
    def address(self):
        return self._address
    @abstractmethod
    def display_details(self):
        pass


    #Inheritance from person class
class Doctor(Person):
    def __init__(self, name, age, address, specialization, years_of_experience):
        super().__init__(name, age, address) # calls constructor of parent class Person and passes arguments from parent class
        self._specialization = specialization
        self._years_of_experience = years_of_experience

    def display_details(self):
        print(f'Doctor Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Address: {self.address}')
        print(f'Specialization: {self._specialization}')
        print(f'Years of Experience: {self._years_of_experience}')

#test for output of doctor details        
"""
if __name__ == '__main__':

        doctor = Doctor("Dr. Alice Gitonga", 45, "Nairobi", "Cardiology", 15)
        print(doctor._specialization)  # Output: Cardiology
        print(doctor._years_of_experience)  # Output: 15

        doctor.display_details()
        """

#Inheritance of patient class from person super class
class Patient(Person):
    def __init__(self, name, age, address, medical_history):
        super().__init__(name, age, address)
        self._medical_history = medical_history

    def display_details(self):
        print(f'Patient Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Address: {self.address}')
        print(f'Medical History: {self._medical_history}')

#test for output of patient details
"""
if __name__ == '__main__':
    patient = Patient("Axel Witsel", 30, "123 Main St", "Asthma")
    patient.display_details()
"""


#Inheritance of staff class from person super class
class HospitalStaff(Person):
    def __init__(self, name, age, address, role):
        super().__init__(name, age, address)
        self._role = role

    def display_details(self):
        print(f'Staff Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Address: {self.address}')
        print(f'Role: {self._role}')

#test for output of staff details

class Hospital:
    def __init__(self): # creating instance for the 3 subclasses
        self._doctors = []
        self._patients = []
        self._staff = []

    def add_doctor(self, doctor): #defining method to add doctor
        self._doctors.append(doctor)

    def add_patient(self, patient): #defining method to add patient
        self._patients.append(patient)

    def add_staff(self, staff): #defining method to add staff
        self._staff.append(staff)

    def update_doctor(self, name):
        for doctor in self._doctors:
            if doctor.name == name:
                doctor._age = int(input("Enter new age: "))
                doctor._address = input("Enter new address: ")
                doctor._specialization = input("Enter new specialization: ")
                doctor._years_of_experience = int(input("Enter new years of experience: "))
                print("Doctor details updated.")
                return
        print("Doctor not found.")

    def update_patient(self, name):
        for patient in self._patients:
            if patient.name == name:
                patient._age = int(input("Enter new age: "))
                patient._address = input("Enter new address: ")
                patient._medical_history = input("Enter new medical history: ")
                print("Patient details updated.")
                return
        print("Patient not found.")

    def delete_doctor(self, name):
        for doctor in self._doctors:
            if doctor.name == name:
                self._doctors.remove(doctor)
                print("Doctor deleted.")
                return
        print("Doctor not found.")

    def delete_patient(self, name):
        for patient in self._patients:
            if patient.name == name:
                self._patients.remove(patient)
                print("Patient deleted.")
                return
        print("Patient not found.")




class Appointment:
    def __init__(self, patient, doctor, date, time):
        self._patient = patient
        self._doctor = doctor
        self._date = date
        self._time = time

    def display_details(self):
        print(f'Patient: {self._patient.name}')
        print(f'Doctor: {self._doctor.name}')
        print(f'Date: {self._date}')
        print(f'Time: {self._time}')

"""
# Assuming Doctor and Patient classes are defined and implemented
doctor = Doctor("Dr. Alice", 45, "456 Oak St", "Cardiology", 15)
patient = Patient("Phillip", 30, "123 Elm St", "Medical History Example")

# Create an Appointment instance
appointment = Appointment(patient, doctor, "2024-11-10", "10:00 AM")

# Display the appointment details
appointment.display_details()
"""


class Bill:
    def __init__(self, patient, amount, date):
        self._patient = patient
        self._amount = amount
        self._date = date

    def display_details(self):
        print(f'Patient: {self._patient.name}')
        print(f'Amount: {self._amount}')
        print(f'Date: {self._date}')


"""  # Assuming Patient class is defined and implemented
patient = Patient("Umaga", 28, "Kisumu", "Allergies")

# Create a Bill instance
bill = Bill(patient, 150.75, "2024-11-01")

# Display the bill details
bill.display_details()

"""

def main():
    hospital = Hospital()  # Create a Hospital instance

    while True:
        print("\nChoose an option:")
        print("1. Add Doctor")
        print("2. Add Patient")
        print("3. Update Doctor")
        print("4. Update Patient")
        print("5. Delete Doctor")
        print("6. Delete Patient")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Input for Doctor
            name = input("Enter doctor's name: ")
            age = int(input("Enter doctor's age: "))
            address = input("Enter doctor's address: ")
            specialization = input("Enter doctor's specialization: ")
            years_of_experience = int(input("Enter years of experience: "))

            doctor = Doctor(name, age, address, specialization, years_of_experience)
            hospital.add_doctor(doctor)  # Add doctor to hospital
            doctor.display_details()

        elif choice == "2":
            # Input for Patient
            name = input("Enter patient's name: ")
            age = int(input("Enter patient's age: "))
            address = input("Enter patient's address: ")
            medical_history = input("Enter patient's medical history: ")

            patient = Patient(name, age, address, medical_history)
            hospital.add_patient(patient)  # Add patient to hospital
            patient.display_details()

        elif choice == "3":
            name = input("Enter the name of the doctor to update: ")
            hospital.update_doctor(name)

        elif choice == "4":
            name = input("Enter the name of the patient to update: ")
            hospital.update_patient(name)

        elif choice == "5":
            name = input("Enter the name of the doctor to delete: ")
            hospital.delete_doctor(name)

        elif choice == "6":
            name = input("Enter the name of the patient to delete: ")
            hospital.delete_patient(name)

        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
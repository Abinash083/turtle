class Disease:
    def __init__(self, disease_name, medication, reason, present_disease=None):
        self.disease_name = disease_name
        self.medication = medication
        self.reason = reason
        self.present_disease = present_disease

class Goat:
    def __init__(self, parent_1, parent_2, animal_id, gender, diseases, weight, dob, status, goat_condition, location, child=None):
        self.parent_1 = parent_1
        self.parent_2 = parent_2
        self.animal_id = animal_id
        self.gender = gender
        self.diseases = diseases  # List of Disease objects
        self.weight = weight
        self.dob = dob
        self.status = status
        self.goat_condition = goat_condition
        self.location = location
        self.child = child

    def __str__(self):
        return f"Goat ID: {self.animal_id}, Gender: {self.gender}, DOB: {self.dob}, Status: {self.status}, Condition: {self.goat_condition}, Location: {self.location}"

# Usage
disease1 = Disease("Fever", "Antibiotics", "High temperature")
disease2 = Disease("Pneumonia", "Cough syrup", "Respiratory infection", present_disease="Cough")

goat1 = Goat("Parent1ID", "Parent2ID", "GoatID123", "Male", [disease1], 25, "2020-01-15", "Breeding", "Good improvement", "Barn")
goat2 = Goat("Parent3ID", "Parent4ID", "GoatID456", "Female", [disease2], 30, "2019-07-20", "Pregnant", "Under medication", "Pasture", child=goat1)

print(goat1)
print(goat2)

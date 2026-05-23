class Student:
    def __init__(self, full_name, section, spanish, english, social_studies, science):
        self.full_name = full_name
        self.section = section
        self.spanish = spanish
        self.english = english
        self.social_studies = social_studies
        self.science = science

    def calculate_average(self):
        total = self.spanish + self.english + self.social_studies + self.science
        return total / 4

    def to_dictionary(self):
        return {
            "full_name": self.full_name,
            "section": self.section,
            "spanish": self.spanish,
            "english": self.english,
            "social_studies": self.social_studies,
            "science": self.science
        }


SUBJECTS = {
    "spanish": "Español",
    "english": "Inglés",
    "social_studies": "Sociales",
    "science": "Ciencias"
}
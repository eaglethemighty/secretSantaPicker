import pandas as pd
from typing import List
from person import Person


class PeopleParser:
    path: str

    def __init__(self, excel_path):
        self.path = excel_path

    def parse_people(self) -> List[Person]:

        peopleInFile: List[Person] = []

        df = pd.DataFrame(pd.read_csv('peopleList.csv', delimiter=';'), columns=['name', 'email'])

        for index, row in df.iterrows():
            name = row['name']
            email = row['email']
            peopleInFile.append(Person(name, email))

        return peopleInFile

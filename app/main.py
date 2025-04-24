class Person:
    people = {}

    def __init__(
        self,
        name: str,
        age: int
    ) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_instance = []
    for person in people:
        person_data = Person(person["name"], person["age"])
        person_instance.append(person_data)

    for person in people:
        person_data = Person.people[person["name"]]
        if "wife" in person and person["wife"] is not None:
            person_data.wife = Person.people[person["wife"]]
        elif "husband" in person and person["husband"] is not None:
            person_data.husband = Person.people[person["husband"]]

    return person_instance

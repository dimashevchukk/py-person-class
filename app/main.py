class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    Person.people.clear()
    list_of_people: list[Person] = []

    for person in people:
        cur_person = Person(person["name"], person["age"])

        if wife := person.get("wife"):
            if wife in Person.people:
                cur_person.wife = Person.people[wife]
                cur_person.wife.husband = cur_person

        elif husband := person.get("husband"):
            if husband in Person.people:
                cur_person.husband = Person.people[husband]
                cur_person.husband.wife = cur_person

        list_of_people.append(cur_person)

    return list_of_people

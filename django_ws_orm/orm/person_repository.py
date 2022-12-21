from .person_exceptions import PersonException
from .models import Person


class person_repository:

    def __guard_is_not_empty(self, person):
        if person is None:
            raise ValueError('There was no any person')

    def get(self, person=None):
        if person is not None:
            try:
                result_person = Person.objects.get(id=person.id)
                return f'Id: {result_person.id}, name: {result_person.name}, age: {result_person.age}'
            except:
                raise PersonException(f'Person with id {person.id} not found')
        else:
            return [f'Id: {person["id"]}, name: {person["name"]}, age: {person["age"]}' for person in Person.objects.values()]

    def delete(self, person):
        self.__guard_is_not_empty(person)
        try:
            result_person = Person.objects.get(id=person.id)
            result_person.delete()
            return True
        except:
            raise PersonException(f'Person with id {person.id} not found')

    def create(self, person):
        self.__guard_is_not_empty(person)
        result_person = Person(name=person.name, age=person.age)
        result_person.save()
        return f'Current Person id is {result_person.id}'

    def update(self, person):
        self.__guard_is_not_empty(person)
        try:
            current_person = Person.objects.get(id=person.id)
            current_person.update(name=person.name, age=person.age)
            return True
        except:
            raise PersonException(f'Person with id {person.id} not found')

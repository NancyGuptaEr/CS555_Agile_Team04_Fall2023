import datetime
from datetime import date
# from prettytable import PrettyTable
from datetime import datetime
# from tkinter.font import families



#Sprint 1 - Nancy Gupta

def us01(individuals,families):
    for individual_person in individuals:
            # self.assertNotEqual(person.birthday, None, "Error: Birthday cannot be None")
            birthdate = individual_person.birthday.split("/")
            date_of_birth = date(
                            int(birthdate[0]),
                            int(birthdate[1]),
                            int(birthdate[2]))
            if(date.today() < date_of_birth):
                print('Birthday cannot be before today')
                return False

            #self.assertLess(birthday, today, "Error: Birthday cannot be before today")

            if individual_person.deathday != "NA":
                deathdate = individual_person.deathday.split("/")
                date_of_death = date(
                            int(deathdate[0]),
                            int(deathdate[1]),
                            int(birthdate[2]))
                if(date.today() < date_of_death):
                    print('Error: deathday cannot be before today')
                    return False
                # self.assertLess(deathDay, today, "Error: deathday cannot be before today")

    for family in families:
        for individual in individuals:
            if(individual.id == family.husbandId or individual.id == family.wifeId):
                if family.married != "NA":
                    marrieddate = family.married.split("/")
                    date_of_marriage = date(
                            int(marrieddate[0]),
                            int(marrieddate[1]),
                            int(marrieddate[2]))
                    if(date.today() < date_of_marriage):
                        print('Error : Married day cannot be before today')
                        return False
                    # self.assertLess(marriedDay, today, "Error: Married day cannot be before today")
                if family.divorced != "NA":
                    divorceddate = family.divorced.split("/")
                    date_of_divorce = date(
                            int(divorceddate[0]),
                            int(divorceddate[1]),
                            int(divorceddate[2]))
                    if(date.today() < date_of_divorce):
                        print('Error: Divorced day cannot be before today')
                        return False
                    # self.assertLess(divorcedDay, today, "Error: Divorced day cannot be before today")
    print('Test 1 Successfully Passed.')
    return True


def us02(individuals, families):
    for family in families:
        for individual in individuals:
            if individual.id == family.husbandId or individual.id == family.wifeId:
                birthdate = individual.birthday.split("/")
                date_of_birth = date(
                    int(birthdate[0]),
                    int(birthdate[1]),
                    int(birthdate[2]))

                marrieddate = family.married.split("/")
                date_of_marriage = date(
                    int(marrieddate[0]),
                    int(marrieddate[1]),
                    int(marrieddate[2]))

                # Check if birth occurs after marriage
                if date_of_birth > date_of_marriage:
                    print('Error: Birth should occur before marriage of an individual')
                    return False

    print('Test 2 Successfully Passed.')
    return True





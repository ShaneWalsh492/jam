all_employees = [
        'JOHNSON WILLIAMS','BROWN JONES','GARçIæ MILLER','DAVIS RODRIGUEZ','MARTINEZ HERNANDEZ','LOPEZ GONZALEZ',
        'WILSON ANDERSON','THOMAS TAYLOR','MÖÖRE JACKSON','MARTIN LEE','PEREZ THOMPSON','WHITE HARRIß',
        'SANCHEZ CLARK','RAMIREZ LEWIS','ROBINSON WALKER','YÖUNG ALLEN','KING WRIGHT','SCOTT TORRES',
        'NGUYEN HILL','FLORES GREEN','ADAMS NELSON','BAKER HALL','RIVERA CAMPBELL','MITCHELL CARTER',
        'ROBERTS GOMEZ','PHILLIPẞ EVANS','TURNER DIAZ','PARKER CRUZ','EDWARDS COLLINS','REYES STEWART',
        'MORRIS MORALES','MURPHY COOK','ROGERS GUTIERREZ','ORTIZ MORGAN','COOPER PETERSON',
        'BAILEY REED','HANẞ HOWARD','RAMOS KIM','CÖX WARD','RICHARDSON WATSON','BROOKS CHAVEZ',
        'WOOD JAMES','BENNETT GRAY','MENDOZA RUIZ','HUGHES PRICE','ALVAREZ çASTILLO'
    ]

def get_all_employees_input(message):
    """ Ignore this function you don't need to understand or change it """
    if "testInput" in message:
        testInputString = message.split("testInput")[1].rstrip().lstrip()
        allEmployeesTestingInput = testInputString.split(",")
        return allEmployeesTestingInput
    return all_employees

# Functions that your team will implement
def problem2_1(message):
    all_employees = get_all_employees_input(message)
    beginsWithLetterCCount = 0
    
    for c in all_employees :
        beginsWithLetterCCount += 1

    


    return str(beginsWithLetterCCount)


def problem2_2(message):
    all_employees = get_all_employees_input(message)
    peopleWithLongerThan8CharacterLastnamesCount = 0
    for person in all_employees:
        if len(person[person.index(' ') + 1:]) > 8:
            peopleWithLongerThan8CharacterLastnamesCount += 1

    return str(peopleWithLongerThan8CharacterLastnamesCount)


def problem2_3(message):
    all_employees = get_all_employees_input(message)
    employeesWhoWillGetBonusesCount = 0
    
    for employee in all_employees :
        if employee.find('ẞ') != -1 or employee.find('ö') != -1 or employee.find('æ') != -1 or employee.find('ç') != -1 or employee.find('Ö') != -1:
            employeesWhoWillGetBonusesCount += 1

    return str(employeesWhoWillGetBonusesCount)
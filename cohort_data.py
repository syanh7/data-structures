"""Functions to parse a file containing student data."""


def all_houses(filename):
    """Return a set of all house names in the given file.

    For example:
      >>> unique_houses('cohort_data.txt')
      {"Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """
    houses = set()
    
    file = open(filename)
    for line in file:
      line = line.rstrip()
      personal_info = line.split('|')
      #Harry|Potter|Gryffindor|McGonagall|Fall 2015
      #print(personal_info)

      if personal_info[4] not in ['I', 'G']:
        houses.add(personal_info[2])
    
    file.close()


    # TODO: replace this with your code

    return houses


def students_by_cohort(filename, cohort='All'):
    """Return a list of students' full names by cohort.

    Names are sorted in alphabetical order. If a cohort isn't
    given, return a list of all students. For example:
      >>> students_by_cohort('cohort_data.txt')
      ['Adrian Pucey', 'Alicia Spinnet', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Fall 2015')
      ['Angelina Johnson', 'Cho Chang', ..., 'Terence Higgs', 'Theodore Nott']

      >>> students_by_cohort('cohort_data.txt', cohort='Winter 2016')
      ['Adrian Pucey', 'Andrew Kirke', ..., 'Roger Davies', 'Susan Bones']

      >>> students_by_cohort('cohort_data.txt', cohort='Spring 2016')
      ['Cormac McLaggen', 'Demelza Robins', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Summer 2016')
      ['Alicia Spinnet', 'Dean Thomas', ..., 'Terry Boot', 'Vincent Crabbe']

    Arguments:
      - filename (str): the path to a data file
      - cohort (str): optional, the name of a cohort

    Return:
      - list[list]: a list of lists
    """

    students = []

    # TODO: replace this with your code
    #Minerva|McGonagall|||I

    file = open(filename)
    for line in file:
      line = line.rstrip()
      personal_info = line.split("|")
      if personal_info[4] not in ['I', 'G']:
        if cohort == personal_info[4]:
          students.append(f'{personal_info[0]} {personal_info[1]}')
        if cohort == "All":
          students.append(f'{personal_info[0]} {personal_info[1]}')
    
    file.close()

    return sorted(students)


def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors.

    Rosters appear in this order:
    - Dumbledore's Army
    - Gryffindor
    - Hufflepuff
    - Ravenclaw
    - Slytherin
    - Ghosts
    - Instructors

    Each roster is a list of names sorted in alphabetical order.

    For example:
      >>> rosters = hogwarts_by_house('cohort_data.txt')
      >>> len(rosters)
      7

      >>> rosters[0]
      ['Alicia Spinnet', ..., 'Theodore Nott']
      >>> rosters[-1]
      ['Filius Flitwick', ..., 'Severus Snape']

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """

    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []
  
    file = open(filename)
    for line in file:
      line = line.rstrip()
      personal_info = line.split("|")
      full_name = f'{personal_info[0]} {personal_info[1]}'

      if personal_info[4] not in ['I', 'G']:
        if personal_info[2] == 'Dumbledore\'s Army':
          dumbledores_army.append(full_name)
        elif personal_info[2] == 'Hufflepuff':
          hufflepuff.append(full_name)
        elif personal_info[2] == 'Ravenclaw':
          ravenclaw.append(full_name)
        elif personal_info[2] == 'Slytherin':
          slytherin.append(full_name)
        else:
          gryffindor.append(full_name)
          
      else:
        if personal_info[4] == "I":
          instructors.append(full_name)
        else:
          ghosts.append(full_name)

    # TODO: replace this with your code
    file.close()



    return [sorted(dumbledores_army), sorted(gryffindor), sorted(hufflepuff), sorted(ravenclaw), sorted(slytherin), sorted(ghosts), sorted(instructors)]


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """

    all_data = []
    file = open(filename)
    for line in file:
      line = line.rstrip()
      personal_info = line.split("|")
      full_name = f'{personal_info[0]} {personal_info[1]}'
      house = personal_info[2]
      advisor = personal_info[3]
      cohort = personal_info[4]
      all_data.append((full_name, house, advisor, cohort))

    # TODO: replace this with your code
    file.close()
    return all_data


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Balloonicorn')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """
    file = open(filename)
    
    for line in file:
      line = line.rstrip()
      personal_info = line.split("|")
      full_name = f'{personal_info[0]} {personal_info[1]}'
      cohort = personal_info[4]

      if name == full_name:
        return cohort
      
      


    file.close()
    # TODO: replace this with your code


def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """
    
    # TODO: replace this with your code

    last_name = set()
    dup_name = set()
    file = open(filename)
    
    for line in file:
      line = line.rstrip()
      personal_info = line.split("|")
      lname = personal_info[1]

      if lname not in last_name:
        last_name.add(lname)
      else:
        dup_name.add(lname)
    
    file.close()
    return dup_name



def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """

    # TODO: replace this with your code

    cohort_data = all_data(filename)
    housemates = set()
    
    

    for personal_info in cohort_data:
      full_name =personal_info[0]
      house = personal_info[1]
      cohort = personal_info[-1]
      
      if full_name == name:
        break  

    for personal_info in cohort_data:
      housemate_name = personal_info[0]
      housemate_cohort = personal_info[-1]
      housemate_house = personal_info[1]
      if house == housemate_house and cohort == housemate_cohort and full_name != housemate_name:
        housemates.add(housemate_name)

    return housemates 
      
    





##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')

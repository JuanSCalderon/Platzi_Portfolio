DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]
def main():
    
    # Create list comprehension y higher functions from DATA
    all_javascript = list(filter(lambda worker: worker['language'] == 'javascript', DATA))
    all_javascript = list(map(lambda worker: worker['name'], all_javascript))
    for worker in all_javascript:
        print('Javascript Developers: ',worker)

    not_a_programmer = list(map(lambda worker: worker | {'not_programmer': worker['language'] == ''}, DATA))
    not_programmer = list(filter(lambda worker: worker['not_programmer'] == True, not_a_programmer))
    not_programmer = list(map(lambda worker: worker['name'], not_programmer))
    for worker in not_programmer:
        print('Not Programmers: ',worker)

    all_platzi = [worker for worker in DATA if worker['organization'] == 'Platzi']
    for worker in all_platzi:
        print('Platzi Workers: ',worker['name'])
    

    
    
 


    
if __name__ == '__main__':
    main()
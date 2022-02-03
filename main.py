import re
# recode names dict
recode_names = {
    'Amal': '1111111111',
    'Mohammed': '2222222222',
    'Khadijah': '3333333333',
    'Abdullah': '4444444444',
    'Rawan': '5555555555',
    'Faisal': '6666666666',
    'Layla': '7777777777'
}
recode_names = {nu:na for na, nu in recode_names.items()}


def search_recode(recode_dict: dict, nu: str, by_name=False):
    pattern = "\\d{10}"
    search_term = 'number'
    if by_name:
        recode_dict = {na: nu for nu, na in recode_dict.items()}
        pattern = "[a-zA-Z]+"
        search_term = 'name'
    if not re.match(pattern, nu):
        return f'This is invalid {search_term}'
    result = recode_dict.get(nu)
    return result if result else f'Sorry, the {search_term} is not found'


if __name__ == '__main__':
    print("""
                
                        Welcome to phone recodes
                        
        please press one of numbers below to choose search method:
        
        1- search by phone number
        2- search by name
        
        Or you can add new recode by press 'n'
        
        
    """)
    user_input = input('Your input: ')
    if user_input == '1':
        number = input('Phone number: ')
        print(search_recode(recode_names, number))
    elif user_input == '2':
        name = input('Person name: ')
        print(search_recode(recode_names, name, by_name=True))
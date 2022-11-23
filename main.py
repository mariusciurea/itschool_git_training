from libs import read_write  as rw


def ex_1():
    names = rw.read_from_file('files/nume.txt')
    if names:
        new_names = [name.strip() for name in names]
        # print(new_names)
        count = {item: new_names.count(item) for item in set(new_names)}
        print(count)
        if rw.write_to_file('files/nume.txt', f'numarul de aparitii: {count}'):
            print('Am scris cu succes datele in fisier')
        else:
            print('datele nu pot fi scrise')
    else:
        print('eroare de fisier')


def ex_2():
    user = 'alexp'
    paswd = 'testing_123'
    content = rw.read_from_file('files/login_info.txt')
    # print(content)
    user_details = [item.split(';') for item in content]
    print(user_details)
    for item in user_details:
        if user in item[0] and paswd in item[1]:
            print(item[2])


def new_func():
    pass


# ex_1()
ex_2()


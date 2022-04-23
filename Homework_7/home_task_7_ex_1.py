import os
def starter_for_work():
    list_file_name = ['my_project', 'settings', 'mainapp',
                      'adminapp', 'authapp']
    for i in list_file_name:
        if i == list_file_name[0]:
            if not os.path.isdir(i):
                os.mkdir(i)
        else:
            try:
                os.makedirs(f'{list_file_name[0]}/{i}')
            except FileExistsError:
                print("директория создана")

starter_for_work()
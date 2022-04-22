import os
import shutil
import home_task_7_ex_1
def add_directory():
    if os.path.isdir('my_project'):
        os.rename('my_project', 'templates')
        os.mkdir('my_project')
        shutil.move('templates', 'my_project')
    else:
        home_task_7_ex_1.starter_for_work()
        os.rename('my_project', 'templates')
        os.mkdir('my_project')
        shutil.move('templates', 'my_project')
        print(1)

add_directory()
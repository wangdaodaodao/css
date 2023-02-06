import os

all_files = os.listdir(os.getcwd())

for fff in all_files:
    if 'ass' not in fff:
        print('无文件')
    else:
        if 'py' not in fff:
            if 'Kamigami' in fff:
                print(fff)
                f2 = fff.split('-')[1].split('[')[0].strip()
                # print(f2)
                if int(f2) < 100:
                    new_name = 'Slam Dunk - 0{}.ass'.format(f2)
                else:
                    new_name = 'Slam Dunk - {}.ass'.format(f2)
                print(new_name)
            os.rename(fff, new_name)
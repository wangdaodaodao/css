import os
from shutil import copyfile

goal_dir = '/Users/wangdaodao/Music/'
new_dir = '/Users/wangdaodao/Music/1'

# 目录内查找所有文件,并转移到新文件夹内
def find_mp3_fie ():
    for root, dirs, files in os.walk(goal_dir):
        for fff in files:
            if 'mp3'not in fff:
                old_name = '{}/{}'.format(root,fff)
                new_name = '/Users/wangdaodao/Music/2/{}'.format(fff)
                print(old_name, new_name)

                if not os.path.exists(new_name):
                    # print('cccc')
                    copyfile(old_name, new_name)
                else:
                    print('已存在')

def del_gang():
    for fff2 in os.listdir(new_dir):
    
    # 去除文件名中的1-0系列
        if '1-' in fff2:
            # print(fff2)     
            print(fff2.split(' '),fff2.split(' ')[1:])
            fff5  = ''.join(fff2.split(' ')[1:])
            if fff5:
                os.rename('{}/{}'.format(new_dir, fff2), '{}/{}'.format(new_dir, fff5))

def del_shuzi(ddd):
    for fff2 in os.listdir(new_dir)[:]:
        # print(fff2)
        if ddd in fff2:
            print(ddd,fff2)
            fff3 = fff2.replace(ddd, '')
            print(fff3)
            os.rename('{}/{}'.format(new_dir, fff2), '{}/{}'.format(new_dir, fff3))



for xxx in range(16,50):
    if xxx <10:
        xxx = '0{}'.format(xxx)
    else:
        xxx = str(xxx)
    print(xxx)
    del_shuzi(xxx)
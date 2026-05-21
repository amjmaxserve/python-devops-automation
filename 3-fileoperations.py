# The below scripts check existance of files and folder inside the same directory and give boolean result values


# import os

# import os.path

# x = os.path.exists('arjun.txt')
# print('The existance of file arjun.txt is :', x)

# os.mkdir('folder1')

# y = os.path.exists('folder1')

# print('the existance of the folder folder1 is: ', y)

# os.rmdir('folder1')
# a = os.listdir('.')
# print(a)

#------------------------------------------------------ 

# The below scripts remove folder with its contents...

import os
#import os.path
import shutil

shutil.rmtree('amj')
a = os.listdir('.')
print(a)




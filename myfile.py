# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 15:19:45 2023

@author: eevae
"""

# run this command in anaconda shell in directory that you want to create your django app
# django-admin startproject mysite

# enter the command below to run dev server
# python manage.py runserver

# to run on different port enter
# python manage.py runserver 8080

# in the spyder kernel try this:
# !python manage.py runserver

# or this

# import os
# os.system('python manage.py runserver')

# You can check the interpreter that your Spyder kernel is currently using by going to the menu bar and selecting "Tools" > "Preferences" > "Python interpreter". This will open a dialog box that shows the current interpreter being used.

# You can also check the interpreter by opening the console, and typing in import sys followed by sys.executable then press enter, it will return the path of the executable that is being used by the kernel.

# Another way is by clicking on the interpreter name at the top right corner of the spyder window,
# this will open the interpreter management window where you can see all the available interpreters and the 
# currently selected one.

#Now, let’s hop into the interactive Python shell and play around with the free API Django gives you. 
# To invoke the Python shell, use this command:
#  python manage.py shell
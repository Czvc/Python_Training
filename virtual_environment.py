"""A virtual environment in Python is an isolated environment on your computer, where you can run and test your Python projects.
It allows you to manage project-specific dependencies without interfering with other projects or the original Python installation."""

# Python has the built-in venv module for creating virtual environments.
"""To create a virtual environment on your computer, open cmd, and navigate to the folder where you want to create your project, 
then type this command: python -m venv myfirstproject """
 
# in my case I will create the project in this directory "D:\CHASE Files\Internship-Toolkt\Python_Training"
"""
The file/folder structure should look like this:
myfirstproject
  Include
  Lib
  Scripts
  .gitignore
  pyvenv.cfg
"""

# to use the virtual environment, activate it with this command in cmd
# myfirstproject\Scripts\activate

# after activation, the command line should look like this
# (myfirstproject) D:\CHASE Files\Internship-Toolkt\Python_Training>

# Once your virtual environment is activated, you can install packages in it, using pip.
# For this example we will use 'cowsay'

# in cmd, type 'pip install cowsay'
"""
(myfirstproject) D:\CHASE Files\Internship-Toolkt\Python_Training>pip install cowsay
Collecting cowsay
  Downloading cowsay-6.1-py3-none-any.whl.metadata (5.6 kB)
Downloading cowsay-6.1-py3-none-any.whl (25 kB)
Installing collected packages: cowsay
Successfully installed cowsay-6.1

[notice] A new release of pip is available: 25.0.1 -> 25.3
[notice] To update, run: python.exe -m pip install --upgrade pip
"""

"""
Now that the 'cowsay' module is installed in your virtual environment, lets use it to display a talking cow.
Create a file called test.py on your computer. You can place it wherever you want, 
but I will place it in the same location as the myfirstproject folder -not in the folder, but in the same location.
"""

"""
THIS IS THE OUTPUT I GOT:
(myfirstproject) D:\CHASE Files\Internship-Toolkt\Python_Training>cd myfirstproject

(myfirstproject) D:\CHASE Files\Internship-Toolkt\Python_Training\myfirstproject>python test.py
  _______________
| San mo lalagay? |
  ===============
               \
                \
                  ^__^
                  (oo)\_______
                  (__)\       )\/\
                      ||----w |
                      ||     ||

"""

# to deactivate the virtual environment, just type 'deactivate'
"""
(myfirstproject) D:\CHASE Files\Internship-Toolkt\Python_Training\myfirstproject>deactivate
D:\CHASE Files\Internship-Toolkt\Python_Training\myfirstproject>
"""
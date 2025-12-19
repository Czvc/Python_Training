# To check pip version just run cmd and type "pip --version"
# If PIP is not installed you can download it from this link: https://pypi.org/project/pip/
# Find more packages at https://pypi.org/
"""To download a package using PIP, in this example we can download 'camelcase'. 
Just run cmd and type 'pip install camelcase' """

# After Installing camelcase, we can now use 'import camelcase'

import camelcase

c = camelcase.CamelCase()
txt = "hello from the other side!"
print(c.hump(txt))

# using CMD first I need to move to my drive D, just type "D:"
# then cd to where the file is located using cmd, in my case = cd D:\CHASE Files\Internship-Toolkt\Python_Training
# lastly run this file by using cmd, type 'python pip_package.py'

# use the uninstall command to remove a package
# python -m pip uninstall camelcase
# The PIP Package Manager will ask you to confirm that you want to remove the camelcase package, press y and the package will be removed

# to see the list of packages just use: python -m pip list




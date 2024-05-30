"""
9-12. Multiple Modules: Store the User class in one module, and store the
Privileges and Admin classes in a separate module. In a separate file, create
an Admin instance and call show_privileges() to show that everything is still
working correctly.
"""


import admin

new_admin = admin.Admin('Admin', 'User', 0, 'Administrator')

new_admin.show_privileges()

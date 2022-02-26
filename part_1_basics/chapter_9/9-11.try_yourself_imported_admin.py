from module_class_admins import User, Privileges, Admin

satoshi = Admin('satoshi', 'nakamoto', 14, 'prophet')
prgs = ['can do any modification', 'can ban other users', ]
satoshi.privileges.modify_privileges(prgs)
satoshi.greet_user()
satoshi.privileges.show_privileges()

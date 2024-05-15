import account
new_admin_account = account.Admin('Shahin', 'Ansari', 53, ['read', 'write', 'execute'])
new_admin_account.show_privilages()
new_admin_account.describe_user()
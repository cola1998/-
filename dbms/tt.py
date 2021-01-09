import pandas as pd
# d = {'user_id':'gaohan','user_pwd':'14562563'}
# df = pd.DataFrame(d,index=[0,1])
# df.to_csv("users.csv")
d = {'user_id': 'gaohan', 'db_privilege': 'yes', 'grant': 'yes', 'create': 'yes', 'select': 'yes',
                                     'insert': 'yes', 'delete': 'yes', 'update': 'yes', 'all': 'yes'}
df = pd.DataFrame(d,index=[0])
df.to_csv("user_privileges.csv")
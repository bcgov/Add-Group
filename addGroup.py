import pandas as pd
import csv
from jira.exceptions import JIRAError
from atlassian import Jira
from jira import JIRA

jira = Jira(
    url='https://aubs-sandbox.atlassian.net',
    username='*',
    password='*'

)
# def get_id(name):
#     print(df.iloc[i]['AccId'])
def read_csv():
    df = pd.read_csv('user_information.csv',true_values=['yes'], false_values=['no'],header=0)
    num_rows = df.shape[0]
    for idx,content in enumerate(df):
            # jira.create_group(content)
        for i in range(num_rows):
            # print(content)
            # print((df.iloc[i])[content])
            if idx>1:
                group_name=content
                if (df.iloc[i])[content]==True:
                    try:
                        # Try to get the group with the specified name
                        print(jira.get_all_users_from_group(group_name, include_inactive_users=True, start=0, limit=50))
                        # jira.add_user_to_group(df.iloc[i]['name'], content, df.iloc[i]['AccId'])
                        print(f"The group '{group_name}' exists in Jira.")
                        print(df.iloc[i]['name'])
                        print(df.iloc[i]['AccId'])
                        try:
                            jira.add_user_to_group(None, group_name, df.iloc[i]['AccId'])
                        except:
                            print('user exists in this group')

                    except:
                            print(f"The group '{group_name}' does not exist in Jira.")
                            jira.create_group(content)
                            print(f"The group '{group_name}' has been created in Jira.")
                            print(df.iloc[i]['name'])
                            print(df.iloc[i]['AccId'])
                            try:
                                jira.add_user_to_group(None, group_name, df.iloc[i]['AccId'])
                            except:
                                print('user exists in this group')
                elif(df.iloc[i])[content]==False:
                    try:
                        # Try to get the group with the specified name
                        print(jira.get_all_users_from_group(group_name, include_inactive_users=True, start=0, limit=50))
                        # jira.add_user_to_group(df.iloc[i]['name'], content, df.iloc[i]['AccId'])
                        print(f"The group '{group_name}' exists in Jira.")
                        print(df.iloc[i]['name'])
                        print(df.iloc[i]['AccId'])
                        try:
                            jira.remove_user_from_group(None, group_name, df.iloc[i]['AccId'])
                        except:
                            print('user not in this group')
                    except:
                            print(f"The group '{group_name}' does not exist in Jira.")
                    # jira.add_user_to_group(df.iloc[i]['name'], content, df.iloc[i]['AccId'])
                    # print(df.iloc[i]['name'])
                    # print(df.iloc[i]['AccId'])
                    # print(content)


read_csv()
# jira.add_user_to_group(None, 'sparklingwater3', '557058:6193f5d3-2bcf-4b3a-9656-a10295ba37fc')

from databricks.sdk import AccountClient
from databricks.sdk.service import iam
from databricks.sdk.oauth import SessionCredentials

import pandas as pd

if __name__ == "__main__":
    # For account-level operations, you should first use the Databricks CLI to run the following command, before you run your Python code. 
    # This command instructs the Databricks CLI to generate and cache the necessary OAuth token in the path .databricks/token-cache.json 
    # within your user’s home folder on your machine:

    # databricks auth login --host https://accounts.azuredatabricks.net/ --account-id <account-id>

    profile = input("Enter Databricks host profile: ")
    a = AccountClient(profile=profile)
    all_users = a.users.list(attributes="userName,display_name,roles,groups",
                            sort_by="userName",
                            sort_order=iam.ListSortOrder.DESCENDING)

    users = [user.as_dict() for user in all_users]
    df = pd.DataFrame(users)
    print(df)

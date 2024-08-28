from databricks.sdk import AccountClient
from databricks.sdk.service import iam
from databricks.sdk.oauth import SessionCredentials

import pandas as pd

# Optional: create an enum for possible attributes
ATTRIBUTES = ['userName', 'display_name', 'roles', 'groups'] # To refactor databricks sdk, userName in camel case but display_name in snake case

if __name__ == "__main__":
    # Use docstring instead of comment
    """For account-level operations, you should first use the Databricks CLI to run the following command, before you run your Python code. 
    This command instructs the Databricks CLI to generate and cache the necessary OAuth token in the path .databricks/token-cache.json 
    within your user’s home folder on your machine:

    databricks auth login --host https://accounts.azuredatabricks.net/ --account-id <account-id>
    """

    profile = input("Enter Databricks host profile: ")
    account = AccountClient(profile=profile)
    all_users = account.users.list(attributes=','.join(ATTRIBUTES),
                            sort_by="userName",
                            sort_order=iam.ListSortOrder.DESCENDING)

    users = [user.as_dict() for user in all_users]
    df = pd.DataFrame(users)

    # Avoid using print
    df.describe()
    df.head()

# Tool to bulk list users/groups from the Account console

This directory contains the `list_account_users.py` script that allows to list users & associated groups from the Account console.

## Installation

You need to have [Databricks SDK for Python](https://pypi.org/project/databricks-sdk/) installed and pandas to run this tool.  Do

```sh
pip install databricks-sdk
pip install pandas
```

to install  Databricks SDK and pandas


## Running

You must configure OAuth to perform Account level operations. To configure U2M authentication, please follow this [doc](https://learn.microsoft.com/en-us/azure/databricks/dev-tools/auth/oauth-u2m#python).

For account-level operations, you should first use the Databricks CLI to run the following command, before you run your Python code. This command instructs the Databricks CLI to generate and cache the necessary OAuth token in the path `.databricks/token-cache.json` within your user’s home folder on your machine:

```
databricks auth login --host <account-console-url> --account-id <account-id>
```

then run the python script

```
python list_account_users.py
```
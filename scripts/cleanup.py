import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
credential = DefaultAzureCredential()
client = ResourceManagementClient(credential, subscription_id)

for rg in client.resource_groups.list():
    if "test" in rg.name.lower():
        print(f"Deleting resource group: {rg.name}")
        client.resource_groups.begin_delete(rg.name)

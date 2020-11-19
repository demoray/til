# Clearing out deleted Azure App Registrations

Application Registrations in Azure Active Directory have a quota of 250 entries
for per user by default.

Deleted application registrations are 'soft-deleted' for 30 days.  

The following sample hard-deletes application registrations that include
'pr-check' in the name.

```python
from azure.graphrbac import GraphRbacManagementClient
from azure.common.client_factory import get_client_from_cli_profile

for entry in client.deleted_applications.list():
    if 'pr-check' in entry.display_name:
        client.deleted_applications.hard_delete(entry.object_id)
```

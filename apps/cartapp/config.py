# from azure.keyvault.secrets import SecretClient
# from azure.identity import ClientSecretCredential
from django.conf import settings

# secret_properties = _sc.list_properties_of_secrets()

# for secret_property in secret_properties:
#     # the list doesn't include values or versions of the secrets
#     print(secret_property.name)

# def get_secret_from_azure_kv(secret_name, default_value=None):
#     keyVaultName = settings.AZURE_KEY_VAULT_URI
#     credential = ClientSecretCredential(settings.AZURE_TENANT_ID, settings.AZURE_KEY_VAULT_CLIENT, settings.AZURE_KEY_VAULT_SECRET)
#     _sc = SecretClient(keyVaultName, credential)

#     try:
#         return _sc.get_secret(secret_name)
#     except Exception:
#         return default_value

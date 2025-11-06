from storages.backends.azure_storage import AzureStorage
# class AzureMediaStorage(AzureStorage):
#     account_name = 'haveblueazdev'  # Must be replaced when going to PROD
#     account_key = 'eP954sCH3j2+dbjzXxcAEj6n7vmImhsFvls+7ZU7F4THbQfNC0dULssGdbXdilTpMgaakIvEJv+QxCmz/G4Y+g=='
#     azure_container = 'portolamedia'
#     expiration_secs = None
#
# class AzureStaticStorage(AzureStorage):
#         account_name = 'haveblueazdev'  # Must be replaced when going to PROD
#         account_key = 'eP954sCH3j2+dbjzXxcAEj6n7vmImhsFvls+7ZU7F4THbQfNC0dULssGdbXdilTpMgaakIvEJv+QxCmz/G4Y+g=='
#         azure_container = 'static'
#         expiration_secs = None

class AzureMediaStorage(AzureStorage):
    account_name = 'portalstore1'  # Must be replaced when going to PROD
    account_key = '/WZCC8HIgX6V1MnhYNqrVhb/V0DM9G7g+AyvS59tdKbSX5sZbV7I0wkiP14vbyHqniJe1P/pYbT0+AStytkQGw=='
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'portalstore1'  # Must be replaced when going to PROD
    account_key = '/WZCC8HIgX6V1MnhYNqrVhb/V0DM9G7g+AyvS59tdKbSX5sZbV7I0wkiP14vbyHqniJe1P/pYbT0+AStytkQGw=='
    azure_container = 'static'
    expiration_secs = None


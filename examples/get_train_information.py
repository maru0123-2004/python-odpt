from os import environ
from python_odpt import Client
from python_odpt.api import get_train_information

client=Client("http://api.odpt.org/api/v4/")
token=environ.get("ODPT_TOKEN", None)

# Fetch train information synchronously
# You can pass query parameters as keyword arguments
train_info_list = get_train_information.sync(
    client=client,
    aclconsumer_key=token,
    # Example query parameters:
    # odpt_operator="odpt.Operator:JR-East"
)

if train_info_list:
    print(f"Retrieved {len(train_info_list)} records.")
else:
    print("No data retrieved.")
    exit(1)

for train_info in train_info_list:
    # Access basic string properties
    print(f"Railway ID: {train_info.odptrailway}")
    
    # Access nested/localized properties (e.g., Multilingual text)
    if train_info.odpttrain_information_text:
        print(f"Information (JA): {train_info.odpttrain_information_text.ja}")
        print(f"Information (EN): {train_info.odpttrain_information_text.en}")
    
    # Access date-time objects (automatically parsed into datetime instances)
    print(f"Time of generation: {train_info.dcdate}")
    print("-" * 20)
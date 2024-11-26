from python_odpt import Client
from python_odpt.api.default import data_search_operations_search
from os import environ

client=Client("http://api.odpt.org/api/v4/")
token=environ.get("ODPT_TOKEN", None)
res=data_search_operations_search.sync_detailed(client=client, aclconsumer_key=token, rdf_type="odpt:BusstopPole", predicate={"odpt:operator":"odpt.Operator:Toei"})

print(res.status_code)
print(res.parsed[0])
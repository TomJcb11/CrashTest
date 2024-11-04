"""import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = os.environ.get("INFLUXDB_TOKEN")
bucket="Trendly"
org = "Trendly"
url = "http://localhost:8086"
token = "RQ2PSWUiYMk6v3GyPiD-yJ7NpkpAJATgrJfdWGxdJ3wwCBprxAy72C7URJtnG4Qc1b3mSxpQa_Bm4h3OJ8l_FA=="

client = influxdb_client.InfluxDBClient(
   url=url,
   token=token,
   org=org
)


write_api = client.write_api(write_options=SYNCHRONOUS)
   
p = influxdb_client.Point("my_measurement").tag("location", "Prague").field("temperature", 25.3)
write_api.write(bucket=bucket, org=org, record=p)


query_api = client.query_api()

query = 'from(bucket:"Trendly")\
|> range(start: -10m)\
|> filter(fn:(r) => r._measurement == "my_measurement")\
|> filter(fn:(r) => r.location == "Prague")\
|> filter(fn:(r) => r._field == "temperature")'

result = query_api.query(org=org, query=query)


results = []
for table in result:
  for record in table.records:
    results.append((record.get_field(), record.get_value()))

print(results)
[(temperature, 25.3)]"""
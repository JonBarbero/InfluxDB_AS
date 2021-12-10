from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

url = "http://localhost:8086"
bucket = "my-bucket"
org = "my-org"
token = "my-token"
query_api = None
client = InfluxDBClient(url=url, token=token, org=org)


def meterdatos():
    global query_api
    write_api = client.write_api(write_options=SYNCHRONOUS)
    query_api = client.query_api()

    p = Point("my_measurement").tag("location", "Spain").field("temperature", 18.2)
    p2 = Point("my_measurement").tag("location", "Italy").field("temperature", 15.6)


    write_api.write(bucket=bucket, org=org, record=p)
    write_api.write(bucket=bucket, org=org, record=p2)


def imprimirdatos():
    # using Table structure
    tables = query_api.query('from(bucket:"my-bucket") |> range(start: -10m)')

    for table in tables:
        print(table)
        for row in table.records:
            print(row.values)


if __name__ == "__main__":
    meterdatos()
    imprimirdatos()
    # client.close()

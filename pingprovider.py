from pythonping import ping
from time import sleep
import click
import datetime

providers = {
    "talktalk": "62.24.134.1",
    "sky": "90.207.238.97",
    "virgin": "194.168.4.100",
    "bt": "62.6.40.178"
}

@click.command()
@click.option('--isp', default="8.8.8.8",
              help="This is your internet service provider such as 'bt'.")
@click.option('--minutes', default=1,
              help="This is how long the logs will run for.")              
@click.argument('outfile', type=click.File('w'), default='pingprovider_log.csv',
                required=False)
def cli(isp, minutes, outfile):
    """This script pings your ISP and logs a response time every second."""
    dns_to_ping = providers[isp.lower()] if isp.lower() in providers else isp
    outfile.write(f"Time,Response_Time(ms),Start:{datetime.datetime.now()},DNS:{dns_to_ping}\n")
    counter = 0
    while(counter != minutes*60):
        result = ping(dns_to_ping, verbose=True, count=1, timeout=1)
        for item in result:
            outfile.write(f"{datetime.datetime.now()},{item.time_elapsed_ms}\n")
        sleep(1)
        counter += 1

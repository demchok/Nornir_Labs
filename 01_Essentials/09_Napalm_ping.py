import os
from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_ping
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

nr.inventory.defaults.username = os.environ["USERNAME"]
nr.inventory.defaults.password = os.environ["PASSWORD"]

def nap_ping_ips(task):
    task.run(task=napalm_ping, dest="10.0.0.5")


results = nr.run(task=nap_ping_ips)

print_result(results)
import os
from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

nr.inventory.defaults.username = os.environ["USERNAME"]
nr.inventory.defaults.password = os.environ["PASSWORD"]

def nap_get_ips(task):
    task.run(task=napalm_get, getters=["get_interfaces_ip"])

results = nr.run(task=nap_get_ips)

print_result(results)
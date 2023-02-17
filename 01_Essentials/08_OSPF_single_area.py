import os
from nornir import InitNornir
from nornir_scrapli.tasks import send_configs
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

nr.inventory.defaults.username = os.environ["USERNAME"]
nr.inventory.defaults.password = os.environ["PASSWORD"]

def start_ospf(task):
    task.run(task=send_configs, configs=["router ospf 1", f"router-id {task.host['loop0_ip']}", "network 0.0.0.0 255.255.255.255 area 0"])

result_loop0 = nr.run(task=start_ospf)

print_result(result_loop0)
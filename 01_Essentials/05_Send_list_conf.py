import os
from nornir import InitNornir
from nornir_scrapli.tasks import send_configs
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

nr.inventory.defaults.username = os.environ["USERNAME"]
nr.inventory.defaults.password = os.environ["PASSWORD"]

def conf_command_list (task):
#    task.run(task=send_configs, configs=["ntp server 1.1.1.1", "no ntp server 1.1.1.1"])
    task.run(task=send_configs, configs=["int gig2", "no ip address", "int gig3", "no ip address","int gig4", "no ip address","int gig5", "no ip address",])

results = nr.run(task=conf_command_list)

print_result(results)
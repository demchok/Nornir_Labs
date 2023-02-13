from nornir import InitNornir
from nornir_scrapli.tasks import send_configs
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def simple_send(task):
    task.run(task=send_configs, configs=["line vty 0 4", "exec-timeout 0 0"])

def write_mem(task):
    task.run(task=send_command, command="write memory")

results_send = nr.run (task=simple_send)
results_write = nr.run (task=write_mem)

print_result(results_send)
print_result(results_write)
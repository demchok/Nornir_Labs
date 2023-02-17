import os
from nornir import InitNornir
from nornir_scrapli.tasks import send_interactive
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

nr.inventory.defaults.username = os.environ["USERNAME"]
nr.inventory.defaults.password = os.environ["PASSWORD"]

def backup_run_flash(task):
    cmds = [("copy run flash:Backup_with_IPs.cfg", "Destination filename [Backup_with_IPs.cfg]?"), ("\n", f"{task.host}#")]
    task.run(task=send_interactive, interact_events=cmds)

results = nr.run(task=backup_run_flash)

print_result(results)
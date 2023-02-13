from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def Restore_flash_run(task):
    task.run(task=send_command, command="configure replace flash:Backup.cfg force")

results = nr.run(task=Restore_flash_run)

print_result(results)
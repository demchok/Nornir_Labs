from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

# command_list = ["show int summ | inc Gig", "sh version | inc Uptime", "sh users | inc vty"]

#command_list = ["sh ip interf brief"]

command_list = ["write mem"]

def show_command_list (task):
    for cmd in command_list:
        task.run(task=send_command, command=cmd)

results = nr.run(task=show_command_list)

print_result(results)
from nornir import InitNornir
from nornir_scrapli.tasks import send_configs
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def set_ip_gig2(task):
    task.run(task=send_configs, configs=["interf gig2", f"{task.host['gig2_ip']}"])

def set_ip_gig3(task):
    task.run(task=send_configs, configs=["interf gig3", f"{task.host['gig3_ip']}"])

def set_ip_gig4(task):
    task.run(task=send_configs, configs=["interf gig4", f"{task.host['gig4_ip']}"])

def set_ip_gig5(task):
    task.run(task=send_configs, configs=["interf gig5", f"{task.host['gig5_ip']}"])

def set_ip_loop0(task):
    task.run(task=send_configs, configs=["interf loop0", f"{task.host['loop0_ip']}"])

result_gig2 = nr.run (task=set_ip_gig2)
result_gig3 = nr.run (task=set_ip_gig3)
result_gig4 = nr.run (task=set_ip_gig4)
result_gig5 = nr.run (task=set_ip_gig5)
result_loop0 = nr.run (task=set_ip_loop0)

print_result(result_gig2)
print_result(result_gig3)
print_result(result_gig4)
print_result(result_gig5)
print_result(result_loop0)
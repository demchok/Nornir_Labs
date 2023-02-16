# This is a stupid version of the assign script. At the end of the file you can see
# another version which is a much more decent piece of programming, but the problem 
# with it is that is doesn't work because of the Python/Nornir data structure limitations

from nornir import InitNornir
from nornir_scrapli.tasks import send_configs
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def set_ip_gig2(task):
    task.run(task=send_configs, configs=["interf gig2", f"ip address {task.host['gig2_ip']} {task.host['gig2_netmask']}"])

def set_ip_gig3(task):
    task.run(task=send_configs, configs=["interf gig3", f"ip address {task.host['gig3_ip']} {task.host['gig3_netmask']}"])

def set_ip_gig4(task):
    task.run(task=send_configs, configs=["interf gig4", f"ip address {task.host['gig4_ip']} {task.host['gig4_netmask']}"])

def set_ip_gig5(task):
    task.run(task=send_configs, configs=["interf gig5", f"ip address {task.host['gig5_ip']} {task.host['gig5_netmask']}"])

def set_ip_loop0(task):
    task.run(task=send_configs, configs=["interf loop0", f"ip address {task.host['loop0_ip']} {task.host['loop0_netmask']}"])

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

# A more decent version of the assign script. Because of Nornir/Python limitations, 
# this piece of code assigns incorrect IPs 

#host_count = len(nr.inventory.hosts)

#print(f"Inventory host count: {host_count}\n")

#for host_id in range (1,host_count+1):
#    host = nr.inventory.hosts[f"R{host_id}"]
#    int_count = (host["int_count"])
    
#    print("\n", nr.inventory.hosts[f"R{host_id}"], f"has {int_count} routing interfaces:")
        
#    int_num = 2
#    while int_num <= int_count+1 :
#        int_ref = f"gig{int_num}_ip"
#        int_msk = f"gig{int_num}_netmask"
#        print(int_ref, int_msk)

#        ip = (host[int_ref])
#        mask = (host[int_msk])
        
#        print(ip, mask)
     
#        def assign_ip (task):
#           task.run(task=send_configs, configs=[f"interface Gig{int_num}", f"ip address {ip} {mask}"])
#        results = nr.run(task=assign_ip)
#        print_result(results)
#        print(int_ref, ip, mask)
#        int_num+=1
# Nornir_Labs
<p>In this repo I'm exploring Nornir and its plugins, such as Scrapli, NetMiko, NAPALM, etc. For further info, please see the README file.</p>

Details:
<ul>
  <li>The labs are based on the Topology V1 PNG file</li>
  <li>Routers are Cisco CSR1000v</li>
  <li>Each router has its interface GigabitEthernet 1 dedicated to the OOBM function</li>
  <li>The OOBM addresses are 10.10.10.31 ... 10.10.10.37 respectively to the Router number [R1-R7]</li>
  <li>Each router has the last octet in every IP address equal to its number (i.e. R7 has IP addresses like 10.0.0.7, 10.10.17.7)</li>
  <li>The automation machine is an Ubuntu desktop running LTS 20.04</li>
  
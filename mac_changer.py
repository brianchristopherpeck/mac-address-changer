#!/usr/bin/env python
# Subprocess allows shell access
import subprocess
# Optperse allows options in cli
import optparse
# Re Third Party regex module
import re

# Create command line arguments to be consumed by program
def c_args():
	# Calls the optparse package
	parser = optparse.OptionParser()
	# Sets allowable command line parameters and --help descriptions
	parser.add_option("-o", "--operating-system", dest="operating_system", help="Choose the type of operating system to run mac changer on")
	parser.add_option("-i", "--interface", dest="interface", help="Interface to change cpu's mac address")
	parser.add_option("-m", "--mac", dest="new_mac_address", help="New mac address")
	# Gather arguments and they're values (options)
	(options, arguments) = parser.parse_args()
	if not options.operating_system:
		parser.error("[-] Please specify a operating system. Use --help for more info")
	elif not options.interface:
		parser.error("[-] Please specify an interface. Use --help for more info")
	elif not options.new_mac_address:
		parser.error("[-] Please specify a mac address. Use --help for more info")
	return options

# Change mac address based on OS (Linux or MACOSX)
def c_mac(os, interface, new_mac_address):
	print("[+] Changing MAC Address for os: " + os + " " + interface + ' to: ' + new_mac_address)
	if os == "Linux" : # Linux Distros
		subprocess.call(["ifconfig"], shell=True)
		subprocess.call(["ifconfig", interface, "down"])
		subprocess.call(["ifconfig", interface, "hw", "ether", new_mac_address])
		subprocess.call(["ifconfig", interface, "up"])
		subprocess.call(["ifconfig", interface])
	elif os == "Mac" : # Mac OSX Distro
		subprocess.call("ifconfig " + interface + " | grep ether", shell=True)
		subprocess.call("openssl rand -hex 6 | sed 's/\(..\)/\1:/g; s/.$//'", shell=True)
		subprocess.call(["ifconfig", interface, "ether", new_mac_address])
		subprocess.call("ifconfig " + interface + " | grep ether", shell=True)

# Get the current MAC address
def g_c_mac(interface):
	ifconfig_result = subprocess.check_output(["ifconfig", interface])
	re_result = re.search(r"([0-9a-fA-F]:?){12}", ifconfig_result)
	if re_result:
		return re_result.group(0)
	else:
		print("[-] Could not read MAC address")

# Create the initiating arguments
options = c_args()

# Print current MAC address before change
current_mac = g_c_mac(options.interface)
print("Current MAC = " + str(current_mac))

# Passes options values to change mac address function 
c_mac(options.operating_system, options.interface, options.new_mac_address)

# Get current MAC address after change
current_mac = g_c_mac(options.interface)
if current_mac == options.new_mac_address:
	print("[+] MAC Address was successfully changed to " + current_mac)
else:
	print("[-] MAC Address didn't change")
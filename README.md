# mac-address-changer

## Help
```
python3 mac_changer.py --help
```

## Options
```
Options:
  -h, --help            show this help message and exit
  -o OPERATING_SYSTEM, --operating-system=OPERATING_SYSTEM
                        Choose the type of operating system to run mac changer
                        on
  -i INTERFACE, --interface=INTERFACE
                        Interface to change cpu's mac address
  -m NEW_MAC_ADDRESS, --mac=NEW_MAC_ADDRESS
                        New mac address
```

## Example command for MacOSX
```
sudo python mac_changer.py -o Mac -i en0 -m 00:11:22:33:44:22
```
#### Mac Address will be cloaked on requests but will still show original system Mac Address in settings

## Example command for Linux
```
sudo python mac_changer.py -o Linux -i eth0 -m 00:11:22:33:44:22
```
#### Mac Address will be cloaked on requests but will still show original system Mac Address in settings

### Currently does NOT work for Windows systems
from bluepy.btle import Peripheral, UUID
from bluepy.btle import Scanner, DefaultDelegate

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        return
        if isNewDev:
            print "Discovered device", dev.addr
        elif isNewData:
            print "Received new data from", dev.addr

scanner = Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(10.0)
n=0
for dev in devices:
    print "%d: Device %s (%s), RSSI=%d dB" % (n, dev.addr, dev.addrType, dev.rssi)
    n += 1
    for (adtype, desc, value) in dev.getScanData():
        if value == "Running Speed and Cadence":
            print "=========================== I'm here ====================\n\n\n"
    #    print " %s = %s" % (desc, value)

number = input('Enter your device number: ')
print('Device', number)
print(devices[number].addr)

print "Connecting..."
dev = Peripheral(devices[number].addr, 'random')
print("Services...")
for svc in dev.services:
    print(str(svc))

try:
    testService = dev.getServiceByUUID(UUID(0x1814))
    for ch in testService.getCharacteristics():
        print "in try for ch", str(ch)
    ch = dev.getCharacteristics(uuid=UUID(0x2a5D))[0]
    if (ch.supportsRead()):
        print(ch.read())
        
    ch_2 = dev.getCharacteristics(uuid=UUID(0x2a54))[0]
    ch_2.write(b'\x74\x14')
finally:
    dev.disconnect() 
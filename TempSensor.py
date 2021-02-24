import time
import machine
import onewire, ds18x20

dsPin = machine.Pin(12)

ds = ds18x20.DS18X20(onewire.OneWire(dsPin))

roms = ds.scan()
#[bytearray(b'(&\xad\x07\xd6\x01<R')]
#print(roms)

while True:
    
    print('temperatures:', end=' ')
    ds.convert_temp()
    for rom in roms:
        print(ds.read_temp(rom), end='\n')
    time.sleep(2)
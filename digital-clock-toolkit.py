import bluetooth
import time

def discover_devices():
    print("Searching for devices...")
    nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True, lookup_class=False)
    return nearby_devices

def connect_and_send_message(address, message):
    port = 1  # RFCOMM port
    sock = bluetooth.BluetoothSocket()
    
    try:
        sock.connect((address, port))
        print(f"Connected to {address}")
        
        sock.send(str.encode(message))
        print(f"Message sent: {message}")
        
    except bluetooth.btcommon.BluetoothError as err:
        print(f"Bluetooth error: {err}")
    finally:
        sock.close()

def main():
    devices = discover_devices()
    
    if not devices:
        print("No devices found.")
        return
    
    print("Found devices:")
    for idx, device in enumerate(devices):
        address, name = device
        print(f"{idx}: {name} - {address}")
    
    device_idx = int(input("Select device index to connect: "))
    if device_idx < 0 or device_idx >= len(devices):
        print("Invalid index")
        return
    
    address = devices[device_idx][0]

    message = f'|RTC,{time.strftime("%Y,%m,%d,%H,%M,%S,")}'

    connect_and_send_message(address, message)

if __name__ == "__main__":
    main()
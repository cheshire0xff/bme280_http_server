# bme280_http_server
http server communicating with udp esp32 device with bme280 sensor.
Runs on port 5000.

# Requirements

Flask python3 package is required to use app.
To install run:
```
pip3 install flask
```

# Usage

To run the server you have to provide esp32 device IP.  
If using ipv6 be sure that esp32 device is also configured to support that protocol.
```
python3 http_server.py 192.168.1.104
python3 http_server.py fe80:0000:0000:0000:42f5:20ff:fe70:2954
```

Show options:
```
python3 http_server.py -h
```
# UI

![alt text](docs/screenshot.png "html page screenshot")

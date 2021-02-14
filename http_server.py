import os
import argparse
import ipaddress

from flask import Flask
from flask import Response
import bme280_comm as bme


app = Flask(__name__, static_folder=os.path.abspath('html'))
esp32ip = ""
esp32port = 3333

@app.route('/')
def index():
    return app.send_static_file("index.html")

@app.route('/esp_command/<string:command>')
def esp_command(command):
    dev = bme.Bme280Device(
            esp32ip,
            esp32port)
    return Response(
            dev.send_command(command),
            mimetype="application/json")

def get_parser():
    parser = argparse.ArgumentParser(
        description='http server.')
    parser.add_argument('ip_address',
        type=ipaddress.ip_address,
        help="provide esp32 device ip")
    parser.add_argument('-p', '-port',
        help="provide esp32 device udp port",
        type=int,
        default=3333)
    return parser
    
if __name__ == "__main__":
    args = get_parser().parse_args()
    esp32ip = args.ip_address
    esp32port = args.p
    app.run(host='127.0.0.1', port='5000')


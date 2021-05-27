import pexpect
from flask import Flask, request

from constants import server_port

app = Flask(__name__)

console = pexpect.spawn("bash")


@app.route('/<device>', methods=["POST"])
def color(device):
    req_dict = request.form.to_dict()
    red = req_dict.get('red', None)
    green = req_dict.get('green', None)
    blue = req_dict.get('blue', None)
    brightness_val = req_dict.get('brightness', None)
    try:
        color = ""
        if red and green and blue:
            color = f"--color {int(red)} {int(green)} {int(blue)}"
        brightness = ""
        if brightness_val:
            brightness = f"--brightness {int(brightness_val)}"
        console.sendline(f"sudo python3 tool.py set --device {device} {color} {brightness}")
        return "Done"
    except Exception:
        return "Bad request"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=server_port)

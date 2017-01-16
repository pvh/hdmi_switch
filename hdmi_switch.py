from flask import Flask
import serial

ser = serial.Serial('/dev/ttyUSB0', 19200, timeout=1)

app = Flask(__name__)

serial_commands = {
  'A1': 'A55B02030100010000000000F9',
  'A2': 'A55B02030200010000000000F8',
  'A3': 'A55B02030300010000000000F7',
  'A4': 'A55B02030400010000000000F6',
  'B1': 'A55B02030100020000000000F8',
  'B2': 'A55B02030200020000000000F7',
  'B3': 'A55B02030300020000000000F6',
  'B4': 'A55B02030400020000000000F5'
}

@app.route("/")
def hello():
    return "Hello from the switch!"

@app.route("/change/<input>/<output>")
def change(input, output):
    ser.write(bytearray.fromhex(serial_commands[input+output]));
    return "Changed to " + input + "/" + output +"!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1337)


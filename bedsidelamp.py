#!/usr/bin/python

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import urlparse
import thread
from time import sleep

set_brightness = 0
cur_brightness = 0
left_lamp = 22
right_lamp = 17

def pwm(pin, amount):
    f = open('/dev/pi-blaster', 'w')
    f.write('%d=%s\n'%(pin, str(amount)))

def controllights():
    while True:
        global set_brightness
        global cur_brightness
        sleep(1)
        cur_set_brightness = int(set_brightness)
        if (cur_set_brightness != cur_brightness):
            sleep_time = float(fade)/100
            print(set_brightness)
            print('Sleep time: ' + str(sleep_time))
            if (cur_set_brightness > cur_brightness):
                for cur_brightness in range(cur_brightness,int(cur_set_brightness) + 1):
                    pwmval = float(cur_brightness/100.0)
                    pwm(left_lamp, pwmval)
                    pwm(right_lamp,  pwmval)
                    sleep(sleep_time)
                    print("Current brightness: " + str(cur_brightness))
                    if (int(set_brightness) != cur_set_brightness):
                        print("Brightness Changed")
                        break

            if (cur_set_brightness < cur_brightness):
                for cur_brightness in range(cur_brightness,int(cur_set_brightness) - 1, -1):
                    pwmval = float(cur_brightness/100.0)
                    pwm(left_lamp, pwmval)
                    pwm(right_lamp,  pwmval)
                    sleep(sleep_time)
                    print("Current brightness: " + str(cur_brightness))
                    if (int(set_brightness) != cur_set_brightness):
                        print("Brightness Changed")
                        break

def parse_data(parsable_data):
        global data
        global set_brightness
        global fade
        if ((parsable_data.get('brightness', [''])[0]) != ''):
            set_brightness = parsable_data.get('brightness', [''])[0]
        if ((parsable_data.get('fade', [''])[0]) != ''):
            fade = parsable_data.get('fade', [''])[0]
        else:
            fade =  '10'
        data = [set_brightness,fade]

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        qs = {}
        path = self.path
        if '?' in path:
            path, tmp = path.split('?', 1)
            qs = urlparse.parse_qs(tmp)
            parse_data(qs)
            self.send_response(200)
            if (data != ''):
                print(data)
            self.end_headers()
            self.wfile.write('Request Recieved')
        return

    def log_request(self, code=None, size=None):
        print('Request')

    def log_message(self, format, *args):
        print('Message')

def server_thread():
    try:
        server = HTTPServer(('', 8080), MyHandler)
        print('Started http server')
        server.serve_forever()
    except KeyboardInterrupt:
        print('^C received, shutting down server')
        server.socket.close()

try:
   thread.start_new_thread(server_thread,())
   thread.start_new_thread(controllights,())
except:
   print "Error: unable to start thread"

while 1:
   pass
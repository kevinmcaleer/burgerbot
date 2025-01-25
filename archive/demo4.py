# BurgerBot V2
# Kevin McAleer
# September 2022

from phew import server, logging, dns, access_point
from phew.template import render_template
from phew.server import redirect
from archive.burgerbot import Burgerbot
from time import sleep
import math

mac = Burgerbot()
mac.speed = 0.5

DOMAIN = "burgerbot.wireless"
ap_name = "burgerbot"
command = ""

@server.route("/", methods=['GET','POST'])
def index(request):
    """ Render the Index page and respond to form requests """
    if request.method == 'GET':
        logging.debug("Get request")
        return render_template("index.html")
    if request.method == 'POST':
        print("posted content received")
        if request.form.get("Forward"):
            mac.forward()
        if request.form.get("Backward"):
            mac.backward()
        if request.form.get("Stop"):
            mac.stop()
        if request.form.get("left"):
            mac.turnleft()
        if request.form.get("right"):
            mac.turnright()
        if request.form.get("Pen up"):
            mac.pen_up()
        if request.form.get("Pen down"):
            mac.pen_down()
        
        
        command = request.form

        print(command)
         
        #return render_template("index.html")

@server.route("/wrong-host-redirect", methods=["GET"])
def wrong_host_redirect(request):
    # if the client requested a resource at the wrong host then present 
    # a meta redirect so that the captive portal browser can be sent to the correct location
    body = "<!DOCTYPE html><head><meta http-equiv=\"refresh\" content=\"0;URL='http://" + DOMAIN + "'/ /></head>"
    logging.debug("body:",body)
    return body

@server.route("/hotspot-detect.html", methods=["GET"])
def hotspot(request):
    """ Redirect to the Index Page """
    return render_template("index.html", command=command)

@server.catchall()
def catch_all(request):
    """ Catch and redirect requests """
    if request.headers.get("host") != DOMAIN:
        return redirect("http://" + DOMAIN + "/wrong-host-redirect")

def start_ap():
    """ Start the Hotspot """

    # connect_to_wifi(access_point, self.DOMAIN)
    # Set to Accesspoint mode
    ap = access_point(ap_name)  # Change this to whatever Wifi SSID you wish
    ip = ap.ifconfig()[0]                   # Grab the IP address and store it
    logging.info(f"starting DNS server on {ip}")
    dns.run_catchall(ip)                    # Catch all requests and reroute them
    server.run()                            # Run the server
    logging.info("Webserver Started")



# setup the accesspoint
start_ap()
print("hello")


# while True:
#     sleep(0.5)
#     print('.', end="")
#     if command == "penup":
#         mac.pen_up()
#     if command == "pendown":
#         mac.pen_down()
#     if command == "forward":
#         mac.forward()
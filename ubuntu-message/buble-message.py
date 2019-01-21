import sys
import pynotify

capabilities = {
    'actions':             False,
    'body':                False,
    'body-hyperlinks':     False,
    'body-images':         False,
    'body-markup':         False,
    'icon-multi':          False,
    'icon-static':         False,
    'sound':               False,
    'image/svg+xml':       False,
    'private-synchronous': False,
    'append':              False,
    'private-icon-only':   False
}

def initCaps ():
  caps = pynotify.get_server_caps ()
  if caps is None:
    print "Failed to receive server caps."
    sys.exit (1)

  for cap in caps:
    capabilities[cap] = True

def get_ip():
  import urllib2
  import json

  response = urllib2.urlopen("http://freegeoip.io/json")
  json_dictionary = json.loads(response.read())
  return json_dictionary

def printCaps ():
  info = pynotify.get_server_info ()
  print "Name:          " + info["name"]
  print "Vendor:        " + info["vendor"]
  print "Version:       " + info["version"]
  print "Spec. Version: " + info["spec-version"]

  caps = pynotify.get_server_caps ()
  if caps is None:
    print "Failed to receive server caps."
    sys.exit (1)

  print "Supported capabilities/hints:"
  if capabilities['actions']:
      print "\tactions"
  if capabilities['body']:
      print "\tbody"
  if capabilities['body-hyperlinks']:
      print "\tbody-hyperlinks"
  if capabilities['body-images']:
      print "\tbody-images"
  if capabilities['body-markup']:
      print "\tbody-markup"
  if capabilities['icon-multi']:
      print "\ticon-multi"
  if capabilities['icon-static']:
      print "\ticon-static"
  if capabilities['sound']:
      print "\tsound"
  if capabilities['image/svg+xml']:
      print "\timage/svg+xml"
  if capabilities['private-synchronous']:
      print "\tprivate-synchronous"
  if capabilities['append']:
      print "\tappend"
  if capabilities['private-icon-only']:
      print "\tprivate-icon-only"

  print "Notes:"
  if info["name"] == "notify-osd":
    print "\tx- and y-coordinates hints are ignored"
    print "\texpire-timeout is ignored"
    print "\tbody-markup is accepted but filtered"
  else:
    print "\tnone"

def message(title, text):
    if not pynotify.init("icon-summary-body"):
        sys.exit (1)
    # call this so we can savely use capabilities dictionary later
    initCaps ()
    # show what's supported
    printCaps ()
    # try the icon-summary-body case
    n = pynotify.Notification (title, text, "notification-message-im")

    n.show ()

#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from snipsTools import SnipsConfigParser
from hermes_python.hermes import Hermes
from hermes_python.ontology import *
import io
import requests
import time
import json

CONFIG_INI = "config.ini"
# If this skill is supposed to run on the satellite,
# please get this mqtt connection info from <config.ini>
# Hint: MQTT server is always running on the master device
MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

class FreeboxMultiRoom(object):
    """Class used to wrap action code with mqtt connection
        Please change the name refering to your application
    """

    def __init__(self):
        # get the configuration if needed

        try:
            self.config = SnipsConfigParser.read_configuration_file(CONFIG_INI)
        except :
            self.config = None

        self.hdnumber = self.config.get("secret").get("hdnumber")
        self.freeremotecode = self.config.get("secret").get("freeremotecode")
        self.defaultchannel = self.config.get("secret").get("defaultchannel")
        self.remoteaddr = 'http://hd'+self.hdnumber+'.freebox.fr/pub/remote_control?code='+self.freeremotecode
        
        # start listening to MQTT
        self.start_blocking()


    # --> Sub callback function, one per intent
    def ChgtEtat_callback(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")
        
        # action code goes here..
        print '[Url]'.format(self.remoteaddr)
        print '[Received] intent ChgtEtat: {}'.format(intent_message.intent.intent_name)
        requests.get(self.remoteaddr+'&key=power')
        time.sleep(1)
        requests.get(self.remoteaddr+'&key=home')
        time.sleep(.5)
        requests.get(self.remoteaddr+'&key=home')
        time.sleep(.5)
        requests.get(self.remoteaddr+'&key=ok')
        time.sleep(1)
        requests.get(self.remoteaddr+'&key=0')
        
        # if need to speak the execution result by tts
        hermes.publish_start_session_notification(intent_message.site_id, "changement etat effectue", "")

    def ChgtChaine_callback(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")

        # action code goes here...
        print '[Received] intent : {}'+format(intent_message.intent.intent_name)
        time.sleep(1)
        
        numchaine = intent_message.slots.chaine.first().value
        
        for digit in numchaine:
            requests.get(self.remoteaddr+'&key='+digit)
            time.sleep(.5)

    def VolInc_callback(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")

        # action code goes here...
        print '[Received] intent : {}'+format(intent_message.intent.intent_name)
        requests.get(self.remoteaddr+'&key=vol_inc&long=true')

    def VolDec_callback(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")

        # action code goes here...
        print '[Received] intent : {}'+format(intent_message.intent.intent_name)
        requests.get(self.remoteaddr+'&key=vol_dec&long=true')

    def MuteUnmute_callback(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")

        # action code goes here...
        print '[Received] intent : {}'+format(intent_message.intent.intent_name)
        requests.get(self.remoteaddr+'&key=mute')

    def LectAvanRap_callback(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")
        # action code goes here...
        print '[Received] intent : {}'+format(intent_message.intent.intent_name)
        requests.get(self.remoteaddr+'&key=fwd')

    def LectPlay_callback(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")
        # action code goes here...
        print '[Received] intent : {}'+format(intent_message.intent.intent_name)
        requests.get(self.remoteaddr+'&key=play')

    def LectRetRap_callback(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")
        # action code goes here...
        print '[Received] intent : {}'+format(intent_message.intent.intent_name)
        requests.get(self.remoteaddr+'&key=bwd')

    def PipAct_callback(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")
        # action code goes here...
        print '[Received] intent : {}'+format(intent_message.intent.intent_name)
        requests.get(self.remoteaddr+'&key=green')
        time.sleep(.25)
        requests.get(self.remoteaddr+'&key=down')
        time.sleep(.25)
        requests.get(self.remoteaddr+'&key=down')
        time.sleep(.25)
        requests.get(self.remoteaddr+'&key=down')
        time.sleep(.5)
        requests.get(self.remoteaddr+'&key=ok')
        time.sleep(.5)
        requests.get(self.remoteaddr+'&key=ok')

    def PipStop_callback(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")
        # action code goes here...
        print '[Received] intent : {}'+format(intent_message.intent.intent_name)
        requests.get(self.remoteaddr+'&key=green')
        time.sleep(.25)
        requests.get(self.remoteaddr+'&key=ok')

    def PipSwitch_callback(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")
        # action code goes here...
        print '[Received] intent : {}'+format(intent_message.intent.intent_name)
        requests.get(self.remoteaddr+'&key=red')

    def PrecChaine_callback(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")
        # action code goes here...
        print '[Received] intent : {}'+format(intent_message.intent.intent_name)
        requests.get(self.remoteaddr+'&key=prgm_dec')

    def SuivChaine_callback(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")
        # action code goes here...
        print '[Received] intent : {}'+format(intent_message.intent.intent_name)
        requests.get(self.remoteaddr+'&key=prgm_inc')

    def TsPause_callback(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")
        # action code goes here...
        print '[Received] intent : {}'+format(intent_message.intent.intent_name)
        requests.get(self.remoteaddr+'&key=play')

    def AffPrgTv_callback(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")
        # action code goes here...
        print '[Received] intent : {}'+format(intent_message.intent.intent_name)
        requests.get(self.remoteaddr+'&key=green')
        time.sleep(.5)
        requests.get(self.remoteaddr+'&key=down')
        time.sleep(.5)
        requests.get(self.remoteaddr+'&key=right')
        time.sleep(.5)
        requests.get(self.remoteaddr+'&key=ok')

    def SortPgTv_callback(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")
        # action code goes here...
        print '[Received] intent : {}'+format(intent_message.intent.intent_name)
        requests.get(self.remoteaddr+'&key=red')

    def TsDirect_callback(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")
        # action code goes here...
        print '[Received] intent : {}'+format(intent_message.intent.intent_name)
        requests.get(self.remoteaddr+'&key=green')
        requests.get(self.remoteaddr+'&key=ok')


# More callback function goes here...

    # --> Master callback function, triggered everytime an intent is recognized
    def master_intent_callback(self,hermes, intent_message):
             
        coming_intent = intent_message.intent.intent_name
        if coming_intent == 'cchalas:ChgtEtat':
            self.ChgtEtat_callback(hermes, intent_message)
        elif coming_intent == 'cchalas:ChgtChaine':
            self.ChgtChaine_callback(hermes, intent_message)
        elif coming_intent == 'cchalas:MuteUnmute':
            self.MuteUnmute_callback(hermes, intent_message)
        elif coming_intent == 'cchalas:AffPrgTv':
            self.AffPrgTv_callback(hermes, intent_message)
        elif coming_intent == 'cchalas:LectAvanRap':
            self.LectAvanRap_callback(hermes, intent_message)
        elif coming_intent == 'cchalas:LectPlay':
            self.LectPlay_callback(hermes, intent_message)
        elif coming_intent == 'cchalas:LectRetRap':
            self.LectRetRap_callback(hermes, intent_message)
        elif coming_intent == 'cchalas:PipAct':
            self.PipAct_callback(hermes, intent_message)
        elif coming_intent == 'cchalas:PipStop':
            self.PipStop_callback(hermes, intent_message)
        elif coming_intent == 'cchalas:PipSwitch':
            self.PipSwitch_callback(hermes, intent_message)
        elif coming_intent == 'cchalas:PrecChaine':
            self.PrecChaine_callback(hermes, intent_message)
        elif coming_intent == 'cchalas:SortPgTv':
            self.SortPgTv_callback(hermes, intent_message)
        elif coming_intent == 'cchalas:SuivChaine':
            self.SuivChaine_callback(hermes, intent_message)
        elif coming_intent == 'cchalas:TsDirect':
            self.TsDirect_callback(hermes, intent_message)
        elif coming_intent == 'cchalas:TsPause':
            self.TsPause_callback(hermes, intent_message)
        elif coming_intent == 'cchalas:VolDec':
            self.VolDec_callback(hermes, intent_message)
        elif coming_intent == 'cchalas:VolInc':
            self.VolInc_callback(hermes, intent_message)

        # more callback and if condition goes here...

    # --> Register callback function and start MQTT
    def start_blocking(self):
        with Hermes(MQTT_ADDR) as h:
            h.subscribe_intents(self.master_intent_callback).start()

if __name__ == "__main__":
    FreeboxMultiRoom()

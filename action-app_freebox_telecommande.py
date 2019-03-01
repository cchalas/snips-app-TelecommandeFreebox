#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import requests
import time
from snipsTools import SnipsConfigParser
from hermes_python.hermes import Hermes
from hermes_python.ontology import *
import io

CONFIG_INI = "config.ini"

# If this skill is supposed to run on the satellite,
# please get this mqtt connection info from <config.ini>
# Hint: MQTT server is always running on the master device
MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

class TelecommandeFreebox(object):
    """Class used to wrap action code with mqtt connection
        Please change the name refering to your application
    """

    def __init__(self):
        # get the configuration if needed
        try:
            self.config = SnipsConfigParser.read_configuration_file(CONFIG_INI)
            self.hdnumber = self.config.get("secret").get("hdnumber")
            self.freeremotecode = self.config.get("secret").get("freeremotecode")
            self.defaultchannel = self.config.get("secret").get("defaultchannel")
            self.defaultvolume = self.config.get("secret").get("defaultvolume")
            self.remoteaddr = 'http://hd'+self.hdnumber+'.freebox.fr/pub/remote_control?code='+self.freeremotecode
        except :
            self.config = None

        # start listening to MQTT
        self.start_blocking()

    def askFreeboxCommand_callback(self, hermes, intent_message):
        # terminate the session first if not continue

        print "Lancement de l'application Telecommandereebox"
        hermes.publish_end_session(intent_message.session_id, "")

        commandeFreebox = None
        subcommandeFreebox = None

        print '[Recep] intent value: {}'.format(intent_message.slots.TvCommand.first().value)

        #if intent_message.slots.TvChannel.first().value == 'oncle':
            #print '[Received] intent: {}'.format(intent_message.slots.TvChannel)
        commandeFreebox = intent_message.slots.TvCommand.first().value
        #subcommandeFreebox = intent_message.slots.TvSubCommand.first().value

        if commandeFreebox is None:
            telecommande_msg = "Je ne comprend pas ce que vous me demandez"
        #else:

        print "Channel"
        if commandeFreebox == 'power':
            self.powerFreebox()
        elif commandeFreebox == 'pip':
            self.pip()
        elif commandeFreebox == 'switchpip':
            self.switchPip()
        elif commandeFreebox == 'stopip':
            self.stopPip()
        elif commandeFreebox == 'direct':
            self.direct()
        elif commandeFreebox == 'rewind':
            self.rewind()
        elif commandeFreebox == 'forward':
            self.forward()
        elif (commandeFreebox == 'play') or (commandeFreebox == 'pause'):
            self.playPause()
        elif (commandeFreebox == 'mute') or (commandeFreebox =='unmute'):
            self.muteUnmute()
        elif commandeFreebox == 'volDown':
            self.volDown()
        elif commandeFreebox == 'volup':
            self.volUp()
        elif commandeFreebox == 'television' :
            self.television()
        elif commandeFreebox=='twitch':
            self.twitch()
        elif commandeFreebox == 'sortprogrammetv' :
            self.exitProgTv()
        elif commandeFreebox == 'programmetv':
            self.progTv()
        #elif (subcommandeFreebox is not None) and (subcommandeFreebox == 'chaîne'):
        #    if (commandeFreebox == 'next') :
        #        self.nextChannel()
        #    elif (commandeFreebox== 'previous'):
        #        self.previousChannel()
        elif (commandeFreebox == 'next'):
            self.right()
        elif (commandeFreebox == 'previous') :
            selft.left()
        else :
            self.channelChange(commandeFreebox)

            #telecommande_msg = 'J\'allume la télévision'
        # if need to speak the execution result by tts
        #    hermes.publish_start_session_notification(intent_message.site_id, telecommande_msg, "FreeboxTelecommande")
        #
    def nextChannel(self):
        time.sleep(1)
        requests.get(self.remoteaddr+'&key=prgm_inc')

    def previousChannel(self):
        time.sleep(1)
        requests.get(self.remoteaddr+'&key=prgm_dec')

    def left(self):
        time.sleep(1)
        requests.get(self.remoteaddr+'&key=left')

    def right(self):
        time.sleep(1)
        requests.get(self.remoteaddr+'&key=right')

    def next(self):
        time.sleep(1)
        requests.get(self.remoteaddr+'&KEY=next')

    def previous(self):
        requests.get(self.remoteaddr+'&KEY=prev')

    def powerFreebox(self):
        time.sleep(1)
        requests.get(self.remoteaddr+'&key=power')
        #If a default channel is set the freebox zap on it

        if self.defaultchannel != None :
            time.sleep(18)
            # If a default value for the volum is set then the freebox volume go to zeor and
            # step by step up
            if self.defaultvolume != None:
                self.volDown()
                self.volDown()
                self.volDown()
                self.volDown()
                for i in range(0,int(self.defaultvolume)) :
                        requests.get(self.remoteaddr+'&key=vol_inc')
            self.television()
            time.sleep(2)
            self.channelChange(self.defaultchannel)

    def switchPip(self):
        time.sleep(1)
        requests.get(self.remoteaddr+'&key=red')

    def stopPip(self):
        time.sleep(1)
        requests.get(self.remoteaddr+'&key=green')
        requests.get(self.remoteaddr+'&key=ok')

    def pip(self):
        time.sleep(1)
        requests.get(self.remoteaddr+'&key=yellow')
        time.sleep(1)
        requests.get(self.remoteaddr+'&key=yellow')
        time.sleep(1)
        requests.get(self.remoteaddr+'&key=right')
        time.sleep(1)
        requests.get(self.remoteaddr+'&key=ok')
        time.sleep(1)
        requests.get(self.remoteaddr+'&key=red')

    def direct(self):
        time.sleep(1)
        requests.get(self.remoteaddr+'&key=green')
        requests.get(self.remoteaddr+'&key=ok')

    def rewind(self):
        time.sleep(1)
        requests.get(self.remoteaddr+'&key=bwd&long=true')
        time.sleep(1)
        requests.get(self.remoteaddr+'&key=bwd&long=true')
        time.sleep(1)
        requests.get(self.remoteaddr+'&key=bwd&long=true')
        time.sleep(1)
        requests.get(self.remoteaddr+'&key=bwd&long=true')
        time.sleep(1)

    def forward(self):
        time.sleep(1)
        requests.get(self.remoteaddr+'&key=fwd&long=true')
        time.sleep(1)
        requests.get(self.remoteaddr+'&key=fwd&long=true')
        time.sleep(1)
        requests.get(self.remoteaddr+'&key=fwd&long=true')
        time.sleep(1)

    def playPause(self):
        time.sleep(1)
        requests.get(self.remoteaddr+'&key=play')

    def muteUnmute(self):
        time.sleep(1)
        requests.get(self.remoteaddr+'&key=mute')

    def volDown(self):
        time.sleep(1)
        requests.get(self.remoteaddr+'&key=vol_dec&long=true')

    def volUp(self):
        time.sleep(1)
        requests.get(self.remoteaddr+'&key=vol_inc&long=true')

    def television(self):
        time.sleep(1)
        requests.get(self.remoteaddr+'&key=home')
        time.sleep(1)
        requests.get(self.remoteaddr+'&key=home')
        time.sleep(1)
        requests.get(self.remoteaddr+'&key=ok')

    def exitProgTv(self):
        time.sleep(1)
        requests.get(self.remoteaddr+'&key=red')

    def progTv(self):
        time.sleep(1)
        requests.get(self.remoteaddr+'&key=home')
        time.sleep(1)
        requests.get(self.remoteaddr+'&key=home')
        time.sleep(2)
        requests.get(self.remoteaddr+'&key=ok')
        time.sleep(6)
        requests.get(self.remoteaddr+'&key=green')
        time.sleep(1)
        requests.get(self.remoteaddr+'&key=down')
        time.sleep(1)
        requests.get(self.remoteaddr+'&key=ok')
        time.sleep(1)
        requests.get(self.remoteaddr+'&key=ok')
        time.sleep(1)

    def twitch(selft):
        time.sleep(1)
        requests.get(self.remoteaddr+'&key=home')
        time.sleep(1)
        requests.get(self.remoteaddr+'&key=home')
        time.sleep(3)
        requests.get(self.remoteaddr+'&key=left')
        requests.get(self.remoteaddr+'&key=left')
        requests.get(self.remoteaddr+'&key=up')
        requests.get(self.remoteaddr+'&key=up')
        requests.get(self.remoteaddr+'&key=ok')
        time.sleep(4)
        requests.get(self.remoteaddr+'&key=down')
        requests.get(self.remoteaddr+'&key=down')
        requests.get(self.remoteaddr+'&key=down')
        requests.get(self.remoteaddr+'&key=down')


    def channelChange(self,commandeFreebox):
        time.sleep(1)
        for digit in commandeFreebox:
            requests.get(self.remoteaddr+'&key='+digit)

    # --> Master callback function, triggered everytime an intent is recognized
    def FreeboxTelecommande_callback(self,hermes, intent_message):
        coming_intent = intent_message.intent.intent_name

        print '[Recept] intent {}'.format(coming_intent)
        if coming_intent == 'cchalas:ChannelFreebox':
            self.askFreeboxCommand_callback(hermes, intent_message)
        # more callback and if condition goes here...

    # --> Register callback function and start MQTT
    def start_blocking(self):
        with Hermes(MQTT_ADDR) as h:
            h.subscribe_intents(self.FreeboxTelecommande_callback).start()

if __name__ == "__main__":
    TelecommandeFreebox()

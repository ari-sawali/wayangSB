# -*- coding: utf-8 -*-
from linepy import *
import json, time, random, tempfile, os, sys
from gtts import gTTS
from googletrans import Translator
from random import randint

if (sys.version_info < (3, 0)):
    print("The script requires Python 3x :( Sorry!\nrecommended using python 3.6")
    sys.exit()

from os import system, mkdir, getcwd, name
from os.path import exists, join
from textwrap import wrap

from PyLyrics import *

from importlib import reload

reload(sys)
print(sys.getdefaultencoding())

#===========================================================================================================================================#

# client = LINE(idOrAuthToken="YOUR_TOKEN_HERE")
client = LINE()
client.log("Auth Token : " + str(client.authToken))

channel = Channel(client,client.server.CHANNEL_ID['LINE_TIMELINE'])
client.log("Channel Access Token : " + str(channel.getChannelResult()))

poll = OEPoll(client)

#===========================================================================================================================================#


ki = LINE()
ki.log("Auth Token : " + str(ki.authToken))

kichannel = Channel(ki,ki.server.CHANNEL_ID['LINE_TIMELINE'])
ki.log("Channel Access Token : " + str(kichannel.getChannelResult()))

kipoll = OEPoll(ki)

#===========================================================================================================================================#

kc = LINE()
kc.log("Auth Token : " + str(kc.authToken))

kcchannel = Channel(kc,kc.server.CHANNEL_ID['LINE_TIMELINE'])
kc.log("Channel Access Token : " + str(kcchannel.getChannelResult()))

kcpoll = OEPoll(kc)

#===========================================================================================================================================#

kk = LINE()
kk.log("Auth Token : " + str(kk.authToken))

kkchannel = Channel(kk,kk.server.CHANNEL_ID['LINE_TIMELINE'])
kk.log("Channel Access Token : " + str(kkchannel.getChannelResult()))

kkpoll = OEPoll(kk)

#===========================================================================================================================================#

ks = LINE()
ks.log("Auth Token : " + str(ks.authToken))

kschannel = Channel(ks,ks.server.CHANNEL_ID['LINE_TIMELINE'])
ks.log("Channel Access Token : " + str(kschannel.getChannelResult()))

kspoll = OEPoll(ks)

#===========================================================================================================================================#

cl = client

KAC=[cl,ki,kc,kk,ks]

mid = cl.getProfile().mid #fahri
Amid = ki.getProfile().mid #felly
Bmid = kc.getProfile().mid #anuan
Cmid = kk.getProfile().mid #andi
Dmid = ks.getProfile().mid #agus


Bots=[mid,Amid,Bmid,Cmid,Dmid]

contact = cl.getProfile()
backup = cl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

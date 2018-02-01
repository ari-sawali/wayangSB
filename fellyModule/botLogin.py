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

# client = LINE()
client = LINE(idOrAuthToken="EoJPgSeHvsijHevWfNg0.JUROxzdkKD3c/MrJQ951aa.XP0n+ARFU3JwM4KQhwAKO+Um5B5ynYkkfM7FWDIvTwM=")
client.log("Auth Token : " + str(client.authToken))

channel = Channel(client,client.server.CHANNEL_ID['LINE_TIMELINE'])
client.log("Channel Access Token : " + str(channel.getChannelResult()))

poll = OEPoll(client)

#===========================================================================================================================================#


ki = LINE(idOrAuthToken="EoMtt6VIOE1d6jeoSBh7.mMD8f775uswF2ssZgJVO5W.dz4oOVIUEkF/LUZ57i7LHr7HFhfUUf4FjEARlu5RyKM=")
ki.log("Auth Token : " + str(ki.authToken))

kichannel = Channel(ki,ki.server.CHANNEL_ID['LINE_TIMELINE'])
ki.log("Channel Access Token : " + str(kichannel.getChannelResult()))

kipoll = OEPoll(ki)

#===========================================================================================================================================#

kc = LINE(idOrAuthToken="Eo701j074Rhsk3TNyud1.tBjPCY+fboP36y18qiobCq.ScwpDrj0jTlDEok/yyh0dVsx12OpuB0iylQC36pDJUA=")
kc.log("Auth Token : " + str(kc.authToken))

kcchannel = Channel(kc,kc.server.CHANNEL_ID['LINE_TIMELINE'])
kc.log("Channel Access Token : " + str(kcchannel.getChannelResult()))

kcpoll = OEPoll(kc)

#===========================================================================================================================================#

kk = LINE(idOrAuthToken="Eo6ZRHUWmb5D7JxEj37e.AkOpRusKp1cn5G+jz324xG.YYHowNjUgs2nhZuN22VqJgI22jj07Ir1HOsdenYLp3E=")
kk.log("Auth Token : " + str(kk.authToken))

kkchannel = Channel(kk,kk.server.CHANNEL_ID['LINE_TIMELINE'])
kk.log("Channel Access Token : " + str(kkchannel.getChannelResult()))

kkpoll = OEPoll(kk)

#===========================================================================================================================================#

ks = LINE(idOrAuthToken="Eo2oeDNcTl57BahHw9rc.75kstEi+SaAxRZV8LISJRa.iIStGfr9ak5XloQOQRJiADCoFjRUHidrPNZhCGcr/YU=")
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
# -*- coding: utf-8 -*-
from linepy import *
import json, time, random, tempfile, os, sys
from gtts import gTTS
from googletrans import Translator
from random import randint

# if (sys.version_info > (3, 0)):
#     print "The script requires Python 2 :( Sorry!"
#     sys.exit()

from os import system, mkdir, getcwd, name
from os.path import exists, join
from textwrap import wrap

# try:
#     from wand.drawing import Drawing
#     from wand.image import Image
#     from wand.color import Color
# except:
#     print "Error importing Wand! Try installing it with 'pip install wand'"
#     sys.exit()

client = LINE()
channel = Channel(client,client.server.CHANNEL_ID['LINE_TIMELINE'])
client.log("Channel Access Token : " + str(channel.getChannelResult()))
poll = OEPoll(client)

mode='autojoin'
cctv={
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

wait={
    "lang":"JP",
    "joinedBoT":"",
    "groupId":"c17e7586a41eb78afc268626e85f15e2d"
}

boten=["ueff8f78401c867593c6ddc8aeb8c649d","u9fec89015e171bc9a8f82ce1ded83075","ubb4183ea6b5c541817eaa3e6a8c6acfe"]
owner=["u8eeae85d90ca91ddc2fa6463abde7500"]

cl = client

while True:
    try:
        ops=poll.singleTrace(count=50)
        # print ops
        # print "\n"
        if ops != None:
          for op in ops:
#=========================================================================================================================================#
            # if op.type in OpType._VALUES_TO_NAMES:
            #    print "[ {} ] {}".format(str(op.type), str(OpType._VALUES_TO_NAMES[op.type]))
#=========================================================================================================================================#
            if mode == 'autojoin' and op.type == 26:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                try:
                    if msg._from in boten:
                        if msg.to == wait["groupId"]:
                            if msg.contentType == 4:
                                mes=str(msg.contentMetadata)
                                mes=mes.replace("{","")
                                mes=mes.replace("}","")
                                mesindex=mes.find('/join')
                                if mesindex == -1:
                                    pass
                                else:
                                    temp_txt=mes[mesindex:]
                                    arr_temp=temp_txt.split(" ")
                                    txt=arr_temp[0]+" "+arr_temp[1]
                                    print(txt)
                                    print("\n\n")
                                    time.sleep(randint(1,10))
                                    cl.sendText(msg._from,(txt))
                            else:
                                pass
                        else:
                            pass
                except Exception as e:
                    client.log("[AUTO JOIN] ERROR : " + str(e))
#==========================Fungsi Memebuzz Start==========================================================================================#
            elif op.type == 25:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                try:
                    if ".getjoinedgroup" in text.lower():
                        try:
                            x=cl.getGroupIdsJoined()
                            z="List Joined Group\n\n"
                            num=1
                            for y in x:
                                g = cl.getCompactGroup(y)
                                print(g)
                                print("\n")
                                z += "GName : " +g.name+"\nGId: "+g.id+"\n\n"
                                num=num+1
                            print("[COMMAND]GET JOINED GROUP EXECUTED\n")
                            cl.sendMessage(receiver,z)
                        except Exception as e:
                            cl.sendMessage(receiver,str(e))
                    elif ".getgroupid " in text.lower():
                        try:
                            gname=text.replace(".getgroupid ","")
                            x=cl.getGroupIdsByName(gname)
                            print("[COMMAND]GET GROUP ID EXECUTED\n")
                            cl.sendMessage(receiver,str(x))
                        except Exception as e:
                            cl.sendMessage(receiver,str(e))

                except Exception as e:
                    client.log("[GET GROUP] ERROR : " + str(e))
#=========================================================================================================================================#
            # Don't remove this line, if you wan't get error soon!
            poll.setRevision(op.revision)
            
    except Exception as e:
        client.log("[SINGLE_TRACE] ERROR : " + str(e))

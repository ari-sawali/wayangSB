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

try:
    from wand.drawing import Drawing
    from wand.image import Image
    from wand.color import Color
except:
    print "Error importing Wand! Try installing it with 'pip install wand'"
    sys.exit()

client = LineClient()
# client = LineClient(id='EMAIL', passwd='PASSWORD')
#client = LineClient(authToken='AUTHTOKEN')
# client = LineClient(authToken="EoEsUZmtP3F0iONKCbe0.JUROxzdkKD3c/MrJQ951aa.HEvGX5zeyF1AHTa6FyWijN4aAa5hS36LuPVrir2tb18=")
client.log("Auth Token : " + str(client.authToken))

channel = LineChannel(client)
client.log("Channel Access Token : " + str(channel.channelAccessToken))

poll = LinePoll(client)

mode='autojoin'
cctv={
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

wait={
    "lang":"JP",
    "joinedBoT":"",
    "groupId":""
}

boten=["ueff8f78401c867593c6ddc8aeb8c649d","u9fec89015e171bc9a8f82ce1ded83075","ubb4183ea6b5c541817eaa3e6a8c6acfe"]
owner=["u8eeae85d90ca91ddc2fa6463abde7500"]

cl = client

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def get_warp_length(width):
    return int((33.0 / 500.0) * (width + 0.0))
    
def generate_meme(upper_text, lower_text, picture_name):
    MEME_FOLDER = "memes"
    MARGINS = [25, 65, 100, 135, 170]

    if not exists(join(getcwd(), MEME_FOLDER)):
        mkdir(join(getcwd(), MEME_FOLDER))

    main_image = Image(filename=picture_name)
    main_image.resize(500, int(((main_image.height * 1.0) / (main_image.width * 1.0)) * 500.0))

    upper_text = "\n".join(wrap(upper_text, get_warp_length(main_image.width))).upper()
    lower_text = "\n".join(wrap(lower_text, get_warp_length(main_image.width))).upper()
    lower_margin = MARGINS[lower_text.count("\n")]

    text_draw = Drawing()

    text_draw.font = join(getcwd(), "impact.ttf")
    text_draw.font_size = 40
    text_draw.text_alignment = "center"
    text_draw.stroke_color = Color("black")
    text_draw.stroke_width = 3
    text_draw.fill_color = Color("white")

    if upper_text:
        text_draw.text(main_image.width / 2, 40, upper_text)
    if lower_text:
        text_draw.text(main_image.width / 2, main_image.height - lower_margin, lower_text)

    text_draw(main_image)

    outname = "[MEME] " + picture_name
    main_image.save(filename=join(getcwd(), MEME_FOLDER, outname))

    # if sys.platform.startswith('darwin'):
    #     system('open "%s"' % (join(getcwd(), MEME_FOLDER, outname)))
    # elif name == 'nt':
    #     system('start "%s"' % (join(getcwd(), MEME_FOLDER, outname)))
    # elif name == 'posix':
    #     system('xdg-open "%s"' % (join(getcwd(), MEME_FOLDER, outname)))
    # else:
    #     pass
    return MEME_FOLDER+'/'+outname

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
            if mode == 'autojoin' and op.type == 25:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                try:
                    if ".mbuzz " in msg.text:
                      if sender in owner:
                        meme_txt = msg.text.replace(".mbuzz ","")
                        text=meme_txt.split("|")
                        print text
                        upper_text=str(text[1])
                        lower_text=str(text[2])
                        img_name="buzz.jpg"
                        genMeme=generate_meme(upper_text,lower_text,img_name)
                        print genMeme
                        cl.sendImage(receiver,genMeme)
                except Exception as e:
                    client.log("[MEME GENERATE] ERROR : " + str(e))
#=========================================================================================================================================#
            # Don't remove this line, if you wan't get error soon!
            poll.setRevision(op.revision)
            
    except Exception as e:
        client.log("[SINGLE_TRACE] ERROR : " + str(e))

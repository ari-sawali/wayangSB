# -*- coding: utf-8 -*-
from linepy import *
import json, time, random, tempfile, os, sys
from gtts import gTTS
from googletrans import Translator

# client = LineClient()
# client = LineClient(id='EMAIL', passwd='PASSWORD')
#client = LineClient(authToken='AUTHTOKEN')
client = LineClient(authToken="Eo3usB8sDLAZq6Cv2Qq7.mMD8f775uswF2ssZgJVO5W.Od060NaT5WI/FQz61mwAVJeH3RbcH/wSfiIBLy/x4HI=")
client.log("Auth Token : " + str(client.authToken))

channel = LineChannel(client)
client.log("Channel Access Token : " + str(channel.channelAccessToken))

poll = LinePoll(client)

#===========================================================================================================================================#

# ki = LineClient()
ki = LineClient(authToken="EoKD9XkERA0jLwAjsht1.tBjPCY+fboP36y18qiobCq.GcMiArb7omZM7RwuPrNrg0MKcJD9fEXa4ttjBQsDRik=")
ki.log("Auth Token : " + str(ki.authToken))

kichannel = LineChannel(ki)
ki.log("Channel Access Token : " + str(kichannel.channelAccessToken))

kipoll = LinePoll(ki)

#===========================================================================================================================================#

mode='self'
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

cl = client

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

while True:
    try:
        ops=poll.singleTrace(count=50)
        # print ops
        # print "\n"
        if ops != None:
          for op in ops:
#=========================================================================================================================================#
            #if op.type in OpType._VALUES_TO_NAMES:
            #    print("[ {} ] {}".format(str(op.type), str(OpType._VALUES_TO_NAMES[op.type])))
#=========================================================================================================================================#
            if op.type == 25:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                try:
                    if msg._from in boten:
                        print "msg from boten ok"
                        if msg.contentType == 4:
                            print msg.contentMetadata
                            print "\n"
                    elif msg.contentType == 0:
                        if msg.toType == 2:
                            client.sendChatChecked(receiver, msg_id)
                            contact = client.getContact(sender)
                            if text.lower() == 'me':
                                client.sendMessage(receiver, None, contentMetadata={'mid': sender}, contentType=13)
                                client.tag(receiver, sender)
                            elif 'lc ' in text.lower():
                                try:
                                    typel = [1001,1002,1003,1004,1005,1006]
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = client.getContact(u).mid
                                    s = client.getContact(u).displayName
                                    hasil = channel.getHomeProfile(mid=a)
                                    st = hasil['result']['feeds']
                                    for i in range(len(st)):
                                        test = st[i]
                                        result = test['post']['postInfo']['postId']
                                        channel.like(str(sender), str(result), likeType=random.choice(typel))
                                        channel.comment(str(sender), str(result), 'Auto Like by nrik')
                                    client.sendText(receiver, 'Done Like+Comment '+str(len(st))+' Post From' + str(s))
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif 'gc ' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    cname = client.getContact(u).displayName
                                    cmid = client.getContact(u).mid
                                    cstatus = client.getContact(u).statusMessage
                                    cpic = client.getContact(u).picturePath
                                    #print(str(a))
                                    client.sendText(receiver, 'Nama : '+cname+'\nMID : '+cmid+'\nStatus Msg : '+cstatus+'\nPicture : http://dl.profile.line.naver.jp'+cpic)
                                    client.sendMessage(receiver, None, contentMetadata={'mid': cmid}, contentType=13)
                                    if "videoProfile='{" in str(client.getContact(u)):
                                        client.sendVideoWithURL(receiver, 'http://dl.profile.line.naver.jp'+cpic+'/vp.small')
                                    else:
                                        client.sendImageWithURL(receiver, 'http://dl.profile.line.naver.jp'+cpic)
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif 'sticker:' in msg.text.lower():
                                try:
                                    query = msg.text.replace("sticker:", "")
                                    query = int(query)
                                    if type(query) == int:
                                        client.sendImageWithURL(receiver, 'https://stickershop.line-scdn.net/stickershop/v1/product/'+str(query)+'/ANDROID/main.png')
                                        client.sendText(receiver, 'https://line.me/S/sticker/'+str(query))
                                    else:
                                        client.sendText(receiver, 'gunakan key sticker angka bukan huruf')
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif "yt:" in msg.text.lower():
                                try:
                                    query = msg.text.replace("yt:", "")
                                    query = query.replace(" ", "+")
                                    x = client.youtube(query)
                                    client.sendText(receiver, x)
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif "image:" in msg.text.lower():
                                try:
                                    query = msg.text.replace("image:", "")
                                    images = client.image_search(query)
                                    client.sendImageWithURL(receiver, images)
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif 'say:' in msg.text.lower():
                                try:
                                    isi = msg.text.lower().replace('say:','')
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp.mp3')
                                    client.sendAudio(receiver, 'temp.mp3')
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif 'apakah ' in msg.text.lower():
                                try:
                                    txt = ['iya','tidak','bisa jadi']
                                    isi = random.choice(txt)
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp2.mp3')
                                    client.sendAudio(receiver, 'temp2.mp3')
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif "sytr:" in msg.text:
                                try:
                                    isi = msg.text.split(":")
                                    translator = Translator()
                                    hasil = translator.translate(isi[2], dest=isi[1])
                                    A = hasil.text
                                    tts = gTTS(text=A, lang=isi[1], slow=False)
                                    tts.save('temp3.mp3')
                                    client.sendAudio(receiver, 'temp3.mp3')
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif "tr:" in msg.text:
                                try:
                                    isi = msg.text.split(":")
                                    translator = Translator()
                                    hasil = translator.translate(isi[2], dest=isi[1])
                                    A = hasil.text                               
                                    client.sendText(receiver, str(A))
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif text.lower() == 'speed':
                                start = time.time()
                                client.sendText(receiver, "TestSpeed")
                                elapsed_time = time.time() - start
                                client.sendText(receiver, "%sdetik" % (elapsed_time))
                            elif 'spic' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = client.getContact(u).pictureStatus
                                    if "videoProfile='{" in str(client.getContact(u)):
                                        client.sendVideoWithURL(receiver, 'http://dl.profile.line.naver.jp/'+a+'/vp.small')
                                    else:
                                        client.sendImageWithURL(receiver, 'http://dl.profile.line.naver.jp/'+a)
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif 'scover' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = channel.getProfileCoverURL(mid=u)
                                    client.sendImageWithURL(receiver, a)
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif text.lower() == 'tagall':
                                group = client.getGroup(receiver)
                                nama = [contact.mid for contact in group.members]
                                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                                if jml <= 100:
                                    client.mention(receiver, nama)
                                if jml > 100 and jml < 200:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    client.mention(receiver, nm1)
                                    for j in range(101, len(nama)):
                                        nm2 += [nama[j]]
                                    client.mention(receiver, nm2)
                                if jml > 200 and jml < 300:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    client.mention(receiver, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    client.mention(receiver, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    client.mention(receiver, nm3)
                                if jml > 300 and jml < 400:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    client.mention(receiver, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    client.mention(receiver, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    client.mention(receiver, nm3)
                                    for l in range(301, len(nama)):
                                        nm4 += [nama[l]]
                                    client.mention(receiver, nm4)
                                if jml > 400 and jml < 501:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    client.mention(receiver, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    client.mention(receiver, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    client.mention(receiver, nm3)
                                    for l in range(301, len(nama)):
                                        nm4 += [nama[l]]
                                    client.mention(receiver, nm4)
                                    for m in range(401, len(nama)):
                                        nm5 += [nama[m]]
                                    client.mention(receiver, nm5)             
                                client.sendText(receiver, "Members :"+str(jml))
                            elif text.lower() == 'ceksider':
                                try:
                                    del cctv['point'][receiver]
                                    del cctv['sidermem'][receiver]
                                    del cctv['cyduk'][receiver]
                                except:
                                    pass
                                cctv['point'][receiver] = msg.id
                                cctv['sidermem'][receiver] = ""
                                cctv['cyduk'][receiver]=True
                            elif text.lower() == 'offread':
                                if msg.to in cctv['point']:
                                    cctv['cyduk'][receiver]=False
                                    client.sendText(receiver, cctv['sidermem'][msg.to])
                                else:
                                    client.sendText(receiver, "Heh belom di Set")
                            elif text.lower() == 'mode:self':
                                mode = 'self'
                                client.sendText(receiver, 'Mode Public Off')
                            elif text.lower() == 'mode:public':
                                mode = 'public'
                                client.sendText(receiver, 'Mode Public ON')
                            elif text.lower() == 'mode:autojoin':
                                mode = 'autojoin'
                                client.sendText(receiver, 'Mode Auto Join ON')
                            elif text.lower() == 'restart':
                                restart_program()
                            elif msg.text in [".setbotkuy"]:
                                group = cl.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members]
                                cb = ""
                                cb2 = ""
                                strt = int(0)
                                akh = int(0)
                                for md in nama:
                                    if md in boten:
                                      print "boten md is : "+md+"\n"
                                      wait["joinedBoT"] = md
                                      gCreator = group.creator.displayName
                                      if wait["lang"] == "JP":
                                        if group.invitee is None:
                                          sinvitee = "0"
                                        else:
                                          sinvitee = str(len(group.invitee))
                                        if group.preventJoinByTicket == True:
                                          QR = "Close"
                                        else:
                                          QR = "Open" 
                                      wait["groupId"] = group.id
                                      cl.sendText(msg.to, "Battle of Ten sudah di set")
                                      # msg.contentType = 13
                                      # msg.contentMetadata = {'mid': md}
                                      # cl.sendText(msg.to,"=============================")
                                      # cl.sendMessage(msg.to, None, contentMetadata={'mid': md}, contentType=13)
                                      # # cl.sendText(msg.to,"[Group Name]\n" + "[•]" + str(group.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + "[•]" + gCreator + "\n\n[Group Status]\n" + "[•]Status QR =>" + QR + "\n\n[Group Picture]\nhttp://dl.profile.line.naver.jp/" + group.pictureStatus + "\n\nMembers:" + str(len(group.members)) + "\nPending:" + sinvitee)
                                      # cl.sendText(msg.to,"=============================")
                                      # cl.sendText(msg.to,"=====Wayang Dugem Uhuiii=====")
                                      print wait["joinedBoT"]+"\n"
                                      print wait["groupId"]
                                      print "\n"
                except Exception as e:
                    client.log("[SEND_MESSAGE] ERROR : " + str(e))
#=========================================================================================================================================#
            elif mode == 'public' and op.type == 26:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                try:
                    if msg._from in boten:
                        print "msg from boten ok"
                        if msg.contentType == 4:
                            print json.dumps(msg.contentMetadata)
                            print "\n"
                            mes=str(msg.contentMetadata)
                            mes=mes.replace("{","")
                            mes=mes.replace("}","")
                            # txt=mes.split(":")
                            mesindex=mes.find('/join')
                            temp_txt=mes[mesindex:]
                            arr_temp=temp_txt.split(" ")
                            txt=arr_temp[0]+" "+arr_temp[1]
                            print txt
                            print "\n\n"
                    elif msg.contentType == 0:
                        if msg.toType == 2:
                            client.sendChatChecked(receiver, msg_id)
                            contact = client.getContact(sender)
                            if text.lower() == 'me':
                                client.sendMessage(receiver, None, contentMetadata={'mid': sender}, contentType=13)
                                client.tag(receiver, sender)
                            elif 'gc ' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    cname = client.getContact(u).displayName
                                    cmid = client.getContact(u).mid
                                    cstatus = client.getContact(u).statusMessage
                                    cpic = client.getContact(u).picturePath
                                    #print(str(a))
                                    client.sendText(receiver, 'Nama : '+cname+'\nMID : '+cmid+'\nStatus Msg : '+cstatus+'\nPicture : http://dl.profile.line.naver.jp'+cpic)
                                    client.sendMessage(receiver, None, contentMetadata={'mid': cmid}, contentType=13)
                                    if "videoProfile='{" in str(client.getContact(u)):
                                        client.sendVideoWithURL(receiver, 'http://dl.profile.line.naver.jp'+cpic+'/vp.small')
                                    else:
                                        client.sendImageWithURL(receiver, 'http://dl.profile.line.naver.jp'+cpic)
                                except Exception as e:
                                    client.sendText(receiver, str(e))                            
                            elif 'sticker:' in msg.text.lower():
                                try:
                                    query = msg.text.replace("sticker:", "")
                                    query = int(query)
                                    if type(query) == int:
                                        client.sendImageWithURL(receiver, 'https://stickershop.line-scdn.net/stickershop/v1/product/'+str(query)+'/ANDROID/main.png')
                                        client.sendText(receiver, 'https://line.me/S/sticker/'+str(query))
                                    else:
                                        client.sendText(receiver, 'gunakan key sticker angka bukan huruf')
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif "yt:" in msg.text.lower():
                                try:
                                    query = msg.text.replace("yt:", "")
                                    query = query.replace(" ", "+")
                                    x = client.youtube(query)
                                    client.sendText(receiver, x)
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif "image:" in msg.text.lower():
                                try:
                                    query = msg.text.replace("image:", "")
                                    images = client.image_search(query)
                                    client.sendImageWithURL(receiver, images)
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif 'say:' in msg.text.lower():
                                try:
                                    isi = msg.text.lower().replace('say:','')
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp.mp3')
                                    client.sendAudio(receiver, 'temp.mp3')
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif 'apakah ' in msg.text.lower():
                                try:
                                    txt = ['iya','tidak','bisa jadi']
                                    isi = random.choice(txt)
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp2.mp3')
                                    client.sendAudio(receiver, 'temp2.mp3')
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif "sytr:" in msg.text:
                                try:
                                    isi = msg.text.split(":")
                                    translator = Translator()
                                    hasil = translator.translate(isi[2], dest=isi[1])
                                    A = hasil.text
                                    tts = gTTS(text=A, lang=isi[1], slow=False)
                                    tts.save('temp3.mp3')
                                    client.sendAudio(receiver, 'temp3.mp3')
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif "tr:" in msg.text:
                                try:
                                    isi = msg.text.split(":")
                                    translator = Translator()
                                    hasil = translator.translate(isi[2], dest=isi[1])
                                    A = hasil.text                               
                                    client.sendText(receiver, str(A))
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif text.lower() == 'speed':
                                start = time.time()
                                client.sendText(receiver, "TestSpeed")
                                elapsed_time = time.time() - start
                                client.sendText(receiver, "%sdetik" % (elapsed_time))
                            elif 'spic' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = client.getContact(u).pictureStatus
                                    if "videoProfile='{" in str(client.getContact(u)):
                                        client.sendVideoWithURL(receiver, 'http://dl.profile.line.naver.jp/'+a+'/vp.small')
                                    else:
                                        client.sendImageWithURL(receiver, 'http://dl.profile.line.naver.jp/'+a)
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif 'scover' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = channel.getProfileCoverURL(mid=u)
                                    client.sendImageWithURL(receiver, a)
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                except Exception as e:
                    client.log("[SEND_MESSAGE] ERROR : " + str(e))
#=========================================================================================================================================#
            elif mode == 'autojoin' and op.type == 26:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                try:
                    if msg._from in boten:
                        if msg.contentType == 4:
                            group=cl.getGroup(msg.to)
                            if group.id == wait["groupId"]:
                                print "Joined BoT : "+wait["joinedBoT"]+"\n"
                                print "Group ID : "+wait["groupId"]+"\n"
                                print "msg from boten ok"
                                print json.dumps(msg.contentMetadata)
                                print "\n"
                                mes=str(msg.contentMetadata)
                                mes=mes.replace("{","")
                                mes=mes.replace("}","")
                                # txt=mes.split(":")
                                mesindex=mes.find('/join')
                                if mesindex == -1:
                                    pass
                                else:
                                    temp_txt=mes[mesindex:]
                                    arr_temp=temp_txt.split(" ")
                                    txt=arr_temp[0]+" "+arr_temp[1]
                                    print txt
                                    print "\n\n"
                                    cl.sendText(wait["joinedBoT"],(txt))
                                    ki.sendText(wait["joinedBoT"],(txt))
                            else:
                                pass
                except Exception as e:
                    client.log("[SEND_MESSAGE] ERROR : " + str(e))
#=========================================================================================================================================#
            elif op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = client.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n~ " + Name
                                pref=['eh ada','hai kak','aloo..','nah','lg ngapain','halo','sini kak']
                                client.sendText(op.param1, str(random.choice(pref))+' '+Name)
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

            else:
                pass
#=========================================================================================================================================#
            # Don't remove this line, if you wan't get error soon!
            poll.setRevision(op.revision)
            
    except Exception as e:
        client.log("[SINGLE_TRACE] ERROR : " + str(e))

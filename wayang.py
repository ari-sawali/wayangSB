# -*- coding: utf-8 -*-
from linepy import *
from fellyModule.botLogin import *
from fellyModule.botCfg import *
from fellyModule.botFunction import *
import logging
from threading import Thread

def restart_program():
    venvprog = "/usr/bin/python3.6 /home/fahri/LineBot/wayangDev/wayang.py"
    os.execl(venvprog, * sys.argv)

def shutdown():
    sys.exit()

def cooldownHStore(n,usermid):
    print("[HSTORE]["+time.strftime("%Y-%m-%d %H:%M:%S")+"] : Cooldown Start\n")
    time.sleep(n)
    autoHStore[usermid]['cooldown']=False
    print("[HSTORE]["+time.strftime("%Y-%m-%d %H:%M:%S")+"] : Cooldown Finish\n")
    # fellyCfgUpdate()

def cekHStore():
    while True:
        # print("cek autoHStore Running\n")
        try:
            if autoHStore!={}:
                if mid in autoHStore:
                    if autoHStore[mid]['start']==True:
                        try:
                            if autoHStore[mid]['cooldown']==False:
                                print("[HSTORE]["+time.strftime("%Y-%m-%d %H:%M:%S")+"] : Send /hstore Command")
                                cl.sendMessage(autoHStore[mid]['server'],'/hstore')
                                print("[HSTORE]["+time.strftime("%Y-%m-%d %H:%M:%S")+"] : Send Command Done")
                                autoHStore[mid]['cooldown']=True
                                # fellyCfgUpdate()
                                cooldownHStore(180,mid)
                            elif autoHStore[mid]['cooldown']==True:
                                autoHStore[mid]['cooldown']=False
                            else:
                                pass
                        except Exception as e:
                            print("[HSTORE]["+time.strftime("%Y-%m-%d %H:%M:%S")+"] : Error "+str(e))
                    else:
                        pass
                else:
                    pass
            else:
                pass
            # print("cek autoHStore Still Running\n")
        except Exception as e:
            print("[CEK HSTORE ERROR]["+time.strftime("%Y-%m-%d %H:%M:%S")+"] : "+str(e)+"\n\n")
# logging.basicConfig(filename='fellyLog/op.log',level=logging.DEBUG)

def bot(op):
                # logging.debug(op)
                # print op
    #=========================================================================================================================================#
                # if op.type in OpType._VALUES_TO_NAMES:
                #    print "[ {} ] {}".format(str(op.type), str(OpType._VALUES_TO_NAMES[op.type]))
    #=========================================================================================================================================#
    #
    #=========================================================================================================================================#
                #Owner Command
    #=========================================================================================================================================#                
                if op.type == 25:
                    msg = op.message
                    text = msg.text
                    msg_id = msg.id
                    receiver = msg.to
                    sender = msg._from
                    try:
                        if msg.contentType == 0:
                            #Command dibawah bisa digunakan di grup atau di pm
                            if text.lower() == '.restart wayang':
                                if sender in owner:
                                    print("Trying Restart")
                                    cl.sendMessage(receiver,"Restarting Wayang")
                                    wait["bigAj"]={}
                                    restartVar['isRestart'] = True
                                    restartVar['restartIn'] = str(receiver)
                                    fellyCfgUpdate()
                                    restart_program()
                                else:
                                    cl.sendMessage(receiver,"Ngapain cuk??\nOwner doang yg bisa restart :p")
                            elif text.lower() == '.shutdown wayang':
                                if sender in owner:
                                    print("Trying Shutdown")
                                    wait["bigAj"]={}
                                    cl.sendMessage(receiver,"Preparing Shutdown")
                                    time.sleep(randint(0,2))
                                    cl.sendMessage(receiver,"Updating Config")
                                    fellyCfgUpdate()
                                    time.sleep(randint(0,2))
                                    cl.sendMessage(receiver,"See You...")
                                    shutdown()
                                else:
                                    cl.sendMessage(receiver,"Ngapain cuk??\nOwner doang yg bisa restart :p")
                            elif ".getsq" in text.lower():
                                try:
                                    x=cl.getJoinedSquares()
                                    print(x)
                                except Exception as e:
                                    client.sendMessage(receiver, str(e))
                            elif ".getsqchat" in text.lower():
                                try:
                                    x=cl.getJoinableSquareChats('s3825e0558cc9b4598fb9f557e113eeb1',continuationToken=None, limit=50)
                                    print(x)
                                except Exception as e:
                                    client.sendMessage(receiver,str(e))
                            elif ".getsqmember" in text.lower():
                                try:
                                    x=cl.getSquareMember('p6c69551c4a0cac4f8c3bc2b3c7db948d')
                                    print(x)
                                except Exception as e:
                                    client.sendMessage(receiver,str(e))
                            elif ".getjoinedgroup" in text.lower():
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
                            elif ".yt " in msg.text.lower():
                                try:
                                    query = msg.text.replace(".yt ", "")
                                    query = query.replace(" ", "+")
                                    x = client.youtube(query)
                                    client.sendMessage(receiver, x)
                                except Exception as e:
                                    client.sendMessage(receiver, str(e))
                            elif ".album " in msg.text.lower():
                                try:
                                    query = msg.text.replace(".album ", "")
                                    x = getAlbums(query)
                                    client.sendMessage(receiver, x)
                                except Exception as e:
                                    client.sendMessage(receiver, str(e))
                            elif ".track " in msg.text.lower():
                                try:
                                    query = msg.text.replace(".track ", "")
                                    x = getTracks(query)
                                    client.sendMessage(receiver, x)
                                except Exception as e:
                                    client.sendMessage(receiver, str(e))
                            elif ".lirik " in msg.text.lower():
                                try:
                                    query = msg.text.replace(".lirik ", "")
                                    x = getLyrics(query)
                                    client.sendMessage(receiver, x)
                                except Exception as e:
                                    client.sendMessage(receiver, str(e))
                            elif ".img " in msg.text.lower():
                                try:
                                    query = msg.text.replace(".img ", "")
                                    images = client.image_search(query)
                                    client.sendImageWithURL(receiver, images)
                                except Exception as e:
                                    client.sendMessage(receiver, str(e))
                            elif ".meme " in text.lower():
                                try:
                                    query = text.replace(".meme ","")
                                    qry = query.split("|")
                                    font = "impact"
                                    templ_id = int(qry[0])
                                    templ_id = templ_id-1
                                    upper_text = qry[1]
                                    lower_text = qry[2]
                                    if len(qry) == 4:
                                        font = qry[3]
                                    getTemplate=get_memes()
                                    template_id=getTemplate[templ_id]['id']
                                    genMeme=imgflipMeme(upper_text,lower_text,template_id,font)
                                    client.sendImageWithURL(receiver,genMeme['url'])
                                except Exception as e:
                                    client.sendMessage(receiver,str(e))
                            elif ".meme_template " in text.lower():
                                try:
                                    txt=text.replace(".meme_template ","")
                                    x=txt.split("-")
                                    start=int(x[0])
                                    y=start-1
                                    end=int(x[1])
                                    if end>100:
                                        client.sendMessage(receiver,"Maksimal 100")
                                    else:
                                        getTemplate=get_memes()
                                        listtemp="List Template Meme\n\n"
                                        for i in range(y,end):
                                            a=i+1
                                            listtemp += str(a) + " . " + getTemplate[i]['name'] + "\n"
                                        client.sendMessage(receiver,listtemp)
                                except Exception as e:
                                    client.sendMessage(receiver,str(e))
                            elif ".view_template " in text.lower():
                                try:
                                    txt=text.replace(".view_template ","")
                                    x=int(txt)
                                    if x>100:
                                        client.sendMessage(receiver,"Maksimal 100")
                                    else:
                                        x=x-1
                                        getTemplate=get_memes()
                                        templateUrl=getTemplate[x]['url']
                                        client.sendImageWithURL(receiver,templateUrl)
                                except Exception as e:
                                    client.sendMessage(receiver,str(e))
                            elif text.lower() in ['adib','.adib','.micin','cilukba','.cilukba']:
                                client.sendImage(receiver, 'adib.jpeg')
                            elif text.lower() == '.ci/luk/baa':
                                client.sendImage(receiver, 'adib_ci.jpeg')
                                client.sendImage(receiver, 'adib_luk.jpeg')
                                client.sendImage(receiver, 'adib_baa.jpeg')
                            elif text.lower() in ['.sabrut','.gustri','.sagne']:
                                client.sendImage(receiver, 'gustri_sabrut.jpeg')
                            elif 'say:' in msg.text.lower():
                                try:
                                    isi = msg.text.lower().replace('say:','')
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp.mp3')
                                    client.sendAudio(receiver, 'temp.mp3')
                                except Exception as e:
                                    client.sendMessage(receiver, str(e))
                            elif 'apakah ' in msg.text.lower():
                                try:
                                    txt = ['iya','tidak','bisa jadi']
                                    isi = random.choice(txt)
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp2.mp3')
                                    client.sendAudio(receiver, 'temp2.mp3')
                                except Exception as e:
                                    client.sendMessage(receiver, str(e))
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
                                    client.sendMessage(receiver, str(e))
                            elif "tr:" in msg.text:
                                try:
                                    isi = msg.text.split(":")
                                    translator = Translator()
                                    hasil = translator.translate(isi[2], dest=isi[1])
                                    A = hasil.text                               
                                    client.sendMessage(receiver, str(A))
                                except Exception as e:
                                    client.sendMessage(receiver, str(e))
                            elif text.lower() in ['.speed','.sp']:
                                start = time.time()
                                client.sendMessage(receiver, "TestSpeed")
                                elapsed_time = time.time() - start
                                client.sendMessage(receiver, "%sdetik" % (elapsed_time))
                            elif text.lower() == '.runtime':
                                client.sendMessage(receiver, "Counting")
                                elapsed_time = time.time() - startTime
                                m, s = divmod(elapsed_time, 60)
                                h, m = divmod(m, 60)
                                d, h = divmod(h, 24)
                                print(("d:h:m:s-> %d:%d:%d:%d" % (d, h, m, s)))
                                client.sendMessage(receiver, "d:h:m:s-> %d:%02d:%02d:%02d" % (d, h, m, s))
                            #Command dibawah hanya untuk didalam grup
                            elif msg.toType == 2:
                                if sender in owner:
                                    client.sendChatChecked(receiver, msg_id)
                                    contact = client.getContact(sender)
                                    if text.lower() in ['me','.me']:
                                        client.sendMessage(receiver, None, contentMetadata={'mid': sender}, contentType=13)
                                        client.tag(receiver, sender)
                                    elif '.gc ' in text.lower():
                                        try:
                                            key = eval(msg.contentMetadata["MENTION"])
                                            u = key["MENTIONEES"][0]["M"]
                                            cname = client.getContact(u).displayName
                                            cmid = client.getContact(u).mid
                                            cstatus = client.getContact(u).statusMessage
                                            cpic = client.getContact(u).picturePath
                                            #print(str(a))
                                            client.sendMessage(receiver, 'Nama : '+cname+'\nMID : '+cmid+'\nStatus Msg : '+cstatus+'\nPicture : http://dl.profile.line.naver.jp'+cpic)
                                            client.sendMessage(receiver, None, contentMetadata={'mid': cmid}, contentType=13)
                                            if "videoProfile='{" in str(client.getContact(u)):
                                                client.sendVideoWithURL(receiver, 'http://dl.profile.line.naver.jp'+cpic+'/vp.small')
                                            else:
                                                client.sendImageWithURL(receiver, 'http://dl.profile.line.naver.jp'+cpic)
                                        except Exception as e:
                                            client.sendMessage(receiver, str(e))
                                    elif '.sticker:' in msg.text.lower():
                                        try:
                                            query = msg.text.replace("sticker:", "")
                                            query = int(query)
                                            if type(query) == int:
                                                client.sendImageWithURL(receiver, 'https://stickershop.line-scdn.net/stickershop/v1/product/'+str(query)+'/ANDROID/main.png')
                                                client.sendMessage(receiver, 'https://line.me/S/sticker/'+str(query))
                                            else:
                                                client.sendMessage(receiver, 'gunakan key sticker angka bukan huruf')
                                        except Exception as e:
                                            client.sendMessage(receiver, str(e))
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
                                            client.sendMessage(receiver, str(e))
                                    elif 'scover' in text.lower():
                                        try:
                                            key = eval(msg.contentMetadata["MENTION"])
                                            u = key["MENTIONEES"][0]["M"]
                                            a = channel.getProfileCoverURL(mid=u)
                                            client.sendImageWithURL(receiver, a)
                                        except Exception as e:
                                            client.sendMessage(receiver, str(e))
                                    elif ".copy @" in msg.text:
                                        print("[COPY] OK")
                                        try:
                                            _name = msg.text.replace(".copy @","")
                                            _nametarget = _name.rstrip('  ')
                                            gs = cl.getGroup(msg.to)
                                            targets = []
                                            for g in gs.members:
                                                if _nametarget == g.displayName:
                                                    targets.append(g.mid)
                                            if targets == []:
                                                cl.sendText(msg.to, "Not Found...")
                                            else:
                                                for target in targets:
                                                    try:
                                                        cl.cloneContactProfile(target)
                                                        cl.sendText(receiver, "Succes Copy profile")
                                                    except Exception as e:
                                                        cl.sendMessage(receiver, str(e))
                                        except Exception as e:
                                            cl.sendMessage(receiver, str(e))
                                    elif msg.text in ".backup":
                                        print("[BACKUP] OK")
                                        try:
                                            cl.updateProfileAttribute(8, backup.pictureStatus)
                                            cl.updateProfile(backup)
                                            cl.sendText(msg.to, "backup done")
                                        except Exception as e:
                                            cl.sendText(msg.to, str (e))
                                    elif text.lower() in ['.tagall','.mentionall','.summon','.kimotih']:   
                                            tagall(client,receiver)
                                    elif text.lower() in ['.tagall2','.mentionall2','.summon2','.kimotih2']:   
                                            tagall2(client,receiver)
                                    elif text.lower() in ['.tagbig']:   
                                            tagbig(client,receiver)
                                    elif text.lower() in ['.tagadmin','.mentionadmin','.summonadmin','.itteh']:   
                                            tagadmin(client,receiver)
                                    elif text.lower() == ".setbotkuy":
                                        group = cl.getGroup(msg.to)
                                        nama = [contact.mid for contact in group.members]
                                        for md in nama:
                                            if md in boten:
                                              wait["joinedBoT"] = str(md)
                                              wait["groupId"] = str(group.id)
                                              fellyCfgUpdate()
                                              cl.sendMessage(msg.to, "Battle of Ten sudah di set")                                         
                                    elif text.lower() == ".unsetbotkuy":
                                            wait["joinedBoT"] = ""
                                            wait["groupId"] = ""
                                            fellyCfgUpdate()
                                            cl.sendMessage(msg.to, "Battle of Ten sudah di unset")
                                    elif msg.text in [".kuy",".nganu",".join kuy"]: #Panggil Semua Bot
                                        inv=inviteBot(KAC,receiver)
                                        print(inv)
                                        cl.sendMessage(receiver,inv)
                                    elif text.lower() == ".felly in": #Panggil Felly ke Group
                                        cl.inviteIntoGroup(receiver,[Amid])
                                        ki.acceptGroupInvitation(receiver)
                                    elif text.lower() == ".felly out":
                                        ginfo = cl.getGroup(receiver)
                                        try:
                                            ki.leaveGroup(receiver)
                                        except:
                                            pass
                                    elif text.lower() in [".cabut all",".kabur all",".kaboor all"]: #Bot Ninggalin Group termasuk Bot Induk
                                        ginfo = cl.getGroup(receiver)
                                        try:
                                            ki.leaveGroup(receiver)
                                            kk.leaveGroup(receiver)
                                            kc.leaveGroup(receiver)
                                            ks.leaveGroup(receiver)
                                        except:
                                            pass
                                    elif ".setbattle: " in text.lower():
                                        settxt=text.replace(".setbattle: ","")
                                        modetxt=settxt.split(" ")
                                        if modetxt[0] == "auto":
                                            wait["autoBattle"]=True
                                            wait["battleMode"]=modetxt[1]
                                            cl.sendMessage(wait['groupId'],"Auto Battle Mode : ON \nBattle Mode : "+wait['battleMode'])
                                        elif modetxt[0] == "off":
                                            wait["autoBattle"]=False
                                            wait["battleMode"]=""
                                            cl.sendMessage(wait['groupId'],"Auto Battle Mode : OFF \nBattle Mode : None")
                                    elif text == '.grAdd':
                                        print("[Command]GroupList Add executing")
                                        if receiver not in grouplist:
                                            grouplist.append(str(receiver))
                                            groupAdmin[str(receiver)]=[]
                                            cl.sendMessage(receiver,"Grup Ditambahkan ke list")
                                            fellyCfgUpdate()
                                        else:
                                            cl.sendMessage(receiver,"Grup sudah ada di list")
                                        print("[Command]GroupList Add executed")
                                    elif text == '.grRemove':
                                        print("[Command]GroupList Remove executing")
                                        if receiver in grouplist:
                                            grouplist.remove(receiver)
                                            groupAdmin.pop(str(receiver),None)
                                            if receiver in protectedGroup:
                                                protectedGroup.remove(receiver)
                                            cl.sendMessage(receiver,"Grup Dihapus dari list")
                                            fellyCfgUpdate()
                                        else:
                                            cl.sendMessage(receiver,"Grup tidak ada di dalam list")
                                        print("[Command]GroupList Remove executed")
                                    elif text == '.grList':
                                        print("[Command]grouplist executing")
                                        grlist=getGroupList(cl)
                                        cl.sendMessage(receiver,grlist)
                                        print("[Command]grouplist executed")
                                    elif "grAdmin add @" in text:
                                        print("[Command]Staff add executing")
                                        targets = getCalonAdmin(KAC,receiver,text)
                                        if targets == []:
                                            cl.sendMessage(receiver,"Contact not found")
                                        else:
                                            for target in targets:
                                                if receiver in grouplist:
                                                    if target not in admin:
                                                        if target not in groupAdmin[receiver]:
                                                            try:
                                                                groupAdmin[receiver].append(str(target))
                                                                cl.sendMessage(receiver,"Admin Grup Ditambahkan")
                                                                fellyCfgUpdate()
                                                            except:
                                                                pass
                                                        else:
                                                            cl.sendMessage(receiver,"Existing Group Admin")
                                                    else:
                                                        cl.sendMessage(receiver,"Targetnya Admin Wayang Dugem Boss")                                                                   
                                                else:
                                                    cl.sendMessage(receiver,"Grup ini belum masuk grouplist")
                                        print("[Command]Staff add executed")
                                    elif "grAdmin remove @" in text:
                                        print("[Command]Staff remove executing")
                                        targets = getCalonAdmin(KAC,receiver,text)
                                        if targets == []:
                                            cl.sendMessage(receiver,"Contact not found")
                                        else:
                                            for target in targets:
                                                if receiver in grouplist:
                                                    if target in groupAdmin[receiver]:
                                                        try:
                                                            groupAdmin[receiver].remove(target)
                                                            cl.sendMessage(receiver,"Admin Grup Dihapus")
                                                            fellyCfgUpdate()
                                                        except:
                                                            pass
                                                    else:
                                                        cl.sendMessage(receiver,"Target not Group Admin")
                                                else:
                                                    cl.sendMessage(receiver,"Grup ini belum masuk grouplist")
                                        print("[Command]Staff remove executed")
                                    elif text.lower() == '.adminlist':
                                        alist=getAdminList(cl,receiver)
                                        cl.sendMessage(receiver,alist)
                                        print("[Command]Adminlist executed")
                                    elif "Admin add @" in text:
                                        print("[Command]Staff add executing")
                                        targets = getCalonAdmin(KAC,receiver,text)
                                        if targets == []:
                                            cl.sendMessage(receiver,"Contact not found")
                                        else:
                                            for target in targets:
                                                if target not in admin:
                                                    try:
                                                        admin.append(str(target))
                                                        cl.sendMessage(receiver,"Admin Ditambahkan")
                                                        fellyCfgUpdate()
                                                    except:
                                                        pass
                                                else:
                                                    cl.sendMessage(receiver,"Existing Admin")
                                        print("[Command]Staff add executed")
                                    elif "Admin remove @" in text:
                                        print("[Command]Staff remove executing")
                                        targets = getCalonAdmin(KAC,receiver,text)
                                        if targets == []:
                                            cl.sendMessage(receiver,"Contact not found")
                                        else:
                                            for target in targets:
                                                if target in admin:
                                                    try:
                                                        admin.remove(target)
                                                        cl.sendMessage(receiver,"Admin Dihapus")
                                                        fellyCfgUpdate()
                                                    except:
                                                        pass
                                                else:
                                                    cl.sendMessage(receiver,"Target Not Admin")
                                        print("[Command]Staff remove executed")
                                    elif text.lower() == '.help':
                                        helpMenu = helpMessage
                                        helpMenu += helpAdmin+helpOwner
                                        helpMenu += helpFooter
                                        cl.sendMessage(receiver,helpMenu)
                                    elif text.lower() == '.updateconfig':
                                        fellyCfgUpdate()
                                        cl.sendMessage(receiver,"Config Updated Successfully")
                                    elif text.lower() in ['.ceksider','.cctv','.halosider']:
                                        txt = text.lower()
                                        try:
                                            del cctv['point'][receiver]
                                            del cctv['sidermem'][receiver]
                                            del cctv['cyduk'][receiver]
                                            del cctv['haloSider'][receiver]
                                        except:
                                            pass
                                        cctv['point'][receiver] = msg.id
                                        cctv['sidermem'][receiver] = "Kang CCTV Keciduk Nih"
                                        cctv['cyduk'][receiver]=True
                                        cctv['haloSider'][receiver]=False
                                        if txt=='.halosider':
                                            cctv['haloSider'][receiver]=True
                                    elif text.lower() in ['.offread','.ciduk']:
                                        if msg.to in cctv['point']:
                                            cctv['cyduk'][receiver]=False
                                            client.sendMessage(receiver, cctv['sidermem'][msg.to])
                                        else:
                                            client.sendMessage(receiver, "Heh belom di Set")
                                    elif text.lower() in ['.resetcctv','.resetsider']:
                                        try:
                                            del cctv['point'][receiver]
                                            del cctv['sidermem'][receiver]
                                            del cctv['cyduk'][receiver]
                                            del cctv['haloSider'][receiver]
                                        except:
                                            pass
                                        cl.sendMessage(receiver,"List CCTV grup ini sudah di reset")
                                    elif text.lower() == 'mode:self':
                                        wait["botmode"] = 'self'
                                        fellyCfgUpdate()
                                        client.sendMessage(receiver, 'Mode Public Off')
                                    elif text.lower() == 'mode:public':
                                        cek=isBotJoined(cl,Bots,receiver)
                                        resmsg=""
                                        if cek == []:
                                            resmsg='Puclic Mode Activation Failed\nError : Missing Felly'
                                        else:
                                            try:
                                                for ceks in cek:
                                                    if ceks == Amid:
                                                        wait["botmode"] = 'public'
                                                        fellyCfgUpdate()
                                                        resmsg='Mode Public ON'
                                                    else:
                                                        resmsg='Puclic Mode Activation Failed\nError : Missing Felly'
                                            except Exception as e:
                                                resmsg=str(e)
                                        client.sendMessage(receiver, resmsg)
                                    elif ".setprotect:" in text.lower():
                                        try:
                                            prot=text.replace(".setprotect:","")
                                            if prot.lower()=='on':
                                                if receiver in grouplist:
                                                    if receiver not in protectedGroup:
                                                        protectedGroup.append(str(receiver))
                                                        fellyCfgUpdate()
                                                        cl.sendMessage(receiver,"Done : Protection ON")
                                                    else:
                                                        cl.sendMessage(receiver,"This Group has been protected")
                                                else:
                                                    cl.sendMessage(receiver,"Grup nya masukin list dlu dong om")
                                            elif prot.lower()=='off':
                                                if receiver in grouplist:
                                                    if receiver in protectedGroup:
                                                        protectedGroup.remove(receiver)
                                                        fellyCfgUpdate()
                                                        cl.sendMessage(receiver,"Done : Protection OFF")
                                                    else:
                                                        cl.sendMessage(receiver,"This Group not protected")
                                                else:
                                                    cl.sendMessage(receiver,"Group ini ga ada di list om")
                                            else:
                                                cl.sendMessage(receiver,"Invalid Parameter")
                                        except Exception as e:
                                            cl.sendMessage(receiver,str(e))
                                    elif text.lower() == ".cekprotect":
                                        try:
                                            if receiver in grouplist:
                                                if receiver in protectedGroup:
                                                    cl.sendMessage(receiver,"Protection On")
                                                else:
                                                    cl.sendMessage(receiver,"Protection Off")
                                            else:
                                                cl.sendMessage(receiver,"This Group Not In Group List")
                                        except Exception as e:
                                            cl.sendMessage(receiver,str(e)) 
                                    elif ".autoadd:" in text.lower():
                                        try:
                                            prot=text.replace(".autoadd:","")
                                            if prot.lower()=="on":
                                                if wait["autoAdd"] == True:
                                                    cl.sendMessage(receiver,"Auto Add Already ON")
                                                elif wait["autoAdd"] == False:
                                                    wait["autoAdd"] = True
                                                    fellyCfgUpdate()
                                                    cl.sendMessage(receiver,"Done : Auto Add ON")
                                            elif prot.lower()=="off":
                                                if wait["autoAdd"] == True:
                                                    wait["autoAdd"] = False
                                                    fellyCfgUpdate()
                                                    cl.sendMessage(receiver,"Done : Auto Add OFF")
                                                elif wait["autoAdd"] == False:
                                                    cl.sendMessage(receiver,"Auto Add Already OFF")
                                            else:
                                                cl.sendMessage(receiver,"Invalid Parameter")
                                        except Exception as e:
                                            cl.sendMessage(receiver,str(e))
                                    elif ".autojoingroup:" in text.lower():
                                        try:
                                            prot=text.replace(".autojoingroup:","")
                                            if prot.lower()=="on":
                                                if wait["autoJoin"] == True:
                                                    cl.sendMessage(receiver,"Auto Accept Group Invitation Already ON")
                                                elif wait["autoJoin"] == False:
                                                    wait["autoJoin"] = True
                                                    fellyCfgUpdate()
                                                    cl.sendMessage(receiver,"Done : Auto Accept Group Invitation ON")
                                            elif prot.lower()=="off":
                                                if wait["autoJoin"] == True:
                                                    wait["autoJoin"] = False
                                                    fellyCfgUpdate()
                                                    cl.sendMessage(receiver,"Done : Auto Accept Group Invitation OFF")
                                                elif wait["autoJoin"] == False:
                                                    cl.sendMessage(receiver,"Auto Accept Group Invitation Already OFF")
                                            else:
                                                cl.sendMessage(receiver,"Invalid Parameter")
                                        except Exception as e:
                                            cl.sendMessage(receiver,str(e))
                                    elif ".bigaj:" in text.lower():
                                        try:
                                            txt=text.replace(".bigaj:","")
                                            gas=txt.split("|")
                                            mode=gas[0]
                                            resmsg=''
                                            if mode.lower()=="on":
                                                if wait["bigAj"] == {}:
                                                    for x in range(1,len(gas)):
                                                        y=int(gas[x])-1
                                                        wait["bigAj"][y]=True
                                                    resmsg="Done ON"
                                                else:
                                                    try:
                                                        a=0
                                                        for x in range(1,len(gas)):
                                                            y=int(gas[x])-1
                                                            if y not in wait["bigAj"]:
                                                                wait["bigAj"][y] = True
                                                                a=a+1
                                                            else:
                                                                pass
                                                        if a == 0:
                                                            resmsg="Already ON"
                                                        else:
                                                            resmsg="Done ON"
                                                    except Exception as e:
                                                        print("trying on "+str(e))
                                                        resmsg=str(e)
                                            elif mode.lower()=="off":
                                                if wait["bigAj"] == {}:
                                                    resmsg="Already OFF"
                                                else:
                                                    if len(gas)==1:
                                                        z=[]
                                                        for mi in wait["bigAj"]:
                                                            z.append(mi)
                                                        for o in z:
                                                            wait["bigAj"].pop(o,None)
                                                        resmsg="Done OFF"
                                                    else:
                                                        try:
                                                            a=0
                                                            for x in range(1,len(gas)):
                                                                y=int(gas[x])-1
                                                                if wait["bigAj"][y] == True:
                                                                    wait["bigAj"].pop(y,None)
                                                                    a=a+1
                                                                else:
                                                                    pass
                                                            if a == 0:
                                                                resmsg="Already OFF"
                                                            else:
                                                                resmsg="Done OFF"
                                                        except Exception as e:
                                                            print("trying off "+str(e))
                                                            resmsg=str(e)
                                            elif mode.lower()=="cek":
                                                if wait["bigAj"] == {}:
                                                    resmsg="OFF"
                                                else:
                                                    try:
                                                        resmsg="ON"
                                                        for o in wait["bigAj"]:
                                                            resmsg+="\n"+str(o+1)+"--> "+str(KAC[o].getProfile().displayName)
                                                    except Exception as e:
                                                        resmsg=str(e)
                                            else:
                                                resmsg="Invalid Parameter"
                                            fellyCfgUpdate()
                                            cl.sendMessage(receiver,resmsg)
                                        except Exception as e:
                                            cl.sendMessage(receiver,str(e))
                                    elif ".ajbattle:" in text.lower():
                                        txt=text.replace(".ajbattle:","")
                                        gas=txt.split("|")
                                        mode=gas[0]
                                        resmsg=''
                                        try:
                                            if mode == 'on':
                                                if autoJoinBattle["on"] == False:
                                                    autoJoinBattle["on"] = True
                                                    autoJoinBattle["groupId"] = gas[1]
                                                    fellyCfgUpdate()
                                                    resmsg="Done ON"
                                                else:
                                                    resmsg="Already ON"
                                            elif mode == 'off':
                                                if autoJoinBattle["on"] == False:
                                                    resmsg="Already OFF"
                                                else:
                                                    autoJoinBattle["on"] = False
                                                    autoJoinBattle["groupId"] = ''
                                                    fellyCfgUpdate()
                                                    resmsg="Done OFF"
                                            elif mode == 'cek':
                                                if autoJoinBattle["on"] == False:
                                                    resmsg="Mode OFF"
                                                else:
                                                    g=cl.getGroup(autoJoinBattle["groupId"])
                                                    mc="Mode ON :\n"
                                                    mc+="••>" + g.name + "\n" + "[•]Group Id : " + g.id + "\n" + "[•]Group Creator : " + g.creator.displayName + "\n"
                                                    resmsg=mc
                                        except Exception as e:
                                            resmsg=str(e)
                                        cl.sendMessage(receiver,resmsg)
                                    elif ".botenname:" in text.lower():
                                        txt=text.replace(".botenname:","")
                                        gas=txt.split("/")
                                        mode=gas[0]
                                        midnum=gas[1]
                                        name=gas[2]
                                        resmsg=''
                                        try:
                                            if mode=="set":
                                                if Bots[midnum] not in customVar:
                                                    customVar[Bots[midnum]]={}
                                                customVar[Bots[midnum]]["botenName"]=gas[2]
                                                if "botenNameList" not in customVar:
                                                    customVar["botenNameList"]=[]
                                                else:
                                                    customVar["botenNameList"].append(gas[2])
                                                resmsg="Battle of Ten Name sudah di set\nName : "+gas[2]
                                            elif mode=="update":
                                                newname=gas[3]
                                                customVar["botenNameList"].remove(name)
                                                customVar["botenNameList"].append(newname)
                                                resmsg="Battle of Ten Name sudah di Update\nOld Name : "+gas[2]+"\nNew Name : "+gas[3]
                                            fellyCfgUpdate()
                                            cl.sendMessage(receiver,resmsg)
                                        except Exception as e:
                                            print("[Battle of Ten Name]["+time.strftime("%Y-%m-%d %H:%M:%S")+"] : "+str(e))
                                            resmsg="[Battle of Ten Name]["+time.strftime("%Y-%m-%d %H:%M:%S")+"] : "+str(e)
                                            cl.sendMessage(receiver,resmsg)
                                    elif ".autotrain:" in text.lower():
                                        txt=text.replace(".autotrain:","")
                                        gas=txt.split("/")
                                        mode=gas[0]
                                        midnum=gas[1]
                                        trainmode=0
                                        if len(gas) > 2:
                                            trainmode=gas[2]
                                        resmsg=''
                                        if Bots[midnum] in customVar:
                                            try:
                                                if mode=="on":
                                                    customVar[Bots[midnum]]["autoTrain"]["active"]=True
                                                    customVar[Bots[midnum]]["autoTrain"]["trainmode"]=trainmode
                                                    resmsg="Auto Train On"
                                                elif mode=="off":
                                                    customVar[Bots[midnum]]["autoTrain"]["active"]=False
                                                    resmsg="Auto Train Off"
                                                fellyCfgUpdate()
                                                cl.sendMessage(receiver,resmsg)
                                            except Exception as e:
                                                print("[Auto Train]["+time.strftime("%Y-%m-%d %H:%M:%S")+"] : "+str(e))
                                                resmsg="[Auto Train]["+time.strftime("%Y-%m-%d %H:%M:%S")+"] : "+str(e)
                                                cl.sendMessage(receiver,resmsg)
                                        else:
                                            cl.sendMessage(receiver,"Battle of Ten Name belum di set")
                                    elif ".autocast:" in text.lower():
                                        txt=text.replace(".autocast:","")
                                        gas=txt.split("/")
                                        mode=gas[0]
                                        midnum=gas[1]
                                        resmsg=''
                                        if Bots[midnum] in customVar:
                                            try:
                                                if mode=="on":
                                                    customVar[Bots[midnum]]["autoBattle"]["cast"]=True
                                                    resmsg="Auto Cast On"
                                                elif mode=="off":
                                                    customVar[Bots[midnum]]["autoBattle"]["cast"]=False
                                                    resmsg="Auto Cast Off"
                                                fellyCfgUpdate()
                                                cl.sendMessage(receiver,resmsg)
                                            except Exception as e:
                                                print("[Auto Cast]["+time.strftime("%Y-%m-%d %H:%M:%S")+"] : "+str(e))
                                                resmsg="[Auto Cast]["+time.strftime("%Y-%m-%d %H:%M:%S")+"] : "+str(e)
                                                cl.sendMessage(receiver,resmsg)
                                        else:
                                            cl.sendMessage(receiver,"Battle of Ten Name belum di set")
                                    elif ".autodef:" in text.lower():
                                        txt=text.replace(".autodef:","")
                                        gas=txt.split("/")
                                        mode=gas[0]
                                        midnum=gas[1]
                                        resmsg=''
                                        if Bots[midnum] in customVar:
                                            try:
                                                if mode=="on":
                                                    customVar[Bots[midnum]]["autoBattle"]["defend"]=True
                                                    resmsg="Auto Defend On"
                                                elif mode=="off":
                                                    customVar[Bots[midnum]]["autoBattle"]["defend"]=False
                                                    resmsg="Auto Defend Off"
                                                fellyCfgUpdate()
                                                cl.sendMessage(receiver,resmsg)
                                            except Exception as e:
                                                print("[Auto Defend]["+time.strftime("%Y-%m-%d %H:%M:%S")+"] : "+str(e))
                                                resmsg="[Auto Defend]["+time.strftime("%Y-%m-%d %H:%M:%S")+"] : "+str(e)
                                        else:
                                            cl.sendMessage(receiver,"Battle of Ten Name belum di set")
                                    elif ".autofind:" in text.lower():
                                        resmsg=''
                                        txt=text.replace(".autofind:","")
                                        data=txt.split("/")
                                        cl.log(data)
                                        mode=data[0]
                                        midnum=int(data[1])-1
                                        if mode == "on":
                                            herotype=data[2]
                                            heroname=data[3]
                                            server=data[4]
                                            slot=data[5]
                                            if autoFind == {}:
                                                resmsg=setAutoFind(Bots[midnum],data)
                                                cl.sendMessage(autoFind[receiver]["server"],"/"+autoFind[receiver]["herotype"])
                                            elif Bots[midnum] not in autoFind:
                                                resmsg=setAutoFind(Bots[midnum],data)
                                                cl.sendMessage(autoFind[receiver]["server"],"/"+autoFind[receiver]["herotype"])
                                            else:
                                                resmsg="Already ON"
                                        elif mode == "off":
                                            if autoFind == {}:
                                                resmsg="Already OFF"
                                            else:
                                                resmsg=unsetAutoFind(Bots[midnum])
                                        elif mode == "cek":
                                            resmsg=cekAutoFind(Bots[midnum])
                                        else:
                                            resmsg="Invalid Parameter"
                                        fellyCfgUpdate()
                                        cl.sendMessage(receiver,resmsg)
                                    elif ".autohstore:" in text.lower():
                                        resmsg=''
                                        txt=text.replace(".autohstore:","")
                                        data=txt.split("/")
                                        cl.log(data)
                                        mode=data[0]
                                        midnum=int(data[1])-1
                                        if mode == "on":
                                            herotype=data[2]
                                            heroname=data[3]
                                            server=data[4]
                                            if autoHStore == {}:
                                                resmsg=setAutoHStore(Bots[midnum],data)
                                            elif Bots[midnum] not in autoHStore:
                                                resmsg=setAutoHStore(Bots[midnum],data)
                                            else:
                                                resmsg="Already ON"
                                        elif mode == "off":
                                            if autoHStore == {}:
                                                resmsg="Already OFF"
                                            else:
                                                resmsg=unsetAutoHStore(Bots[midnum])
                                        elif mode == "cek":
                                            resmsg=cekAutoHStore(Bots[midnum])
                                        elif mode == "start":
                                            try_start=startStopAutoHStore(Bots[midnum],mode)
                                            if try_start['result'] == True:
                                                cl.sendMessage(autoHStore[Bots[midnum]]["server"],"/hstore")
                                                resmsg=try_start['resmsg']
                                            else:
                                                resmsg=try_start['resmsg']
                                        elif mode == "stop":
                                            try_stop=startStopAutoHStore(Bots[midnum],mode)
                                            resmsg=try_stop['resmsg']
                                        else:
                                            resmsg="Invalid Parameter"
                                        fellyCfgUpdate()
                                        cl.sendMessage(receiver,resmsg)
                                    elif ".refresh_battle" in text.lower():
                                        try:
                                            txt="/refresh"
                                            for n in boten:
                                                cl.sendMessage(n,(txt))
                                                ki.sendMessage(n,(txt))
                                                kc.sendMessage(n,(txt))
                                                kk.sendMessage(n,(txt))
                                                ks.sendMessage(n,(txt))
                                                sleep(3)
                                        except Exception as e:
                                            cl.sendMessage(receiver,str(e))
                                    elif ".cekmember @" in text.lower():
                                        _name = text.replace(".cekmember @","")
                                        _nametarget = _name.rstrip('  ')
                                        gs = cl.getGroup(receiver)
                                        targets = ''
                                        for g in gs.members:
                                            if _nametarget == g.displayName:
                                                targets=g.mid
                                        if targets == '':
                                            result="Tidak Ditemukan....."
                                        else:
                                            if targets not in owner or admin or groupAdmin[receiver]:
                                                cl.sendMessage(receiver,"Target adalah Member")
                                            else:
                                                cl.sendMessage(receiver,"Target adalah Admin")
                                    elif text.lower() in [".oqr",".openqr",".bukaqr",".ourl"]:
                                        oqr=openQr(cl,receiver)
                                        cl.sendMessage(receiver,oqr)
                                    elif text.lower() in [".cqr",".closeqr",".curl",".tutupqr"]:
                                        cqr=closeQr(cl,receiver)
                                        cl.sendMessage(receiver,cqr)
                                    elif text.lower() in [".gurl",".groupurl"]:
                                        gu=gurl(cl,receiver)
                                        cl.sendMessage(receiver,gu)
                                    elif "nk " in text.lower():
                                        nk=nameKick(cl,msg)
                                        cl.sendMessage(receiver,nk)
                                else:
                                    client.sendMessage(receiver,"Owner Only Kakak")
                    except Exception as e:
                        client.log("[SEND MESSAGE] ERROR : " + str(e))
                elif op.type == 26:
                    msg = op.message
                    text = msg.text
                    msg_id = msg.id
                    receiver = msg.to
                    sender = msg._from
                    try:
                        if sender in boten:
                            # print msg
                            # print "\n"
                            # group=cl.getGroup(msg.to)
                            
                            #######################################################################################################################
                            if msg.toType == 0:
                                if msg.contentType == 0:
                                    if "nobot" in text:
                                        antibotindex=text.lower().find("kode kamu")
                                        if antibotindex == -1:
                                            if "SATPOLL PP" in text:
                                                nobot=text.find("/nobot")
                                                temp=text[nobot:]
                                                spl=temp.split(" ")
                                                txt=spl[0]+' '+spl[1]
                                                cl.sendMessage(sender,(txt))
                                            else:
                                                isitext="ada nobot versi ghaib boss"
                                                try:
                                                    ki.mentionWithText('cfed1f18026bdf0ccd335839f25285533',mid,str(isitext))
                                                except:
                                                    try:
                                                        cl.mentionWithText('cfed1f18026bdf0ccd335839f25285533',mid,str(isitext))
                                                    except Exception as e:
                                                        print("[nobot]["+time.strftime("%Y-%m-%d %H:%M:%S")+"] : "+str(e))
                                        else:
                                            temp=text[antibotindex:]
                                            spl=temp.split(" ")
                                            txt="/nobot "
                                            if spl[2].lower() == 'bukan':
                                                txt+=spl[5]
                                            else:
                                                txt+=spl[3]
                                            cl.sendMessage(sender,(txt))
                                            
                            if autoFind != {}:
                                if msg.toType == 0:
                                    if msg.contentType == 0:
                                        print(text)
                                        if "Setelah lama mencari akhirnya " in text:
                                            heroname=autoFind[receiver]["heroname"]
                                            mesindex=text.find(heroname.capitalize())
                                            if mesindex == -1:
                                                slot=int(autoFind[receiver]["slot"])+1
                                                time.sleep(randint(1,10))
                                                cl.sendMessage(sender,"/removeok "+str(slot))
                                                time.sleep(randint(1,10))
                                                cl.sendMessage(autoFind[receiver]["server"],"/"+autoFind[receiver]["herotype"])
                                            else:
                                                slot=int(autoFind[receiver]["slot"])+1
                                                autoFind[receiver]["slot"]=slot
                                                fellyCfgUpdate()
                                                if slot < 3:
                                                    time.sleep(randint(1,10))
                                                    cl.sendMessage(autoFind[receiver]["server"],"/"+autoFind[receiver]["herotype"])
                                                else:
                                                    pass
                                        elif autoFind[receiver]["heroname"].capitalize()+" berhasil Power UP!!!" in text:
                                            slot=int(autoFind[receiver]["slot"])-1
                                            autoFind[receiver]["slot"]=slot
                                            fellyCfgUpdate()
                                            if slot == 1:
                                                time.sleep(randint(1,10))
                                                cl.sendMessage(autoFind[receiver]["server"],"/"+autoFind[receiver]["herotype"])
                                        elif autoHStore != {}:
                                            if "Kamu membeli Hero "+autoFind[receiver]["heroname"].capitalize() in text:
                                                slot=int(autoFind[receiver]["slot"])+1
                                                autoFind[receiver]["slot"]=slot
                                                fellyCfgUpdate()
                                        else:
                                            pass
                                else:
                                    pass

                            if autoHStore != {}:
                                if msg.toType == 0:
                                    if msg.contentType == 4:
                                        mes=str(msg.contentMetadata)
                                        mes=mes.replace("{","")
                                        mes=mes.replace("}","")
                                        testsplit=mes.split('\"')
                                        postbacklist=[]
                                        for x in range(0,len(testsplit)):
                                            if "linepostback" in testsplit[x]:
                                                postbacklist.append(testsplit[x])

                                        if postbacklist!=[]:
                                            heroname=autoHStore[receiver]['heroname'].capitalize()
                                            price=autoHStore[receiver]['price']
                                            for y in range(0,len(postbacklist)):
                                                if heroname in postbacklist[y]:
                                                    oindex=postbacklist[y].find('harga')
                                                    o=postbacklist[y][oindex:]
                                                    o=o.split("%3D")
                                                    o=o[1]
                                                    o=o.split("%26")
                                                    o=o[0]
                                                    print(o)
                                                    if price=='0':    
                                                        isitext='Hero Found\nHero Name : '+heroname+'\nHero Price : '+o
                                                        try:
                                                            ki.mentionWithText('cfed1f18026bdf0ccd335839f25285533',owner,str(isitext))
                                                        except:
                                                            try:
                                                                cl.mentionWithText('cfed1f18026bdf0ccd335839f25285533',owner,str(isitext))
                                                            except Exception as e:
                                                                cl.sendMessage('cfed1f18026bdf0ccd335839f25285533',str(e))
                                                    elif price == o:
                                                        isitext='Hero Found\nHero Name : '+heroname+'\nHero Price : '+price
                                                        try:
                                                            ki.mentionWithText('cfed1f18026bdf0ccd335839f25285533',owner,str(isitext))
                                                        except:
                                                            try:
                                                                cl.mentionWithText('cfed1f18026bdf0ccd335839f25285533',owner,str(isitext))
                                                            except Exception as e:
                                                                cl.sendMessage('cfed1f18026bdf0ccd335839f25285533',str(e))
                                                    else:
                                                        pass
                                                else:
                                                    pass

                            #elif autoPowerUp != {}:
                            ###########################################################################################################################
                            if receiver == wait["groupId"]:
                                if msg.contentType == 4:
                                    print("Joined BoT : "+wait["joinedBoT"]+"\n")
                                    print("Group ID : "+wait["groupId"]+"\n")
                                    print("msg from boten ok")
                                    print(json.dumps(msg.contentMetadata))
                                    print("\n")
                                    mes=str(msg.contentMetadata)
                                    print("\nnonton wayang str mes : "+mes+"\n")
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
                                        print(txt)
                                        print("\n\n")
                                        customVar["roomNumber"]=arr_temp[1]
                                        time.sleep(randint(1,10))
                                        ki.sendMessage(wait["joinedBoT"],(txt))
                                        kc.sendMessage(wait["joinedBoT"],(txt))
                                        kk.sendMessage(wait["joinedBoT"],(txt))
                                        ks.sendMessage(wait["joinedBoT"],(txt))
                                        if wait['autoBattle']==False:
                                            cl.sendMessage(wait["joinedBoT"],(txt))
                                elif msg.contentType == 0:
                                    if msg.toType == 2:
                                        if "Semua musuh sudah mati.\nTim " in msg.text:
                                            if wait["autoBattle"] == True:
                                                print(msg.text)
                                                print("\nBoten Read\n")
                                                cl.sendMessage(msg.to, "bentar ya, auto reset 5 detik lg... itteh itteh kimotih")
                                                time.sleep(5)
                                                cl.sendMessage(msg.to, "/resetbot")
                                                time.sleep(2)
                                                cl.sendMessage(msg.to, ".tagall")
                                            else:
                                                pass
                            elif wait["bigAj"] != {}:
                                if msg.toType == 0:
                                    # print("[BIG AJ]["+time.strftime("%Y-%m-%d %H:%M:%S")+"] : MESSAGE Start\n")
                                    # print(msg)
                                    # print("[BIG AJ]["+time.strftime("%Y-%m-%d %H:%M:%S")+"] : MESSAGE End\n")
                                    if msg.contentType == 0:
                                        if "isJoin" in wait["bigAj"]:
                                            print("[BIG AJ]["+time.strftime("%Y-%m-%d %H:%M:%S")+"] : Try to Check Participants\n")
                                            if wait["bigAj"]["isJoin"]==False:
                                                print("[BIG AJ]["+time.strftime("%Y-%m-%d %H:%M:%S")+"] : Text = "+text+"\n")
                                                if "/judge" in text:
                                                    print("[BIG AJ]["+time.strftime("%Y-%m-%d %H:%M:%S")+"] : Check Total Participants\n")
                                                    mesindex=text.find("Contoh")
                                                    if mesindex == -1:
                                                        pass
                                                    else:
                                                        temp=text[mesindex:]
                                                        temp_arr=temp.split("\n")
                                                        arr_temp=temp_arr[1].split(" ")
                                                        jml=int(arr_temp[2])
                                                        print("[BIG AJ]["+time.strftime("%Y-%m-%d %H:%M:%S")+"] : Total Participants "+str(arr_temp[2])+"\n")
                                                        if jml >= 39:
                                                            target=wait["bigAj"]["boten"]
                                                            txt='/join '+wait["bigAj"]["roomNumber"]
                                                            customVar["roomNumber"]=wait["bigAj"]["roomNumber"]
                                                            wait["bigAj"].pop("isJoin",None)
                                                            wait["bigAj"].pop("checkCount",None)
                                                            wait["bigAj"].pop("boten",None)
                                                            wait["bigAj"].pop("roomNumber",None)
                                                            wait["bigAj"].pop("waitReply",None)
                                                            # fellyCfgUpdate()
                                                            for n in wait["bigAj"]:
                                                                KAC[n].sendMessage(target,(txt))
                                                                print("[BIG AJ]["+time.strftime("%Y-%m-%d %H:%M:%S")+"] : Send Join Command "+txt+"\n")
                                                        else:
                                                            if wait["bigAj"]["checkCount"]==2:
                                                                wait["bigAj"].pop("isJoin",None)
                                                                wait["bigAj"].pop("checkCount",None)
                                                                wait["bigAj"].pop("boten",None)
                                                                wait["bigAj"].pop("roomNumber",None)
                                                                wait["bigAj"].pop("waitReply",None)
                                                                # fellyCfgUpdate()
                                                            else:
                                                                pass
                                                else:
                                                    pass
                                            else:
                                                pass
                                        else:
                                            pass
                                elif receiver == bigGroupId:
                                    if msg.contentType == 4:
                                        # print(json.dumps(msg.contentMetadata))
                                        print("[BIG AJ]["+time.strftime("%Y-%m-%d %H:%M:%S")+"]: Initialize\n")
                                        mes=str(msg.contentMetadata)
                                        # print("\nbigaj str mes : "+mes+"\n")
                                        mes=mes.replace("{","")
                                        mes=mes.replace("}","")
                                        # txt=mes.split(":")
                                        mesindex=mes.find("ALT_TEXT")
                                        if mesindex == -1:
                                            pass
                                        else:
                                            if "isJoin" in wait["bigAj"]:
                                                temp=mes[mesindex:]
                                                arr_temp=temp.split(" ")
                                                if arr_temp[2]=='Room':
                                                    mesindex=mes.find('/join')
                                                    if mesindex == -1:
                                                        pass
                                                    else:
                                                        temp_txt=mes[mesindex:]
                                                        arr_temp=temp_txt.split(" ")
                                                        # txt=arr_temp[0]+" "+arr_temp[1]
                                                        txt="/cek "+arr_temp[1]
                                                        print("[BIG AJ]["+time.strftime("%Y-%m-%d %H:%M:%S")+"]: Get Room => "+arr_temp[1]+"\n")
                                                        # print(txt)
                                                        # print("\n\n")
                                                        # time.sleep(10)
                                                        wait["bigAj"]["isJoin"]=False
                                                        wait["bigAj"]["checkCount"]=1
                                                        wait["bigAj"]["boten"]=str(sender)
                                                        wait["bigAj"]["roomNumber"]=arr_temp[1]
                                                        wait["bigAj"]["waitReply"]=time.time()
                                                        # fellyCfgUpdate()
                                                        # time.sleep(10)
                                                        # for n in wait["bigAj"]:
                                                        #     KAC[n].sendMessage(sender,(txt))
                                                        # cl.sendMessage(sender,(txt))
                                                        # print("[BIG AJ]["+time.strftime("%Y-%m-%d %H:%M:%S")+"]: Checking\n")
                                                        # print("[BIG AJ]["+time.strftime("%Y-%m-%d %H:%M:%S")+"]: Sleep\n")
                                                        # time.sleep(randint(15))
                                                        # print("[BIG AJ]["+time.strftime("%Y-%m-%d %H:%M:%S")+"]: Sleep Finish\n")
                                                else:
                                                    pass
                                            else:
                                                pass
                                    elif msg.contentType == 0:
                                        if "Pertempuran akan dimulai dalam 50 detik" in text:
                                            if "isJoin" in wait["bigAj"]:
                                                txt="/cek "+wait["bigAj"]["roomNumber"]
                                                cl.sendMessage(sender,(txt))
                                                print("[BIG AJ]["+time.strftime("%Y-%m-%d %H:%M:%S")+"]: Checking\n")
                                            else:
                                                pass
                                        else:
                                            pass
                                    else:
                                        pass
                                else:
                                    pass
                            elif autoJoinBattle["on"] == True:
                                if receiver == autoJoinBattle["groupId"]:
                                    if msg.contentType == 4:
                                        print(json.dumps(msg.contentMetadata))
                                        mes=str(msg.contentMetadata)
                                        print("\nbigaj str mes : "+mes+"\n")
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
                                            print(txt)
                                            print("\n\n")
                                            time.sleep(randint(1,10))
                                            cl.sendMessage(sender,(txt))
                                    else:
                                        pass
                                else:
                                    pass
                            else:
                                pass
                        else:
                            if msg.toType == 4:
                                print(msg)
                            elif receiver == 'c39de70718b11214f8234ba8db7c4c31b':
                                if msg.contentType == 0:
                                    print(msg.contentMetadata)
                                    if "MENTION" in msg.contentMetadata:
                                        print(msg)
                                        key = eval(msg.contentMetadata["MENTION"])
                                        jml = len(key["MENTIONEES"])
                                        print(jml)
                                    else:
                                        pass
                            elif wait["bigAj"] != {}:
                                if receiver == bigGroupId:
                                    if msg.contentType == 0:
                                        if "MENTION" in msg.contentMetadata:
                                            print(msg)
                                            key = eval(msg.contentMetadata["MENTION"])
                                            jml = len(key["MENTIONEES"])
                                            print(jml)
                                            if jml >= 90:
                                                wait["bigAj"]["isJoin"]=False
                                                # fellyCfgUpdate()
                                            else:
                                                pass
                                        else:
                                            pass
                            elif wait["botmode"] == "public":
                                if receiver in grouplist:
                                    if msg.contentType == 0:
                                        if msg.toType == 2:
                                            # if receiver in grouplist
                                            if text.lower() == '.adminlist':
                                                alist=getAdminList(ki,receiver)
                                                ki.sendMessage(receiver,alist)
                                                print("[Command]Adminlist executed")
                                            elif text.lower() in ['.tagadmin','.mentionadmin','.summonadmin','.itteh']:   
                                                tagadmin(ki,receiver)
                                            elif text.lower() == '.help':
                                                helpMenu=helpMessage
                                                if sender in owner:
                                                    helpMenu += helpAdmin+helpOwner
                                                elif sender in admin:
                                                    helpMenu += helpAdmin
                                                helpMenu+=helpFooter
                                                ki.sendMessage(receiver,helpMenu)
                                            elif text.lower() in ['adib','.adib','.micin','cilukba','.cilukba']:
                                                ki.sendImage(receiver, 'adib.jpeg')
                                            elif text.lower() == '.ci/luk/baa':
                                                ki.sendImage(receiver, 'adib_ci.jpeg')
                                                ki.sendImage(receiver, 'adib_luk.jpeg')
                                                ki.sendImage(receiver, 'adib_baa.jpeg')
                                            elif text.lower() in ['.sabrut','.gustri','.sagne']:
                                                ki.sendImage(receiver, 'gustri_sabrut.jpeg')
                                            else:
                                                if sender in admin or groupAdmin[receiver]:
                                                    if text.lower() in ['.tagall','.mentionall','.summon']:
                                                        print("\nProcessing Tagall\n")
                                                        tagall(ki,receiver)
                                                else:
                                                    pass
                                        else:
                                            pass
                                    else:
                                        pass
                                else:
                                    pass
                            else:
                                pass
                    except Exception as e:
                        client.log("[READ MESSAGE] ERROR : " + str(e))
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
                                    if cctv['haloSider'][op.param1] == True:
                                        client.sendMessage(op.param1, str(random.choice(pref))+' '+Name)
                                    else:
                                        pass
                            else:
                                pass
                        else:
                            pass
                    except:
                        pass
                elif op.type == 19: #bot Ke Kick
                    if op.param1 in protectedGroup:
                        if op.param2 in Bots:
                            pass 
                        elif op.param2 in admin:
                            pass
                        elif op.param2 in groupAdmin[op.param1]:
                            pass
                        else:
                            if op.param3 in Bots:
                                try:
                                    print("ki Take Action")
                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                    ki.inviteIntoGroup(op.param1,[mid])
                                    cl.acceptGroupInvitation(op.param1)
                                    banUserByMid(op.param2)
                                except:
                                    print("cl Exception Take Action")
                                    cl.kickoutFromGroup(op.param1,[op.param2])
                                    cl.inviteIntoGroup(op.param1,[Amid])
                                    ki.acceptGroupInvitation(op.param1)
                                    banUserByMid(op.param2)
                            elif op.param3 in admin:
                                try:
                                    print("ki Take Action")
                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                    ki.findAndAddContactsByMid(op.param3)
                                    ki.inviteIntoGroup(op.param1,[op.param3])
                                    banUserByMid(op.param2)
                                except:
                                    print("cl Exception Take Action")
                                    cl.kickoutFromGroup(op.param1,[op.param2])
                                    cl.inviteIntoGroup(op.param1,[Amid])
                                    ki.acceptGroupInvitation(op.param1)
                                    ki.findAndAddContactsByMid(op.param3)
                                    ki.inviteIntoGroup(op.param1,[op.param3])
                                    banUserByMid(op.param2)
                            elif op.param3 in groupAdmin[op.param1]:
                                try:
                                    print("ki Take Action")
                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                    ki.findAndAddContactsByMid(op.param3)
                                    ki.inviteIntoGroup(op.param1,[op.param3])
                                    banUserByMid(op.param2)
                                except:
                                    print("cl Exception Take Action")
                                    cl.kickoutFromGroup(op.param1,[op.param2])
                                    cl.inviteIntoGroup(op.param1,[Amid])
                                    ki.acceptGroupInvitation(op.param1)
                                    ki.findAndAddContactsByMid(op.param3)
                                    ki.inviteIntoGroup(op.param1,[op.param3])
                                    banUserByMid(op.param2)
                            else:
                                try:
                                    print("ki Take Action")
                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                    banUserByMid(op.param2)
                                except:
                                    print("cl Exception Take Action")
                                    cl.kickoutFromGroup(op.param1,[op.param2])
                                    banUserByMid(op.param2)

                    else:
                        pass
                elif op.type == 11:
                    if op.param1 in protectedGroup:
                        if ki.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 in Bots:
                                pass 
                            elif op.param2 in admin:
                                pass
                            elif op.param2 in groupAdmin[op.param1]:
                                pass
                            else:
                                try:
                                    ki.sendText(op.param1,cl.getContact(op.param2).displayName + "Jangan Buka Kode QR Njiiir")
                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                    X = ki.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    ki.updateGroup(X)
                                except:
                                    cl.sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + "Jangan Buka Kode QR Njiiir")
                                    cl.kickoutFromGroup(op.param1,[op.param2])
                                    Z = cl.getGroup(op.param1)
                                    Z.preventedJoinByTicket = True
                                    cl.updateGroup(Z)
                    else:
                        pass
                elif op.type == 13:
                    if op.param1 in protectedGroup:
                        if op.param3 in Bots:
                            if wait["autoJoin"] == True:
                                x=0
                                k=0
                                for val in Bots:
                                    if val == op.param3:
                                        k=x
                                    x=x+1
                                if op.param2 in Bots:
                                    KAC[k].acceptGroupInvitation(op.param1)
                                elif op.param2 in admin:
                                    KAC[k].acceptGroupInvitation(op.param1)
                                elif op.param2 in groupAdmin[op.param1]:
                                    KAC[k].acceptGroupInvitation(op.param1)
                                else:
                                    KAC[k].rejectGroupInvitation(op.param1)
                            else:
                                pass
                        elif wait["Protectcancl"] == True:
                            group = cl.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            if op.param2 in Bots:
                                pass
                            elif op.param2 in admin:
                                pass
                            elif op.param2 in groupAdmin[op.param1]:
                                pass
                            else:
                                try:
                                    ki.cancelGroupInvitation(op.param1, gMembMids)
                                    ki.sendMessage(op.param1, "Mau Ngundang Siapa Ka?\nKk Bukan Admin\nJadi Aku Cancel😛")
                                except:
                                    cl.cancelGroupInvitation(op.param1, gMembMids)
                                    cl.sendMessage(op.param1, "Mau Ngundang Siapa Ka?\nKk Bukan Admin\nJadi Aku Cancel😛")
                        else:
                            pass
                    else:
                        pass       
    #=========================================================================================================================================#

def runPoll():
    while True:
        try:
            ops=poll.singleTrace(count=50)
            if ops != None:
              for op in ops: 
                bot(op)
                poll.setRevision(op.revision)
                
        except Exception as e:
            client.log("[FAHRI_SINGLE_TRACE] ERROR : " + str(e))

def runkiPoll():
    while True:
        try:
            ops=kipoll.singleTrace(count=50)
            if ops != None:
              for op in ops: 
                bot(op)
                kipoll.setRevision(op.revision)
                
        except Exception as e:
            client.log("[FELLY_SINGLE_TRACE] ERROR : " + str(e))

#Command ini otomatis dijalankan jika restart bot sudah sukses
#
if restartVar['isRestart'] == True:
    recv=restartVar['restartIn']
    restartVar['isRestart'] = False
    restartVar['restartIn'] = ''
    startTime = time.time()
    print(startTime)
    print('\n'+repr(startTime))
    fellyCfgUpdate()
    cl.sendMessage(recv,'Wayang Restarted')
else:
    if startTime == 0:
        startTime = time.time()
        print(startTime)
        print('\n'+repr(startTime))
        fellyCfgUpdate()

print("Running cekHStore() Thread\n")
Thread(target=cekHStore).start()
print("Running bot(fahri) Thread\n")
Thread(target=runPoll).start()
# print("Running bot(felly) Thread\n")
# Thread(target=runkiPoll).start()
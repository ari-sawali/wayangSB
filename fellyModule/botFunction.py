# -*- coding: utf-8 -*-
from fellyModule.botCfg import *
import json, requests, time
from bs4 import BeautifulSoup
from PyLyrics import *

def get_memes():
    url = 'https://api.imgflip.com/get_memes'
    r = requests.get(url)
    r.raise_for_status()
    response = r.json()
    if response['success']:
        return response['data']['memes']
    else:
        raise RuntimeError("Imgflip returned error message: " + response['error_message'])

def imgflipMeme(upper_text,lower_text,template_id,font="impact"):
    username = "kopisusu"
    password = "kopisusu27"
    text0 = upper_text
    text1 = lower_text
    url = "https://api.imgflip.com/caption_image"
    mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
    payload = {'username':username, 'password':password, 'template_id':template_id, 'text0':text0, 'text1':text1, 'font':font}
    req = requests.post(url, data=payload)
    req.raise_for_status()
    response = req.json()
    if response['success']:
        return response['data']
    else:
        raise RuntimeError("Imgflip returned error message: " + response['error_message'])

def getAlbums(query):
    albums = PyLyrics.getAlbums(singer=query)
    x=1
    rs="List Albums of "+query+"\n"
    for a in albums:
        rs += str(x)+'. '+str(a)+'\n'
        x=x+1
    return rs

def getTracks(query):
    listAlbums=[]
    txt=query.split("|")
    artist=txt[0]
    number=int(txt[1])
    number=number-1
    albums = PyLyrics.getAlbums(singer=artist)
    for a in albums:
        listAlbums.append(str(a))
    myalbum = albums[number] #Select your album based on Index

    tracks = myalbum.tracks() #or PyLyrics.getTracks(myalbum)
    result = "List Tracks ("+artist+": "+listAlbums[number]+")\n"
    x=1
    for track in tracks:
        result += str(x)+'. '+str(track)+'\n'
        x=x+1
    return result 

def getLyrics(query):
    txt=query.split('|')
    artist=txt[0]
    song=txt[1]
    print((artist+'-'+song))
    # print (PyLyrics.getLyrics(artist,song))
    return PyLyrics.getLyrics(artist,song)

def fellyCfgUpdate():
    cctv={
        "cyduk":{},
        "point":{},
        "sidermem":{},
        "haloSider":{}
    }
    f = open( 'fellyModule/botCfg.py', 'w' )
    f.write( 
            '# -*- coding: utf-8 -*-' + '\n' +
            'botmode = ' + repr(botmode) + '\n' +
            'startTime = ' + repr(startTime) + '\n' +
            'cctv = ' + repr(cctv) + '\n' +
            'wait = ' + repr(wait) + '\n' +
            'boten = ' + repr(boten) + '\n' +
            'owner = ' + repr(owner) + '\n' +
            'admin = ' + repr(admin) + '\n' +
            'whitelist = ' + repr(whitelist) + '\n' +
            'grouplist = ' + repr(grouplist) + '\n' +
            'groupAdmin = ' + repr(groupAdmin) + '\n' +
            'bigGroupId = ' + repr(bigGroupId) + '\n' +
            'helpMessage = ' + repr(helpMessage) + '\n' +
            'helpAdmin = ' + repr(helpAdmin) + '\n' +
            'helpOwner = ' + repr(helpOwner) + '\n' +
            'helpFooter = ' + repr(helpFooter) + '\n' +
            'restartVar = ' + repr(restartVar) + '\n' +
            'protectedGroup = ' + repr(protectedGroup) + '\n' +
            'autoFind = ' + repr(autoFind) + '\n' +
            'autoHStore = ' + repr(autoHStore) + '\n' +
            'autoPowerUp = ' + repr(autoPowerUp) + '\n' +
            'autoJoinBattle = ' + repr(autoJoinBattle) + '\n' +
            'customVar = ' + repr(customVar) + '\n'
        )
    f.close()

def tagall(kx,receiver):
    exec_start=time.time()
    try:
        group = kx.getGroup(receiver)
        nama = [contact.mid for contact in group.members]
        nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
        if jml <= 100:
            kx.mention(receiver, nama)
        if jml > 100 and jml <= 200:
            for i in range(0, 100):
                nm1 += [nama[i]]
            kx.mention(receiver, nm1)
            for j in range(100, len(nama)):
                nm2 += [nama[j]]
            kx.mention(receiver, nm2)
        if jml > 200 and jml <= 300:
            for i in range(0, 100):
                nm1 += [nama[i]]
            kx.mention(receiver, nm1)
            for j in range(100, 200):
                nm2 += [nama[j]]
            kx.mention(receiver, nm2)
            for k in range(200, len(nama)):
                nm3 += [nama[k]]
            kx.mention(receiver, nm3)
        if jml > 300 and jml <= 400:
            for i in range(0, 100):
                nm1 += [nama[i]]
            kx.mention(receiver, nm1)
            for j in range(100, 200):
                nm2 += [nama[j]]
            kx.mention(receiver, nm2)
            for k in range(200, 300):
                nm3 += [nama[k]]
            kx.mention(receiver, nm3)
            for l in range(300, len(nama)):
                nm4 += [nama[l]]
            kx.mention(receiver, nm4)
        if jml > 400 and jml < 501:
            for i in range(0, 100):
                nm1 += [nama[i]]
            kx.mention(receiver, nm1)
            for j in range(100, 200):
                nm2 += [nama[j]]
            kx.mention(receiver, nm2)
            for k in range(200, 300):
                nm3 += [nama[k]]
            kx.mention(receiver, nm3)
            for l in range(300, 400):
                nm4 += [nama[l]]
            kx.mention(receiver, nm4)
            for m in range(400, len(nama)):
                nm5 += [nama[m]]
            kx.mention(receiver, nm5)
        if wait["autoBattle"] == True:
            if wait["battleMode"] == "battle":
                kx.sendMessage(wait["groupId"],"/battle")
            elif wait["battleMode"] == "summon":
                kx.sendMessage(wait["groupId"],"/summon")
            elif wait["battleMode"] == "guildwar":
                kx.sendMessage(wait["groupId"],"/guildwar")
            else:
                pass
        else:
            pass
        exec_finish=time.time()
        elapsed_time=exec_finish-exec_start
        kx.sendMessage(receiver, "%sdetik" % (elapsed_time))
    except Exception as e:
        print(e)

def tagadmin(kx,receiver):
    try:
        group = kx.getGroup(receiver)
        nama = [contact.mid for contact in group.members]
        md=[]
        for nm in nama:
            if nm in admin:
                md+=[nm]
            elif nm in groupAdmin[receiver]:
                md+=[nm]
        kx.mention(receiver, md)
    except Exception as e:
        print(e)

def isBotJoined(kx,Bots,receiver):
    try:
        group = kx.getGroup(receiver)
        nama = [contact.mid for contact in group.members]
        md=[]
        for nm in nama:
            if nm in Bots:
                md.append(nm)
        return md
    except Exception as e:
        print(e)

def getAdminList(kx,receiver):
    if admin == []:
        return "The stafflist is empty"
    else:
        mc = "◄]·♦·Admin Wayang Dugem·♦·[►\n\n"
        for mi_d in admin:
            mc += "••>" +kx.getContact(mi_d).displayName + "\n"
    print("Global Admin :"+mc+"\n\n")
    if receiver in grouplist:
        mc += "\n◄]·♦·Admin Grup Ini·♦·[►\n\n"
        if groupAdmin[receiver]!=[] or groupAdmin[receiver]!=['']:
            for ga in groupAdmin[receiver]:
                print(ga)
                if ga != ['']:
                    mc += "••>" +kx.getContact(ga).displayName + "\n"
        else:
            mc+="••>Belum ada Admin Grup\n"
    return mc

def getCalonAdmin(KAC,receiver,text):
    _name = "";    
    if "grAdmin add @" in text:
        _name = text.replace("grAdmin add @","")
    elif "grAdmin remove @" in text:
        _name = text.replace("grAdmin remove @","")
    elif "Admin add @" in text:
        _name = text.replace("Admin add @","")
    elif "Admin remove @" in text:
        _name = text.replace("Admin remove @","")
    _nametarget = _name.rstrip('  ')
    print(_nametarget+"\n")
    gs = KAC[0].getGroup(receiver)
    # gs = KAC[1].getGroup(receiver)
    # gs = KAC[2].getGroup(receiver)
    # gs = KAC[3].getGroup(receiver)
    # gs = KAC[4].getGroup(receiver)
    targets = []
    print(gs.members)
    print("\n")
    for g in gs.members:
        if _nametarget == g.displayName:
            targets.append(g.mid)
    return targets

def getGroupList(kx):
    mc="Group List\n\n"
    if grouplist == [] or grouplist == [""]:
        mc+="---Empty---"
    else:
        for grlist in grouplist:
            if grlist != '':
                g=kx.getGroup(grlist)
                protection="No"
                print(g)
                print("\n")
                if grlist in protectedGroup:
                    protection="Yes"
                mc+="••>" + g.name + "\n" + "[•]Group Id : " + g.id + "\n" + "[•]Group Creator : " + g.creator.displayName + "\n" + "[•]Protection : " + protection + "\n\n"
    return mc

def cancelInvitation(kx,receiver):
    result_msg=''
    try:
        X = kx.getGroup(receiver)
        if X.invitee is not None:
            gInviMids = [contact.mid for contact in X.invitee]
            kx.cancelGroupInvitation(receiver, gInviMids)
            result_msg="Cancel Invitation Done"
        else:
            if wait["lang"] == "JP":
                result_msg="No one is inviting"
            else:
                result_msg="Sorry, nobody absent"
    except Exception as e:
        result_msg=str(e)
    return result_msg

def openQr(kx,receiver):
    result_msg=''
    try:
        X = kx.getGroup(receiver)
        X.preventedJoinByTicket = False
        kx.updateGroup(X)
        if wait["lang"] == "JP":
            result_msg="QR Sudah Dibuka"
        else:
            result_msg="Sudah Terbuka Unch"
    except Exception as e:
        result_msg=str(e)
    return result_msg

def closeQr(kx,receiver):
    result_msg=''
    try:
        X = kx.getGroup(receiver)
        X.preventedJoinByTicket = True
        kx.updateGroup(X)
        if wait["lang"] == "JP":
            result_msg="QR Sudah Ditutup"
        else:
            result_msg="Sudah Tertutup Unch"
    except Exception as e:
        result_msg=str(e)
    return result_msg

def gurl(kx,receiver):
    x = kx.getGroup(receiver)
    if x.preventedJoinByTicket == True:
        x.preventedJoinByTicket = False
        kx.updateGroup(x)
    gurl = kx.reissueGroupTicket(receiver)
    result="line://ti/g/" + gurl
    return result

def nameKick(kx,msg):
    result=''
    targets = []
    key = eval(msg.contentMetadata["MENTION"])
    key["MENTIONEES"] [0] ["M"]
    for x in key["MENTIONEES"]:
        targets.append(x["M"])
    for target in targets:
        try:
            kx.kickoutFromGroup(msg.to,[target])
            result="Target Has Been Slain"
        except Exception as e:
            result=str(e)
    return result

def banUser(kx,receiver,text):
    result=''
    _name = text.replace(".blacklist @","")
    _kicktarget = _name.rstrip(' ')
    gs = kx.getGroup(receiver)
    targets = []
    for g in gs.members:
        if _kicktarget == g.displayName:
            targets.append(g.mid)
    if targets == []:
        result="Not found"
    else:
        for target in targets:
            if target in owner:
                result="Busettt Ya Kali Owner di Banned"
            elif target in admin:
                result="Busettt Ya Kali Admin di Banned"
            elif target in groupAdmin:
                result="Busettt Ya Kali Admin Grup di Banned"
            elif target in Bots:
                result="Eitss Ga Boleh Banned Bot ya Kakak"
            elif target in whitelist:
                result="Target ada di dalam white list"
            else:
                try:
                    wait["blacklist"][target] = True
                    f=codecs.open('st2__b.json','w','utf-8')
                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                    result="Target Added to Black List Unch"
                except Exception as e:
                    result=str(e)
    return result

def banUserByMid(target):
    result=''
    try:
        wait["blacklist"][target] = True
        f=codecs.open('st2__b.json','w','utf-8')
        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
        result="Target Added to Black List"
    except Exception as e:
        result=str(e)
    return result

def unbanUser(kx,receiver,text):
    result=''
    _name = text.replace(".unban @","")
    _nametarget = _name.rstrip('  ')
    gs = kx.getGroup(receiver)
    targets = []
    for g in gs.members:
        if _nametarget == g.displayName:
            targets.append(g.mid)
    if targets == []:
        result="Tidak Ditemukan....."
    else:
        for target in targets:
            try:
                del wait["blacklist"][target]
                f=codecs.open('st2__b.json','w','utf-8')
                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                result="Akun Bersih Kembali"
            except Exception as e:
                result=str(e)
    return result

def cekBanlist(kx):
    result=''
    if wait["blacklist"] == {}:
        result="Tidak Ada Akun Terbanned"
    else:
        mc = "Black List User"
        for mi_d in wait["blacklist"]:
            mc += "->" +kx.getContact(mi_d).displayName + "\n"
        result=mc
    return result

def addWhitelist(kx,receiver,text):
    result=''
    _name = text.replace(".wladd @","")
    _wltarget = _name.rstrip(' ')
    gs = kx.getGroup(receiver)
    targets = []
    for g in gs.members:
        if _wltarget == g.displayName:
            targets.append(g.mid)
    if targets == []:
        result="Not found"
    else:
        for target in targets:
            if target in owner:
                result="Target adalah Owner"
            elif target in admin:
                result="Target adalah Admin"
            elif target in groupAdmin:
                result="Target adalah Admin Grup"
            elif target in Bots:
                result="Target adalah Bot Wayang"
            elif target in wait["blacklist"]:
                result="Target ada di dalam black list"
            else:
                try:
                    whitelist.append(str(target))
                    result="Target Added to White List\nKimotih!!!"
                except Exception as e:
                    result=str(e)
    return result

def removeWhitelist(kx,receiver,text):
    result=''
    _name = text.replace(".wlremove @","")
    _nametarget = _name.rstrip('  ')
    gs = kx.getGroup(receiver)
    targets = []
    for g in gs.members:
        if _nametarget == g.displayName:
            targets.append(g.mid)
    if targets == []:
        result="Tidak Ditemukan....."
    else:
        for target in targets:
            try:
                whitelist.remove(target)
                result="Target Dihapus dari White List"
            except Exception as e:
                result=str(e)
    return result

def cekWhitelist(kx):
    result=''
    if whitelist == []:
        result="White List Empty"
    else:
        mc = "White List User"
        for mi_d in whitelist:
            mc += "->" +kx.getContact(mi_d).displayName + "\n"
        result=mc
    return result

def inviteBot(KAC,receiver):
    try:
        ax=KAC[0]
        G = ax.getGroup(receiver)
        G.preventedJoinByTicket = False
        ax.updateGroup(G)
        invsend = 0
        Ticket = ax.reissueGroupTicket(receiver)
        KAC.remove(KAC[0])
        for x in KAC:
            x.acceptGroupInvitationByTicket(receiver,Ticket)
            time.sleep(0.01)
        G = ax.getGroup(receiver)
        G.preventedJoinByTicket = True
        ax.updateGroup(G)
        return "Invite BOT Done"
    except Exception as e:
        return str(e)

#==============Auto Gacha hero=========================================================#

def setAutoFind(usermid,data):
    resmsg=""
    try:
        autoFind[str(usermid)]={}
        autoFind[str(usermid)]["herotype"]=data[2]
        autoFind[str(usermid)]["heroname"]=data[3]
        autoFind[str(usermid)]["server"]=str(boten[int(data[4])-1])
        autoFind[str(usermid)]["slot"]=int(data[5])
        fellyCfgUpdate()
        resmsg="Done ON"
    except Exception as e:
        print("trying on "+str(e))
        resmsg=str(e)
    return resmsg

def unsetAutoFind(usermid):
    resmsg=''
    try:
        autoFind.pop(usermid,None)
        fellyCfgUpdate()
        resmsg="Done OFF"
    except Exception as e:
        resmsg=str(e)
    return resmsg
    
def cekAutoFind(usermid):
    resmsg=''
    try:
        if autoFind == {}:
            resmsg="Auto Find OFF"
        else:
            resmsg="Auto Find\n\n"
            resmsg+="Hero Type : "+autoFind[usermid]["herotype"]+"\n"
            resmsg+="Hero Name : "+autoFind[usermid]["heroname"]+"\n"
            resmsg+="Slot Numb : "+str(autoFind[usermid]["slot"])+"\n"
    except Exception as e:
        resmsg=str(e)
    return resmsg
             
#=======================================================================================#

#==============Auto Gacha hero==========================================================#

def setAutoHStore(usermid,data):
    resmsg=""
    try:
        print("Set HStore Parameter\n")
        autoHStore[str(usermid)]={}
        autoHStore[str(usermid)]["herotype"]=data[2]
        autoHStore[str(usermid)]["heroname"]=data[3]
        autoHStore[str(usermid)]["server"]=str(boten[int(data[4])-1])
        autoHStore[str(usermid)]["price"]=str(data[5])
        print(str(len(data))+"\n")
        if len(data) > 6:
            print("Set Slot if data > 6")
            autoHStore[str(usermid)]["slot"]=int(data[6])
        else:
            print("Set Slot if only 6 data provided")
            autoHStore[str(usermid)]["slot"]=0
        autoHStore[str(usermid)]["start"]=False
        autoHStore[str(usermid)]["cooldown"]=False
        print("HStore Parameter has been set")
        fellyCfgUpdate()
        resmsg="Done ON"
    except Exception as e:
        print("trying on "+str(e))
        resmsg=str(e)
    return resmsg

def unsetAutoHStore(usermid):
    resmsg=''
    try:
        autoHStore.pop(usermid,None)
        fellyCfgUpdate()
        resmsg="Done OFF"
    except Exception as e:
        resmsg=str(e)
    return resmsg
    
def cekAutoHStore(usermid):
    resmsg=''
    try:
        if autoHStore == {}:
            resmsg="Auto HStore OFF"
        else:
            resmsg="Auto HStore\n\n"
            resmsg+="Hero Type : "+autoHStore[usermid]["herotype"]+"\n"
            resmsg+="Hero Name : "+autoHStore[usermid]["heroname"]+"\n"
            resmsg+="Hero Price : "+autoHStore[usermid]["price"]+"\n"
            if autoHStore[usermid]["start"] == True:
                resmsg+="Status : Running"
            else:
                resmsg+="Status : Paused"
    except Exception as e:
        resmsg=str(e)
    return resmsg

def startStopAutoHStore(usermid,data):
    result=''
    try:
        if data.lower()=="start":
            if autoHStore[str(usermid)]["start"]==True:
                result={'result': False, 'resmsg': 'Already Start'}
            else:
                autoHStore[str(usermid)]["start"]=True
                fellyCfgUpdate()
                result={'result': True, 'resmsg': 'Sukses Start'}
        elif data.lower()=="stop":
            if autoHStore[str(usermid)]["start"]==True:
                autoHStore[str(usermid)]["start"]=False
                fellyCfgUpdate()
                result={'result': True, 'resmsg': 'Sukses Stop'}
            else:
                result={'result': False, 'resmsg': 'Already Stop'}
    except Exception as e:
        resmsg=str(e)
        result={'result': False, 'resmsg': resmsg}
    return result

#=======================================================================================#
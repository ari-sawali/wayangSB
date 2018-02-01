# -*- coding: utf-8 -*-
from linepy import *
from fellyModule.botLogin import *
from fellyModule.botCfg import *
from fellyModule.botFunction import *
import logging

def restart_program():
    python2 = sys.executable
    os.execl(python2, python2, * sys.argv)

def shutdown():
    sys.exit()

while True:
    try:
        ops=poll.singleTrace(count=50)
        if ops!=None:
            for op in ops:
                if op.type == 19: #bot Ke Kick
                    print(op)
                    if op.param3 in Bots:
                        try:
                          print("ki Take Action")
                          G = ki.getGroup(op.param1)
                          G.preventedJoinByTicket = False
                          ki.updateGroup(G)
                          Ticket = ki.reissueGroupTicket(op.param1)
                          cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                          time.sleep(0.01)
                          G.preventedJoinByTicket = True
                          ki.updateGroup(G)
                        except:
                          print("cl Exception Take Action")
                          G = cl.getGroup(op.param1)
                          G.preventedJoinByTicket = False
                          cl.updateGroup(G)
                          Ticket = cl.reissueGroupTicket(op.param1)
                          ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                          time.sleep(0.01)
                          G.preventedJoinByTicket = True
                          cl.updateGroup(G)
                elif op.type == 18:
                    print("Fahri disini\n")
                    print(op)
                elif op.type == 25:
                    msg = op.message
                    text = msg.text
                    msg_id = msg.id
                    receiver = msg.to
                    sender = msg._from
                    try:
                        if msg.contentType == 0:
                            if text.lower() == '.ceksend':
                                cl.sendMessage(msg.to,"Send Message Ok")
                    except Exception as e:
                        cl.sendMessage(receiver,str(e))
                poll.setRevision(op.revision)

        # kiops=kipoll.singleTrace(count=50)
        # if kiops!=None:
        #     for kiop in kiops:
        #         if kiop.type == 19: #bot Ke Kick
        #             print(kiop)
        #             if kiop.param3 in Bots:
        #                 try:
        #                   print("cl Take Action")
        #                   G = cl.getGroup(kiop.param1)
        #                   G.preventedJoinByTicket = False
        #                   cl.updateGroup(G)
        #                   Ticket = cl.reissueGroupTicket(kiop.param1)
        #                   ki.acceptGroupInvitationByTicket(kiop.param1,Ticket)
        #                   time.sleep(0.01)
        #                   G.preventedJoinByTicket = True
        #                   cl.updateGroup(G)
        #                 except:
        #                   print("ki Exception Take Action")
        #                   G = ki.getGroup(op.param1)
        #                   G.preventedJoinByTicket = False
        #                   ki.updateGroup(G)
        #                   Ticket = ki.reissueGroupTicket(op.param1)
        #                   cl.acceptGroupInvitationByTicket(op.param1,Ticket)
        #                   time.sleep(0.01)
        #                   G.preventedJoinByTicket = True
        #                   ki.updateGroup(G)
        #         elif kiop.type == 18:
        #             print("Felly disini\n")
        #             print(kiop)
        #             print("\n")
        #         elif kiop.type == 26:
        #             print("Felly disini lg read\n")
        #             print(kiop)
        #             print("\n")
        #         kipoll.setRevision(kiop.revision)
    except Exception as e:
        client.log("[SINGLE_TRACE] ERROR : " + str(e))
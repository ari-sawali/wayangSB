# -*- coding: utf-8 -*-
from linepy import *
import time

line = LINE(idOrAuthToken="EoMpcu0LXJGsaKCAiCu0.JUROxzdkKD3c/MrJQ951aa.wRm5q/STR+Fk8DA55FVeIXs+2HEAqbJzyiTp1XPhBh4=")
#line = LINE('AUTHTOKEN')

line.log("Auth Token : " + str(line.authToken))
squareChatMid='s3825e0558cc9b4598fb9f557e113eeb1' # Get manual from line.getJoinableSquareChats('YOUR_SQUARE_MID')

# Initialize OEPoll with LINE instance
oepoll = OEPoll(line)

while True:
    try:
        eventsSquareChat=oepoll.singleFetchSquareChat(squareChatMid=squareChatMid)
        for e in eventsSquareChat:
            if e.createdTime is not 0:
                ts_old = int(e.createdTime) / 1000
                ts_now = int(time.time())
                line.log('[FETCH_TIME] ' + str(int(e.createdTime)))
                if ts_old >= ts_now:
                    '''
                        This is sample for implement BOT in LINE square
                        BOT will noticed who leave square chat
                        Command availabe :
                        > hi
                        > /author
                    '''
                    # Receive messages
                    if e.payload.receiveMessage != None:
                        payload=e.payload.receiveMessage
                        line.log('[RECEIVE_MESSAGE]')
                        msg=payload.squareMessage.message
                        msg_id=msg.id
                        receiver_id=msg._from
                        sender_id=msg.to
                        line.log('%s' % msg)
                    # Notified leave Square Chat
                    elif e.payload.notifiedLeaveSquareChat != None:
                        payload=e.payload.notifiedLeaveSquareChat
                        line.log('[NOTIFIED_LEAVE_SQUARE_CHAT]')
                        squareMemberMid=payload.squareChatMid
                        squareMemberMid=payload.squareMemberMid
                        squareMember=payload.squareMember
                        displayName=squareMember.displayName
                        # line.sendSquareMessage(squareChatMid, 'Good bye! ' + str(displayName))
                    else:
                        pass
            
    except Exception as e:
        line.log("[FETCH_SQUARE] Fetch square chat error: " + str(e))

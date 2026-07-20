from fastapi import HTTPException

def itemDetail(session,materialFrom, materialDest, fromPlant, destPlant, fromLoc, destLoc, quantity, fromBatch, destBatch):

    try:
        try:
            shell = ("wnd[0]/usr/ssubSUB_MAIN_CARRIER:SAPLMIGO:0007/subSUB_ITEMDETAIL:SAPLMIGO:0303/subSUB_DETAIL:SAPLMIGO:0305/tabsTS_GOITEM/tabpOK_GOITEM_TRANS/ssubSUB_TS_GOITEM_TRANS:SAPLMIGO:0390/")
        except:
            shell = ("wnd[0]/usr/ssubSUB_MAIN_CARRIER:SAPLMIGO:0003/subSUB_ITEMDETAIL:SAPLMIGO:0303/subSUB_DETAIL:SAPLMIGO:0305/tabsTS_GOITEM/tabpOK_GOITEM_TRANS/ssubSUB_TS_GOITEM_TRANS:SAPLMIGO:0390/")

        session.findById(shell+"ctxtGODYNPRO-MAKTX").text= materialFrom
        session.findById(shell+"ctxtGOITEM-UMMAKTX").text= materialDest

        session.findById(shell+"ctxtGODYNPRO-NAME1").text = fromPlant
        session.findById(shell+"ctxtGODYNPRO-LGOBE").text = fromLoc
        session.findById(shell+"ctxtGOITEM-UMNAME1").text = destPlant
        session.findById(shell+"ctxtGOITEM-UMLGOBE").text = destLoc
        session.findById(shell+"txtGODYNPRO-ERFMG").text = quantity
        session.findById("wnd[0]").sendVKey(0)
        try:
            session.findById("wnd[0]/usr/ssubSUB_MAIN_CARRIER:SAPLMIGO:0007/subSUB_ITEMDETAIL:SAPLMIGO:0303/subSUB_DETAIL:SAPLMIGO:0305/tabsTS_GOITEM/tabpOK_GOITEM_TRANS/ssubSUB_TS_GOITEM_TRANS:SAPLMIGO:0390/ctxtGODYNPRO-CHARG").text = fromBatch
            session.findById("wnd[0]/usr/ssubSUB_MAIN_CARRIER:SAPLMIGO:0007/subSUB_ITEMDETAIL:SAPLMIGO:0303/subSUB_DETAIL:SAPLMIGO:0305/tabsTS_GOITEM/tabpOK_GOITEM_TRANS/ssubSUB_TS_GOITEM_TRANS:SAPLMIGO:0390/ctxtGODYNPRO-UMCHA").text = destBatch
        except:
            pass
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/tbar[1]/btn[23]").press()
        try:
            session.findById('wnd[1]')
            errormsg = session.findById("wnd[1]/usr/lbl[10,3]").text
            return {
                'success' : False,
                'error' : errormsg
                }
        except:
            return {'success' : True}

    except Exception as e:
        return {
            'success' : False,
            'error' : str(e)
            }

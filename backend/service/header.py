from fastapi import HTTPException
def header(session,headerText):
    try:
        print('in header')
        try:
            session.findById("wnd[0]/usr/ssubSUB_MAIN_CARRIER:SAPLMIGO:0003/subSUB_FIRSTLINE:SAPLMIGO:0011/cmbGODYNPRO-ACTION").key = "A08"
        except:
            session.findById("wnd[0]/usr/ssubSUB_MAIN_CARRIER:SAPLMIGO:0007/subSUB_FIRSTLINE:SAPLMIGO:0011/cmbGODYNPRO-ACTION").key = "A08"

        print('A08')
        session.findById("wnd[0]/usr/ssubSUB_MAIN_CARRIER:SAPLMIGO:0007/subSUB_FIRSTLINE:SAPLMIGO:0011/cmbGODYNPRO-REFDOC").key = "R10"
        print('R10')
        session.findById("wnd[0]/usr/ssubSUB_MAIN_CARRIER:SAPLMIGO:0007/subSUB_FIRSTLINE:SAPLMIGO:0011/ctxtGODEFAULT_TV-BWART").text = "309"
        print('309')
        session.findById("wnd[0]/usr/ssubSUB_MAIN_CARRIER:SAPLMIGO:0007/subSUB_HEADER:SAPLMIGO:0101/subSUB_HEADER:SAPLMIGO:0100/tabsTS_GOHEAD/tabpOK_GOHEAD_GENERAL").select()
        print('SELECTED')
        if not headerText == None:
            session.findById("wnd[0]/usr/ssubSUB_MAIN_CARRIER:SAPLMIGO:0007/subSUB_HEADER:SAPLMIGO:0101/subSUB_HEADER:SAPLMIGO:0100/tabsTS_GOHEAD/tabpOK_GOHEAD_GENERAL/ssubSUB_TS_GOHEAD_GENERAL:SAPLMIGO:0112/txtGOHEAD-BKTXT").text = headerText
            print(headerText)
        session.findById('wnd[0]').sendVKey(0)
        # session.findById('wnd[1010101]')
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error in header Information')


def gotoCode(session):
    try:
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nMIGO"
        session.findById("wnd[0]").sendVKey(0)
    except:
        raise ("Error: Cannot locate to Transaction MIGO")

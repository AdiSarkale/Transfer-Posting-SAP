from fastapi import HTTPException, APIRouter, UploadFile, File
import json
import pandas as pd


from service.connection import connection
from service.header import header
from service.itemDetail import itemDetail
from service.gotoCode import gotoCode
from service.docNumber import DocumentNumber
from schema.api import ApiResponse
from service.csvfile import readFile

router = APIRouter(prefix='/test',tags=['/Test'])


@router.post('/test',response_model=ApiResponse)
def main(file: UploadFile = File(...)):
    try:
        errors = []
        success_code = []
        res = []
        r = readFile(file.file)
        session = connection()
        size = len(r['materialFrom'])
        for i in range(size):
            headerText = r['headerText'][i]  if not pd.isna(r['headerText'][i]) else ' '
            gotoCode(session)
            header(session,headerText)
            materialFrom = r['materialFrom'][i]
            materialDest = r['materialDest'][i]
            fromPlant = r['fromPlant'][i]
            destPlant = r['destPlant'][i]
            fromLoc = r['fromLoc'][i]
            destLoc = r['destLoc'][i]
            quantity = r['quantity'][i]
            fromBatch = str(r['fromBatch'][i] if not pd.isna(r['fromBatch'][i]) else ' ').strip("'")
            destBatch = str(r['destBatch'][i] if not pd.isna(r['destBatch'][i]) else ' ').strip("'")
            print("B A T C H : ",fromBatch)
            # return

            print("fromBatch HERE is: ",fromBatch)
            result = itemDetail(session, materialFrom, materialDest, fromPlant, destPlant, fromLoc, destLoc, quantity, fromBatch,destBatch)

            if not result['success']:
                errors.append({
                    'row' : i + 1,
                    'From': f" {fromPlant} | {materialFrom} | {fromLoc} {f'➡️ {fromBatch}' if fromBatch != ' ' else ''} ",
                    'To' : f" {destPlant} | {materialDest} | {destLoc} {f'➡️ {destBatch}' if destBatch != ' '  else ''} ",
                    'message' : result['error']
                    })
                res.append({
                    'row' : i + 1,
                    'From' : f" {fromPlant} | {materialFrom} | {fromLoc} {f'➡️ {fromBatch}' if fromBatch != ' ' else ''} ",
                    'To' : f" {destPlant} | {materialDest} | {destLoc} {f'➡️ {destBatch}' if destBatch  != ' ' else ''} ",
                    'message' : result['error']
                    })
                continue
            status_bar_text = DocumentNumber(session)

            success_code.append({
                    'row' : i + 1,
                    'From': f" {fromPlant} | {materialFrom} | {fromLoc} {f'➡️ {fromBatch}' if fromBatch != ' ' else ''} ",
                    'To' : f" {destPlant} | {materialDest} | {destLoc} {f'➡️ {destBatch}' if destBatch != ' '  else ''} ",
                    'message' : status_bar_text
                    })
            res.append({
                    'row' : i + 1,
                    'From': f" {fromPlant} | {materialFrom} | {fromLoc} {f'➡️ {fromBatch}' if fromBatch != ' ' else ''} ",
                    'To' : f" {destPlant} | {materialDest} | {destLoc} {f'➡️ {destBatch}' if destBatch != ' '  else ''} ",
                    'message' : status_bar_text
                    })


        if not errors:
            return ApiResponse(success=True, message=f'Successfully Posted', data=res)
        else:
            return ApiResponse(success=True, message='Posted With Errors', data=res)

    except Exception as e:
        return ApiResponse(success=False, message=str(e), data=None)






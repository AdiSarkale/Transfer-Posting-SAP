from pydantic import BaseModel

class PostData(BaseModel):
    docHeader : str = 'SOME HEADER TEXT'
    materialFrom : str = '1000000133'
    materialDest : str = '1000000029'
    fromPlant : str = '1002'
    destPlant : str = '1002'
    fromLoc : str = 'CN01'
    destLoc : str = 'CN01'
    quantity : str = '10'

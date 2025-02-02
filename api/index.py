from fastapi import FastAPI, Query
from typing import List
import json

app = FastAPI()

# Load student marks data directly
STUDENT_MARKS = [
    {"name":"RnFdwiS","marks":48},{"name":"0","marks":13},{"name":"79","marks":79},{"name":"s","marks":52},{"name":"MmzK5K","marks":48},{"name":"J","marks":37},{"name":"LK9bob0","marks":68},{"name":"EVda","marks":96},{"name":"GDf","marks":38},{"name":"fdnxY48Ai","marks":42},{"name":"9bvxpEIvq","marks":79},{"name":"HX7styaPV","marks":63},{"name":"jcGpjDA1","marks":62},{"name":"18rK","marks":76},{"name":"kYu","marks":58},{"name":"Zh33XKg","marks":82},{"name":"1rnN","marks":52},{"name":"YjV","marks":21},{"name":"KXN8ImVTQ","marks":82},{"name":"1xKR","marks":28},{"name":"uS","marks":64},{"name":"SFkJb","marks":86},{"name":"oOS9dm0j0N","marks":92},{"name":"GCR","marks":39},{"name":"4Hsatne4","marks":17},{"name":"sQwMSn7","marks":5},{"name":"Nwzi8","marks":46},{"name":"h","marks":74},{"name":"Wc01EzW","marks":77},{"name":"IBmMAiBx","marks":95},{"name":"lp4wA","marks":24},{"name":"wQbSFPUjey","marks":11},{"name":"Wd","marks":11},{"name":"0Rio","marks":22},{"name":"SdBj7n2hVK","marks":82},{"name":"UcGPQYpJXo","marks":8},{"name":"mOR","marks":55},{"name":"IL2a2D","marks":5},{"name":"7U","marks":87},{"name":"z4nKGg2x","marks":77},{"name":"Ylv","marks":14},{"name":"HsOG","marks":0},{"name":"c2kVvWgBM","marks":31},{"name":"phW3","marks":77},{"name":"xVM3f0jhlf","marks":92},{"name":"UYjVzO","marks":3},{"name":"EGR","marks":61},{"name":"CJ3g2zzk","marks":20},{"name":"KJ52hAe","marks":57},{"name":"s5J","marks":30},{"name":"FJE","marks":89},{"name":"IGn","marks":56},{"name":"DCHD","marks":1},{"name":"wkGFStCV","marks":0},{"name":"0YWETORrdQ","marks":99},{"name":"AyQIk","marks":96},{"name":"Oustp","marks":10},{"name":"rLYamN","marks":82},{"name":"qQBd","marks":49},{"name":"1HClGnF","marks":6},{"name":"g0WBpYv","marks":37},{"name":"EyM5z8W","marks":11},{"name":"cqVkGg","marks":63},{"name":"YH8024gm","marks":78},{"name":"6cRs4pgiU","marks":80},{"name":"Qe","marks":63},{"name":"FWBZVx3u","marks":26},{"name":"jL7VXrpgkv","marks":24},{"name":"k","marks":95},{"name":"ersrZi22Fo","marks":51},{"name":"NEjhBGK","marks":88},{"name":"8Q9M7bRY","marks":81},{"name":"gXciZb8o","marks":18},{"name":"EP","marks":58},{"name":"zzgaUm","marks":1},{"name":"iR","marks":8},{"name":"2Wgr","marks":18},{"name":"l","marks":52},{"name":"hs1Wk1","marks":8},{"name":"Z4QUuUPGh","marks":43},{"name":"lK0ATHrBn","marks":30},{"name":"alNrFhvhsb","marks":88},{"name":"bfeu6","marks":97},{"name":"E","marks":19},{"name":"rdW2RlLIA","marks":41},{"name":"cIsR","marks":70},{"name":"mzPxvq39","marks":13},{"name":"Dx","marks":59},{"name":"tRrFA","marks":18},{"name":"fxuF4Sv2","marks":52},{"name":"wzpcnJ","marks":7},{"name":"HmG5GH2","marks":82},{"name":"gv1jOJwUOT","marks":49},{"name":"Jd5o0O","marks":71},{"name":"5","marks":98},{"name":"D","marks":89},{"name":"WZeY7a","marks":96},{"name":"N83f","marks":22},{"name":"7YLBnDFwfD","marks":15},{"name":"e","marks":89}
]

@app.get("/")
async def root():
    return {"message": "Student Marks API"}

@app.get("/api")
async def get_marks(name: List[str] = Query(...)):
    # Create a lookup dictionary for faster access
    marks_dict = {student['name']: student['marks'] for student in STUDENT_MARKS}
    marks = [marks_dict.get(n) for n in name]
    return {"marks": marks}

# Add CORS headers
@app.middleware("http")
async def add_cors_headers(request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    return response

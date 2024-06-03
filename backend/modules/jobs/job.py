from fastapi import APIRouter, Depends
from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer

from modules.serializers.jobSerializers import jobListEntity
from modules.database import Job
from modules import schemas
from modules.auth import oauth2
import re

def escape_regex(text):
    return re.escape(text)

router = APIRouter()

security = HTTPBearer()

@router.get('/search', response_model=schemas.JobResponse)
def search( job_name: str|None,user_id: str = Depends(oauth2.require_user) ):
    if job_name:
        regex = re.compile(escape_regex(job_name), re.IGNORECASE)
        query = {"job_name": {"$regex": regex}}
        jobs = jobListEntity(Job.find(query))
    else:
        jobs = jobListEntity(Job.find())
    return {"status": "success", "jobs": jobs}
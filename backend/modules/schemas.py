from datetime import datetime
from pydantic import BaseModel, EmailStr, constr
from typing import List

##User
class UserBaseSchema(BaseModel):
    name: str | None = None
    email: str
    role: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        orm_mode = True

class CreateUserSchema(UserBaseSchema):
    password: constr(min_length=8)
    passwordConfirm: str
    verified: bool = False

class LoginUserSchema(BaseModel):
    email: EmailStr
    password: constr(min_length=8)

class UserResponseSchema(UserBaseSchema):
    id: str
    pass

class UserResponse(BaseModel):
    status: str
    user: UserResponseSchema

##Job
class JobBaseSchema(BaseModel):
    id: str
    # post_id: str | None = None
    job_name: str
    company_name: str | None = None
    job_full_text: str | None = None
    # post_url: str | None = None
    # post_apply_url: str | None = None
    # company_url: str | None = None
    # company_industry: str | None = None
    # minimum_compensation: str | None = None
    # maximum_compensation: str | None = None
    # compensation_type: str | None = None
    # job_hours: str | None = None
    # role_seniority: str | None = None
    # minimum_education: str | None = None
    # office_location: str | None = None
    # post_html: str | None = None
    # city: str | None = None
    # region: str | None = None
    # country: str | None = None
    # job_published_at:  str | None = None
    # last_indexed:  str | None = None

    class Config:
        orm_mode = True

class JobResponseSchema(JobBaseSchema):
    id: str
    pass

class JobResponse(BaseModel):
    status: str
    jobs: List[JobResponseSchema]

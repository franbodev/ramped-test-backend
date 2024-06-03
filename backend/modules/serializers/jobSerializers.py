def jobEntity(job) -> dict:
    return {
        "id": str(job["_id"]),
        "post_id": job["post_id"],
        "job_name": job["job_name"],
        "company_name": job["company_name"],
        "job_full_text": job["job_full_text"],
        "post_url": job["post_url"],
        "post_apply_url": job["post_apply_url"],
        "company_url": job["company_url"],
        "Company Industry": job["Company Industry"],
        "Minimum Compensation": job["Minimum Compensation"],
        "Maximum Compensation": job["Maximum Compensation"],
        "Compensation Type": job["Compensation Type"],
        "Job Hours": job["Job Hours"],
        "Role Seniority": job["Role Seniority"],
        "Minimum Education": job["Minimum Education"],
        "Office Location": job["Office Location"],
        "post_html": job["post_html"],
        "city": job["city"],
        "region": job["region"],
        "country": job["country"],
        "job_published_at":  job["job_published_at"],
        "last_indexed":  job["last_indexed"],
    }


def jobResponseEntity(job) -> dict:
    return {
        "id": str(job["_id"]),
        "post_id": job["post_id"],
        "job_name": job["job_name"],
        "company_name": job["company_name"],
        "job_full_text": job["job_full_text"],
        "post_url": job["post_url"],
        "post_apply_url": job["post_apply_url"],
        "company_url": job["company_url"],
        "Company Industry": job["Company Industry"],
        "Minimum Compensation": job["Minimum Compensation"],
        "Maximum Compensation": job["Maximum Compensation"],
        "Compensation Type": job["Compensation Type"],
        "Job Hours": job["Job Hours"],
        "Role Seniority": job["Role Seniority"],
        "Minimum Education": job["Minimum Education"],
        "Office Location": job["Office Location"],
        "post_html": job["post_html"],
        "city": job["city"],
        "region": job["region"],
        "country": job["country"],
        "job_published_at":  job["job_published_at"],
        "last_indexed":  job["last_indexed"],
    }


def embeddedJobResponse(job) -> dict:
    return {
        "id": str(job["_id"]),
        "job_name": job["job_name"],
        "company_name": job["company_name"],
        "job_full_text": job["job_full_text"]
    }


def jobListEntity(jobs) -> list:
    return [embeddedJobResponse(job) for job in jobs]
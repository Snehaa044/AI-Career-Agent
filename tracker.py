applications = []

def add_application(role, company, status):
    applications.append({
        "role": role,
        "company": company,
        "status": status
    })
    return "Application added!"

def list_applications():
    return applications

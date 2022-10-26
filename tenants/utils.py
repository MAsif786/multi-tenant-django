
from email.policy import default


def tenant_db_from_request(request):
    host = request.META['HTTP_HOST']
    if '.' in host:
        domain = host.split('.')[0]
    else:
        domain = "default"
    
    tenant = domain
    print("Request Tenant",tenant)
    return tenant
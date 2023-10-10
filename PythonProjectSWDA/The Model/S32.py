from codeable_models import CClass, add_links
from metamodels.GT_metamodel import source
from models.E4M_ADD_models import *

source_S32 = CClass(source, "S32", values={
    "title": "COMMON CLOUD THREATS: CREDENTIAL THEFT",
    "url": "https://www.crowdstrike.com/cybersecurity-101/cloud-security/credential-theft/",
    "archive url": "https://web.archive.org/web/20230610040043/https://www.crowdstrike.com/cybersecurity-101/cloud-security/credential-theft/",
    "source type": "Blog Post",
    "author type": "David Puzas",
    "date": "January 12, 2023",
    "problem": [
        "Malware",
        "Weak passwords or password reuse",
        "Man-in-the-middle (MitM) attacks"
    ],
    "solution": {
        "Problem 1": "Enable and require multifactor authentication (MFA), OTP, 2FA",
        "Problem 2": "Maintain good password hygiene",
        "Problem 3": "Properly scope permissions across users and machines"
    },
    "decision driver": "",
    "references": "https://www.crowdstrike.com/cybersecurity-101/cloud-security/credential-theft/",
    "remarks": "N/A"
})

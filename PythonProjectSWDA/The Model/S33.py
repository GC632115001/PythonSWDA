from codeable_models import CClass, add_links
from metamodels.GT_metamodel import source
from models.E4M_ADD_models import *

source_S33 = CClass(source, "S33", values={
    "title": "Vulnerabilities in password-based login",
    "url": "https://portswigger.net/web-security/authentication/password-based",
    "archive url": "https://web.archive.org/web/20230521093349/https://portswigger.net/web-security/authentication/password-based",
    "source type": "Blog Post",
    "author type": "portswigger",
    "date": "-",
    "problem": [
        "Brute-force attacks"
    ],
    "solution": {
        "Problem 1": "Locking the account that the remote user is trying to access if they make too many failed login attempts. Blocking the remote user's IP address if they make too many login attempts in quick succession"
    },
    "decision driver": "",
    "references": "https://portswigger.net/web-security/authentication/password-based",
    "remarks": "N/A"
})

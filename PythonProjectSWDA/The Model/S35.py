from codeable_models import CClass, add_links
from metamodels.GT_metamodel import source
from models.E4M_ADD_models import *

source_S35 = CClass(source, "S35", values={
    "title": "Secure Communication Principles & Tips By Salt Communications",
    "url": "https://saltcommunications.com/press-releases/secure-communication-principles-tips-by-salt-communications/",
    "archive url": "https://web.archive.org/web/20230321132543/https://saltcommunications.com/press-releases/secure-communication-principles-tips-by-salt-communications/",
    "source type": "Blog Post",
    "author type": "Nicole Allen",
    "date": "August 15, 2022",
    "problem": [
        "Salt Communications",
        "Wire"
    ],
    "solution": {
        "Problem 1": "Employee Training",
        "Problem 2": "Secure Communication Tools"
    },
    "decision driver": "",
    "references": "https://saltcommunications.com/press-releases/secure-communication-principles-tips-by-salt-communications/",
    "remarks": "N/A"
})

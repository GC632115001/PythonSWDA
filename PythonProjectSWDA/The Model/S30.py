from codeable_models import CClass, add_links
from metamodels.GT_metamodel import source
from models.E4M_ADD_models import *

source_S30 = CClass(source, "S30", values={
    "title": "Passwords technical overview",
    "url": "https://learn.microsoft.com/en-us/windows-server/security/kerberos/passwords-technical-overview",
    "archive url": "https://tinyurl.com/3fkw2rjs",
    "source type": "Article",
    "author type": "N/A",
    "date": "NOVEMBER 14, 2022",
    "problem": [
        "A system has a weak password policy."
    ],
    "solution": {
        "Problem": "Using a strong passwords that difficult to crack, ex. At least seven characters long, Contains \"secret\" or random information, Is significantly different from previous passwords, Uppercase letters, Lowercase letters, Numerals, and Symbols including spaces."
    },
    "decision driver": "approachability, prioritization, stakeholders",
    "references": "N/A",
    "remarks": "N/A"
})

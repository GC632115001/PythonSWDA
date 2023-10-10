from codeable_models import CClass, add_links
from metamodels.GT_metamodel import source
from models.E4M_ADD_models import *

source_S02 = CClass(source, "S02", values={
    "title": "10 cyber security risks in software development and how to mitigate them",
    "url": "https://devtalents.com/cyber-security-during-software-development/",
    "archive url": "https://web.archive.org/web/20230703032931/https://devtalents.com/cyber-security-during-software-development/",
    "source type": "Blog post",
    "author type": "Olga Trąd",
    "date": "02/10/2023",
    "problem": [
        "Data breaches",
        "Insecure APIs",
        "Poor password policies",
        "Unauthorized access",
        "Malware"
    ],
    "solution": {
        "Problem 1.": "Use secure coding practices",
        "Problem 2.": "Encrypt sensitive data",
        "Problem 3.": "Use security testing",
        "Problem 4.": "Train employees on cyber security best practices",
        "Problem 5.": "Monitor systems for cyber threats"
    },
    "decision driver": "team cohesion, code language",
    "references": ["https://devtalents.com/cyber-security-during-software-development/"],
    "remarks": "N/A"
})
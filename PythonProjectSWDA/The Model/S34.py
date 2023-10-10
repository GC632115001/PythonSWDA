from codeable_models import CClass, add_links
from metamodels.GT_metamodel import source
from models.E4M_ADD_models import *

source_S34 = CClass(source, "S34", values={
    "title": "Common password vulnerabilities and how to avoid them",
    "url": "https://www.acunetix.com/blog/web-security-zone/common-password-vulnerabilities/",
    "archive url": "https://web.archive.org/web/20230528085912/https://www.acunetix.com/blog/web-security-zone/common-password-vulnerabilities/",
    "source type": "Blog Post",
    "author type": "Tomasz Andrzej Nidecki",
    "date": "March 21, 2022",
    "problem": [
        "Length or complexity?",
        "The danger of password reuse"
    ],
    "solution": {
        "Problem 1": "Avoid Common Patterns",
        "Problem 2": "Weakened Security Measures"
    },
    "decision driver": "",
    "references": "https://www.acunetix.com/blog/web-security-zone/common-password-vulnerabilities/",
    "remarks": "N/A"
})

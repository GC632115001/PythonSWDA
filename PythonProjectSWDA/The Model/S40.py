from codeable_models import CClass, add_links
from metamodels.GT_metamodel import source
from models.E4M_ADD_models import *

source_S40 = CClass(source, "S40", values={
    "title": "10 cyber security risks in software development and how to mitigate them",
    "url": "https://devtalents.com/cyber-security-during-software-development/",
    "archive url": "https://web.archive.org/web/*/https://devtalents.com/cyber-security-during-software-development/*",
    "source type": "Blog Post",
    "author type": "Olga Trąd",
    "date": "2 October 2023",
    "problem": [
        "Data breaches",
        "Insecure APIs",
        "Insufficient logging",
        "Cross-site scripting (XSS)",
        "Malware",
        "Unpatched vulnerabilities"
    ],
    "solution": {
        "Problem 1": "Use secure coding practices",
        "Problem 2": "Implement multi-factor authentication",
        "Problem 3": "Use security testing",
        "Problem 4": "Monitor systems for cyber threats",
        "Problem 5": "Encrypt sensitive data",
        "Problem 6": "Train employees on cyber security best practices"
    },
    "decision driver": "approachability, chosen tools",
    "references": "N/A",
    "remarks": "N/A"
})

from codeable_models import CClass, add_links
from metamodels.GT_metamodel import source
from models.E4M_ADD_models import *

source_S11 = CClass(source, "S11", values={
    "title": "Common types of security vulnerabilities & ways to fix them",
    "url": "https://itrexgroup.com/blog/security-vulnerability-types-and-ways-to-fix-them/#",
    "archive url": "https://tinyurl.com/4vb4pvak",
    "source type": "Article",
    "author type": "Innovation Analyst",
    "date": "6 July 2022",
    "problem": [
        "Lack of strong encryption practices",
        "Sensitive data exposure",
        "Insufficient transport layer protection"
    ],
    "solution": {
        "Problem 1.": "Plan better protection like encrypting data on USB sticks, laptops, and desktops.",
        "Problem 2.": "Better training.",
        "Problem 3.": "Secure the data transportation"
    },
    "decision driver": "Negligent",
    "references": ["N/A"],
    "remarks": "N/A"
})
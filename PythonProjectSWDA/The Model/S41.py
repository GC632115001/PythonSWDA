from codeable_models import CClass, add_links
from metamodels.GT_metamodel import source
from models.E4M_ADD_models import *

source_S41 = CClass(source, "S41", values={
    "title": "SOFTWARE SECURITY: DEFINITIONS AND GUIDANCE",
    "url": "https://www.crowdstrike.com/cybersecurity-101/security-it-operations/software-security/",
    "archive url": "https://web.archive.org/web/*/https://www.crowdstrike.com/cybersecurity-101/security-it-operations/software-security/*",
    "source type": "Blog Post",
    "author type": "N/A",
    "date": "26 October 2022",
    "problem": [
        "Malicious attacks"
    ],
    "solution": {
        "Problem 1": "Use Software Security Tools",
        "Problem 2": "Ensuring and Improving Software Security"
    },
    "decision driver": "approachability, chosen tools",
    "references": "N/A",
    "remarks": "N/A"
})

from codeable_models import CClass, add_links
from metamodels.GT_metamodel import source
from models.E4M_ADD_models import *

source_S39 = CClass(source, "S39", values={
    "title": "4 Common Software Security Development Issues & How to Fix Them",
    "url": "https://devm.io/security/security-dev-issues-174540",
    "archive url": "https://web.archive.org/web/*/https://devm.io/security/security-dev-issues-174540*",
    "source type": "Blog Post",
    "author type": "Tim Jarrett",
    "date": "2 July 2021",
    "problem": [
        "Slow remediation time for vulnerabilities",
        "Flaws pose the greatest risk to your applications",
        "Some insecure open source libraries in applications are transitive.",
        "Error from software language you prefer"
    ],
    "solution": {
        "Problem 1": "Implement automated scanning and testing.",
        "Problem 2": "Address these common flaws.",
        "Problem 3": "Integrating a scanning tool like Software Composition Analysis (SCA).",
        "Problem 4": "Surplus of high and very high severity flaws in code."
    },
    "decision driver": "code language, approachability, chosen tools, team decision",
    "references": "N/A",
    "remarks": "N/A"
})

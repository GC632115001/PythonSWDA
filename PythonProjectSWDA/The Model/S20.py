from codeable_models import CClass, add_links
from metamodels.GT_metamodel import source
from models.E4M_ADD_models import *

source_S20 = CClass(source, "S20", values={
    "title": "5 Key Open Source Security Risks and How to Prevent Them",
    "url": "https://blog.sonatype.com/5-key-open-source-security-risks-and-how-to-prevent-them",
    "archive url": "https://tinyurl.com/2pm69bkn",
    "source type": "Blog Post",
    "author type": "Luke Mcbride",
    "date": "December 01, 2022",
    "problem": [
        "Lack of Security Expertise",
        "Managing Code"
    ],
    "solution": {
        "Problem 1.": "Shift Left and Adopt DevSecOps",
        "Problem 2.": "Maintain an OSS Security Library Inventory"
    },
    "decision driver": "Code language, prioritization, team cohesion (decision making), time-consuming.",
    "references": [
        "https://learn.sonatype.com/guides-old/devsecops/",
        "https://www.sonatype.com/state-of-the-software-supply-chain/project-quality-metrics"
    ],
    "remarks": "N/A"
})

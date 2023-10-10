from codeable_models import CClass, add_links
from metamodels.GT_metamodel import source
from models.E4M_ADD_models import *

source_S06 = CClass(source, "S06", values={
    "title": "Common Software Vulnerabilities in 2022 and Ways to Prevent Them",
    "url": "https://codesigningstore.com/common-software-vulnerabilities",
    "archive url": "https://web.archive.org/web/20230703033943/https://www.legitsecurity.com/blog/10-agile-software-development-security-concerns-you-need-to-know",
    "source type": "Blog post",
    "author type": "N/A",
    "date": "2022",
    "problem": [
        "Exposure of sensitive data",
        "Flaws in Injection",
        "Buffer overflow",
        "Broken access control"
    ],
    "solution": {
        "Problem 1.": "Personal or sensitive data has to be protected with encryption",
        "Problem 2.": "Test Your Software",
        "Problem 3.": "Use programming languages that have automatic protection against buffer overflow attacks",
        "Problem 4.": "Restricted users to only necessary areas"
    },
    "decision driver": "code language, stakeholders, implementation technology",
    "references": ["https://codesigningstore.com/common-software-vulnerabilities"],
    "remarks": "N/A"
})

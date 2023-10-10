from codeable_models import CClass, add_links
from metamodels.GT_metamodel import source
from models.E4M_ADD_models import *

source_S10 = CClass(source, "S10", values={
    "title": "3 security risks that architecture analysis can resolve",
    "url": "https://www.synopsys.com/blogs/software-security/security-risks-that-architecture-analysis-can-resolve/",
    "archive url": "https://tinyurl.com/bdcuw9hj",
    "source type": "Article",
    "author type": "Team of writer",
    "date": "25 Jan 2016",
    "problem": [
        "Point-of-sale (POS) intrusions",
        "Insider threats and privilege misuse",
        "Web app attacks"
    ],
    "solution": {
        "Problem 1 2 3.": "Architecture analysis assessments"
    },
    "decision driver": "Lack of security controls, inadequate system design",
    "references": ["N/A"],
    "remarks": "N/A"
})


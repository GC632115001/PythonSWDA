from codeable_models import CClass, add_links
from metamodels.GT_metamodel import source
from models.E4M_ADD_models import *

source_S38 = CClass(source, "S38", values={
    "title": "Engineering Solutions to Security Issues",
    "url": "https://thenewstack.io/engineering-solutions-to-security-issues/",
    "archive url": "https://web.archive.org/web/*/https://thenewstack.io/engineering-solutions-to-security-issues/*",
    "source type": "Blog Post",
    "author type": "Ron Powell",
    "date": "24 May 2021",
    "problem": [
        "Need software delivery pipelines based on continuous integration and continuous delivery (CI/CD)"
    ],
    "solution": {
        "Problem 1": "Use static analytical methods to design and test components.",
        "Problem 2": "Complement static code analysis with static secure code review."
    },
    "decision driver": "chosen tools, team decision",
    "references": "N/A",
    "remarks": "N/A"
})

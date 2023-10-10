from codeable_models import CClass, add_links
from metamodels.GT_metamodel import source
from models.E4M_ADD_models import *

source_S42 = CClass(source, "S42", values={
    "title": "Top Risks In Software Development Life Cycle: 7-Minute Read",
    "url": "https://cystack.net/blog/security-risks-in-software-development-life-cycle",
    "archive url": "https://web.archive.org/web/20230701000000*/https://cystack.net/blog/security-risks-in-software-development-life-cycle",
    "source type": "Blog Post",
    "author type": "Jenny Duong",
    "date": "5 April 2023",
    "problem": [
        "There might be no specific framework for risk management stated during the planning.",
        "External security risks",
        "Forget architecture design adaptive to possible environmental changes",
        "The code might be exposed",
        "Cannot replicate the security problems"
    ],
    "solution": {
        "Problem 1": "Building risk management strategies to handle risks in SDLC",
        "Problem 2": "Running automatic test cases to detect difficult risks",
        "Problem 3": "Educating the development team on security SDLC",
        "Problem 4": "Eliciting requirements carefully, including security requirements",
        "Problem 5": "Building secure coding checklists and doing code reviews"
    },
    "decision driver": "chosen tools, prioritization, team decision.",
    "references": "N/A",
    "remarks": "N/A"
})

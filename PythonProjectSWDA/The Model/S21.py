from codeable_models import CClass, add_links
from metamodels.GT_metamodel import source
from models.E4M_ADD_models import *

source_S21 = CClass(source, "S21", values={
    "title": "7 reasons why development teams skip security steps",
    "url": "https://www.invicti.com/blog/web-security/7-reasons-why-development-teams-skip-security-steps/",
    "archive url": "https://tinyurl.com/ymdv53xb",
    "source type": "Blog Post",
    "author type": "Tomasz Andrzej Nidecki",
    "date": "Thu, 26 Jan 2023",
    "problem": [
        "Frustrations due to inadequate tooling",
        "Effective application security starts at the top",
        "Insufficient education in application security"
    ],
    "solution": {
        "Problem 1.": "Avoid depending on SAST tools, as it's vulnerable to triggering several false warnings.",
        "Problem 2.": "Selecting a suitable security platform and integrating it into your software development lifecycle will help to alleviate many of the issues.",
        "Problem 3.": "Take the time to learn about security."
    },
    "decision driver": "Approachability, chosen tools, prioritization.",
    "references": [
        "https://www.invicti.com/learn/static-application-security-testing-sast/"
    ],
    "remarks": "N/A"
})

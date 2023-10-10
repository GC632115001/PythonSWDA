from codeable_models import CClass, add_links
from metamodels.GT_metamodel import source
from models.E4M_ADD_models import *

source_S22 = CClass(source, "S22", values={
    "title": "5 ways to enable secure software development in 2023",
    "url": "https://techtarget.com/searchsecurity/opinion/Ways-to-enable-secure-software-development-in-2023",
    "archive url": "https://tinyurl.com/ayuf64pj",
    "source type": "Blog Post",
    "author type": "Melinda Marks",
    "date": "January 2023",
    "problem": [
        "Supply Chain Security Management Software Isn't Good Enough",
        "Managing API security"
    ],
    "solution": {
        "Problem 1.": "Take the time to learn about security and train staff.",
        "Problem 2.": "Reduce misconfigurations and monitor for security issues."
    },
    "decision driver": "Chosen tools, time-consuming.",
    "references": [
        "https://www.techtarget.com/searchsecurity/tip/Top-4-source-code-security-best-practices",
        "https://www.techtarget.com/searchapparchitecture/tip/10-API-security-guidelines-and-best-practices"
    ],
    "remarks": "N/A"
})
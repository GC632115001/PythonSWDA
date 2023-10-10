from codeable_models import CClass, add_links
from metamodels.GT_metamodel import source
from models.E4M_ADD_models import *

source_S04 = CClass(source, "S04", values={
    "title": "Application Security 101",
    "url": "https://www.trendmicro.com/vinfo/us/security/news/virtualization-and-cloud/application-security-101",
    "archive url": "https://web.archive.org/web/20230703033943/https://www.legitsecurity.com/blog/10-agile-software-development-security-concerns-you-need-to-know",
    "source type": "Blog post",
    "author type": "N/A",
    "date": "July 27, 2020",
    "problem": [
        "Weak backend access controls",
        "Security misconfiguration",
        "Broken authentication and authorization",
        "Insufficient logging and monitoring",
        "Using components with known vulnerabilities"
    ],
    "solution": {
        "Problem 1.": "Scan for vulnerabilities regularly",
        "Problem 2.": "Include application security in data privacy compliance strategy",
        "Problem 3.": "Adopt automated testing",
        "Problem 4.": "Implement Principle of Least Privilege",
        "Problem 5.": "Scan for vulnerabilities regularly"
    },
    "decision driver": "team cohesion, code language, stakeholders",
    "references": ["https://www.trendmicro.com/vinfo/us/security/news/virtualization-and-cloud/application-security-101"],
    "remarks": "N/A"
})
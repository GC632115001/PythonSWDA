from codeable_models import CClass, add_links
from metamodels.GT_metamodel import source
from models.E4M_ADD_models import *

source_S24 = CClass(source, "S24", values={
    "title": "10 Common Web Security Vulnerabilities",
    "url": "https://www.toptal.com/cyber-security/10-most-common-web-security-vulnerabilities",
    "archive url": "https://tinyurl.com/bdh9taef",
    "source type": "Blog Post",
    "author type": "Gergely Kalman",
    "date": "April 4, 2016",
    "problem": [
        "Missing Function Level Access Control",
        "Broken Authentication",
        "Cross-Site Request Forgery (CSRF)"
    ],
    "solution": {
        "Problem 1.": "Restrict access and use a password once saved.",
        "Problem 2.": "Implementing a framework will help you avoid the web security risks caused by faulty authentication.",
        "Problem 3.": "Add a secret token in a form field that is hidden and inaccessible to software."
    },
    "decision driver": "Approachability",
    "references": [
        "https://en.wikipedia.org/wiki/Confused_deputy_problem"
    ],
    "remarks": "N/A"
})
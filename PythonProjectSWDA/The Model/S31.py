from codeable_models import CClass, add_links
from metamodels.GT_metamodel import source
from models.E4M_ADD_models import *

source_S31 = CClass(source, "S31", values={
    "title": "4 Common Security Issues Found In Password-Based Login",
    "url": "https://www.loginradius.com/blog/identity/common-vulnerabilities-password-based-login/",
    "archive url": "https://web.archive.org/web/20220701072922/https://www.loginradius.com/blog/identity/common-vulnerabilities-password-based-login/",
    "source type": "Blog Post",
    "author type": "Srishti Singh",
    "date": "-",
    "problem": [
        "Your personal and valuable data is at risk.",
        "Hackers spread malware to cause disruptions in a network.",
        "Hackers hijack targeted systems for malicious activities.",
        "Such attacks can ruin your company’s reputation."
    ],
    "solution": {
        "Problem 1": "Use longer passwords with varied character types.",
        "Problem 2": "Change your passwords frequently.",
        "Problem 3": "Use different usernames for every site.",
        "Problem 4": "Use a password manager to track your online login info automatically."
    },
    "decision driver": "",
    "references": "https://www.loginradius.com/blog/identity/common-vulnerabilities-password-based-login/",
    "remarks": "N/A"
})

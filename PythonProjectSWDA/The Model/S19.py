from codeable_models import CClass, add_links
from metamodels.GT_metamodel import source
from models.E4M_ADD_models import *

source_S19 = CClass(source, "S19", values={
    "title": "10 BEST PRACTICES FOR SOFTWARE DEVELOPMENT SECURITY",
    "url": "https://www.orientsoftware.com/blog/software-development-security/",
    "archive url": "https://tinyurl.com/yb9shzzy",
    "source type": "Blog Post",
    "author type": "Øyvind Forsbak",
    "date": "Nov 29, 2021",
    "problem": [
        "SQL Injection",
        "Encryption Weakness",
        "Password Hashing",
        "Insufficient Logging & Monitoring"
    ],
    "solution": {
        "Problem 1.": "Using parameterized queries instead of dynamic SQL statements.",
        "Problem 2.": "All data should be encrypted in transit and at rest. This includes database storage, file storage, sessions, cookies, etc.",
        "Problem 3.": "Use a password hashing technique to generate a unique hash of the user's password that could be saved in the database.",
        "Problem 4.": "Implement monitoring and auditing practices such as user activity tracking, file integrity monitoring, and network activity logs."
    },
    "decision driver": "Code language, approachability, chosen tools.",
    "references": [
        "https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-data-at-rest-encryption/policy.html",
        "https://crashtest-security.com/insufficient-logging-monitoring-guide/",
        "https://owasp.org/www-community/attacks/SQL_Injection"
    ],
    "remarks": "N/A"
})

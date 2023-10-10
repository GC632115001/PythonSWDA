from codeable_models import CClass, add_links
from metamodels.GT_metamodel import source
from models.E4M_ADD_models import *

source_S36 = CClass(source, "S36", values={
    "title": "SQL Injection Attacks (SQLi)",
    "url": "https://www.rapid7.com/fundamentals/sql-injection-attacks/",
    "archive url": "https://web.archive.org/web/20230330192614/https://www.rapid7.com/fundamentals/sql-injection-attacks/",
    "source type": "Blog Post",
    "author type": "Rapid7",
    "date": "2022",
    "problem": [
        "Unsanitized Input",
        "Blind SQL Injection",
        "Out-of-Band Injection"
    ],
    "solution": {
        "Problem 1": "Avoid placing user-provided input directly into SQL statements",
        "Problem 2": "Don’t use dynamic SQL",
        "Problem 3": "Use a Web Application Firewall (WAF) for web applications that access databases"
    },
    "decision driver": "",
    "references": "https://www.rapid7.com/fundamentals/sql-injection-attacks/",
    "remarks": "N/A"
})

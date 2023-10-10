from codeable_models import CClass, add_links
from metamodels.GT_metamodel import source
from models.E4M_ADD_models import *

source_S25 = CClass(source, "S25", values={
    "title": "Hypertext Transfer Protocol Secure (HTTPS)",
    "url": "https://www.techtarget.com/searchsoftwarequality/definition/HTTPS",
    "archive url": "https://tinyurl.com/48ejwvze",
    "source type": "Blog Post",
    "author type": "Contributing writer (Rahul Awati)",
    "date": "MARCH 23, 2022",
    "problem": [
        "The current website is HTTP, which is vulnerable to attacks."
    ],
    "solution": {
        "Problem": "Change to HTTPS, That provides protection against these vulnerabilities by encrypting all exchanges between a web browser and web server. As a result, HTTPS ensures that no one can tamper with these transactions, thus securing users' privacy and preventing sensitive information from falling into the wrong hands."
    },
    "decision driver": "Code language, approachability, chosen tools, prioritization",
    "references": "N/A",
    "remarks": "N/A"
})

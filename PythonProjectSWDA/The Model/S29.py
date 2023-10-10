from codeable_models import CClass, add_links
from metamodels.GT_metamodel import source
from models.E4M_ADD_models import *

source_S29 = CClass(source, "S29", values={
    "title": "How the latest SQL injection attacks threaten web application firewalls",
    "url": "https://www.scmagazine.com/resource/data-security/how-the-latest-sql-injection-attacks-threaten-web-application-firewalls",
    "archive url": "https://tinyurl.com/bdeztzmw",
    "source type": "Blog Post",
    "author type": "Paul Wagenseil",
    "date": "FEBRUARY 21, 2023",
    "problem": [
        "SQL injection attack"
    ],
    "solution": {
        "Problem": "Using a web application firewall (WAF). While regular network firewalls are put up client-side by organizations to defend users and devices, WAFs are implemented server-side to protect websites and web applications. Barracuda Networks, Cloudflare and F5 are among the best-known providers of commercial WAFs, and there are also free open-source alternatives such as ModSecurity."
    },
    "decision driver": "code language, approachability, chosen tools, prioritization",
    "references": "N/A",
    "remarks": "N/A"
})
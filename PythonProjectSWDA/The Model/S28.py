from codeable_models import CClass, add_links
from metamodels.GT_metamodel import source
from models.E4M_ADD_models import *

source_S28 = CClass(source, "S28", values={
    "title": "Session Management",
    "url": "https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html",
    "archive url": "https://tinyurl.com/nn8f5e3n",
    "source type": "Sheet",
    "author type": "OWASP",
    "date": "JULY 16, 2019",
    "problem": [
        "Sessions are not properly managed, leading to security vulnerabilities and potential unauthorized access to user accounts."
    ],
    "solution": {
        "Problem": "Web development frameworks, such as J2EE, ASP .NET, PHP, and others, provide their own session management features and associated implementation. It is recommended to use these built-in frameworks versus building a homemade one from scratch, as they are used worldwide on multiple web environments and have been tested by the web application security and development communities over time."
    },
    "decision driver": "code language, chosen tools, team cohesion (decision making)",
    "references": "N/A",
    "remarks": "N/A"
})
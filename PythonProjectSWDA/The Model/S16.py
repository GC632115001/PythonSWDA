from codeable_models import CClass, add_links
from metamodels.GT_metamodel import source
from models.E4M_ADD_models import *

source_S16 = CClass(source, "S16", values={
    "title": "Not having a security architecture",
    "url": "https://www.kambda.com/main-software-architecture-issues-and-challenges/",
    "archive url": "/web/20230702180659/https://www.networkworld.com/article/2305984/not-having-a-security-architecture.html",
    "source type": "Blog Post",
    "author type": "Technology Blogger",
    "date": "28 Aug 2006",
    "problem": [
        "Lack of comprehensive architectural framework for IT security.",
        "Insufficient hardware and software security measures.",
        "Inadequate protection of physical assets and network traffic.",
        "Fragmented tools and one-off solutions."
    ],
    "solution": {
        "Problem 1.": "Develop an overall security architecture blueprint to optimize resource placement and support business functions.",
        "Problem 2.": "Implement robust security measures, such as firewalls and encryption.",
        "Problem 3.": "Implement physical security measures, encryption, and secure protocols to protect assets and network traffic.",
        "Problem 4.": "Adopt a comprehensive security architecture approach for enterprise risk management, avoiding disconnected tools."
    },
    "decision driver": "Chosen tools, team cohesion (decision making), stakeholders, implementation methodology or technique.",
    "references": ["Minoli, D. (2006, August 28). Not having a security architecture. Network World. Retrieved from https://www.networkworld.com/article/2305984/not-having-a-security-architecture.html"],
    "remarks": "N/A"
})

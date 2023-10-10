from codeable_models import CClass, add_links
from metamodels.GT_metamodel import source
from models.E4M_ADD_models import *

source_S17 = CClass(source, "S17", values={
    "title": "Security Risks in the Software Development Lifecycle",
    "url": "https://www.researchgate.net/publication/369538781_Security_Risks_in_the_Software_Development_Lifecycle_A_Review",
    "archive url": "/web/20230702182257/https://www.researchgate.net/publication/369538781_Security_Risks_in_the_Software_Development_Lifecycle_A_Review",
    "source type": "Technical Report",
    "author type": "Researcher",
    "date": "23 Feb 2023",
    "problem": [
        "Lack of priority and resources for security.",
        "Neglect of security and performance verification.",
        "Lack of interest in adopting software security practices.",
        "Delayed consideration of security issues.",
        "Agile methods neglecting security."
    ],
    "solution": {
        "Problem 1.": "Prioritize security and recognize it as an essential aspect of software development.",
        "Problem 2.": "Include thorough verification processes in project timelines.",
        "Problem 3.": "Organizations should foster a culture that emphasizes the importance of software security.",
        "Problem 4.": "Integrate security from the beginning of the development process.",
        "Problem 5.": "Incorporate security practices and requirements into Agile processes."
    },
    "decision driver": "Prioritization, team decision-making, stakeholders, knowledge and experience.",
    "references": [
        "Bishop D,Rowland P.Agile and secure software development: an unfinishedstory. Issues in Information Systems. 2019 Jan 1, 20(1).",
        "Rygge H,Jøsang A.Threat poker: solving security and privacy threats in agile software development. In Secure IT Systems: 23rd Nordic Conference, NordSec 2018, Oslo, Norway, November 28-30, 2018, Proceedings 23 2018 (pp. 468-483). Springer International Publishing."
    ],
    "remarks": "N/A"
})

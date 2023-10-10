from codeable_models import CClass, add_links
from metamodels.GT_metamodel import source
from models.E4M_ADD_models import *

source_S18 = CClass(source, "S18", values={
    "title": "Secure Software Architecture and Design",
    "url": "http://archive.nitjsr.ac.in/course_assignment/CA02CA4203%20Lect%2024-30Secure%20Software%20Architecture%20and%20Design.pdf",
    "archive url": "https://tinyurl.com/zfhsykpb",
    "source type": "Research paper",
    "author type": "Researcher",
    "date": "N/A",
    "problem": [
        "Lack of secure authentication mechanisms.",
        "Vulnerabilities due to coding bugs.",
        "Insufficient protection against session hijacking.",
        "Lack of defense in depth"
    ],
    "solution": {
        "Problem 1.": "Implement strong authentication methods such as multi-factor authentication (MFA) to reduce the risk of unauthorized access.",
        "Problem 2.": "Conduct testing to identify and address coding bugs. Implement secure coding practices and perform regular code reviews to minimize the introduction of vulnerabilities.",
        "Problem 3.": "Implement session management mechanisms, such as setting expiration time for sessions after a period of inactivity.",
        "Problem 4.": "Implement multiple layers of security defenses to reduce the likelihood of a successful attack."
    },
    "decision driver": "Code language, Implementation methodology, team decision-making, time-consuming.",
    "references": ["National Institute of Technology Jamshedpur. (n.d.). Secure Software Architecture and Design. Retrieved from http://archive.nitjsr.ac.in/course_assignment/CA02CA4203%20Lect%2024-30Secure%20Software%20Architecture%20and%20Design.pdf"],
    "remarks": "The public date of publication is not mentioned."
})
from codeable_models import CClass, add_links
from metamodels.GT_metamodel import source
from models.E4M_ADD_models import *

source_S15 = CClass(source, "S15", values={
    "title": "A Catalog of Security Architecture Weaknesses",
    "url": "https://s2e-lab.github.io/preprints/icsaw17-preprint.pdf",
    "archive url": "/web/20230702174324/https://s2e-lab.github.io/preprints/icsaw17-preprint.pdf",
    "source type": "Conference Paper",
    "author type": "Researcher",
    "date": "26 June 2017",
    "problem": [
        "Session Hijacking Attack",
        "Session Fixation Attack"
    ],
    "solution": {
        "Problem 1.": "Encrypt session data, use strong and unpredictable session IDs, regularly regenerate session IDs, securely store session files, set session timeouts, implement strong user authentication, and keep software updated.",
        "Problem 2.": "The validation of session IDs should not only include checking the format and length but also verify the existence of the ID."
    },
    "decision driver": "Code language, implementation methodology, frameworks and libraries, team decision-making.",
    "references": [
        "I. C. for Secure Design. Avoiding the top 10 software security design flaws. http://cybersecurity.ieee.org/center-for-secure-design/, 2015. (Accessed on 10/06/2016).",
        "G. Pedraza-Garcia, H. Astudillo, and D. Correal. A methodological approach to apply security tactics in software architecture design. In Communications and Computing (COLCOM), 2014 IEEE Colombian Conference on, pages 1–8. IEEE, 2014."
    ],
    "remarks": "N/A"
})

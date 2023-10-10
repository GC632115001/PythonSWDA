from codeable_models import CClass, add_links
from metamodels.GT_metamodel import source
from models.E4M_ADD_models import *

source_S08 = CClass(source, "S08", values={
    "title": "4 core software security problems—and what to do about them",
    "url": "https://techbeacon.com/security/4-core-software-security-problems-what-do-about-them",
    "archive url": "https://tinyurl.com/vunyhky6",
    "source type": "Article",
    "author type": "VP of Security, Indeed",
    "date": "N/A",
    "problem": [
        "Vague requirements",
        "Fault is irrelevant",
        "Misaligned management",
        "Collaboration between each member of the company"
    ],
    "solution": {
        "Problem 1.": "Introduce specific requirements focused on incremental steps to improving security",
        "Problem 2.": "Security teams should focus on vulnerabilities by evaluating their scope, managing the risks they present, and configuring tools as needed to recognize the problem. In turn, developers should focus on fixing the problem that led to the vulnerability, and leadership needs to hold both groups equally accountable for their roles in security.",
        "Problem 3.": "Executives, directors, and managers need to align their individual verticals and teams by prioritizing the same security goals.",
        "Problem 4.": "Better collaboration and cautious coding from all parties involved."
    },
    "decision driver": "Company structure for only speed and profit",
    "references": ["N/A"],
    "remarks": "N/A"
})

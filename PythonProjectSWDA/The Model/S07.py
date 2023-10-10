from codeable_models import CClass, add_links
from metamodels.GT_metamodel import source
from models.E4M_ADD_models import *

source_S07 = CClass(source, "S07", values={
    "title": "What are the Challenges in Establishing Cyber Security?",
    "url": "https://www.tutorialspoint.com/what-are-the-challenges-in-establishing-cyber-security",
    "archive url": "https://tinyurl.com/yfbc2bzc",
    "source type": "Article",
    "author type": "Instructor",
    "date": "30 May 2022",
    "problem": [
        "Ransomware Attacks",
        "Lack of Skills and Trained Workforce"
    ],
    "solution": {
        "Problem 1.": "Prioritize cybersecurity more in budgeting",
        "Problem 2.": "Train more employees with better quality rather than relying on hiring one"
    },
    "decision driver": "workforce crisis, increasingly complex cyberattacks",
    "references": ["N/A"],
    "remarks": "N/A"
})

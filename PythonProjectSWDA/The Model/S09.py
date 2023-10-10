from codeable_models import CClass, add_links
from metamodels.GT_metamodel import source
from models.E4M_ADD_models import *

source_S09 = CClass(source, "S09", values={
    "title": "Most Extensive Cyber Security Challenges & Solutions in 2023",
    "url": "https://www.knowledgehut.com/blog/security/cyber-security-challenges",
    "archive url": "https://tinyurl.com/973fxzbb",
    "source type": "Article",
    "author type": "Blog Author",
    "date": "19 Jun 2023",
    "problem": [
        "Adapting To A Remote Workforce",
        "Blockchain And Cryptocurrency Attack",
        "Phishing And Spear-Phishing Attacks"
    ],
    "solution": {
        "Problem 1.": "Implement cloud-based cybersecurity solutions that protect the user's identity, device, and the cloud",
        "Problem 2.": "Blockchain-powered cybersecurity controls and standards to defend enterprises against cyberattacks.",
        "Problem 3.": "Use anti-phishing tools such as Antivirus software and Anti-phishing Toolbar, sandbox the E-mail attachments, and train the employees."
    },
    "decision driver": "Lack of updates regarding security",
    "references": ["N/A"],
    "remarks": "N/A"
})


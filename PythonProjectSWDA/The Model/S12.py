from codeable_models import CClass, add_links
from metamodels.GT_metamodel import source
from models.E4M_ADD_models import *

source_S12 = CClass(source, "S12", values={
    "title": "Best Practices For Secure Software Development",
    "url": "Common types of security vulnerabilities & ways to fix them",
    "archive url": "https://tinyurl.com/4vzcy6rv",
    "source type": "Article",
    "author type": "Senior Solution Architect",
    "date": "31 March 2023",
    "problem": [
        "Vulnerabilities in third-party libraries and frameworks",
        "Insufficient logging and monitoring",
        "Cross-site scripting (XSS)"
    ],
    "solution": {
        "Problem 1.": "Code review involves reviewing the code written by developers to identify potential security issues",
        "Problem 2.": "Continuous monitoring helps in detecting and responding to security incidents in real-time",
        "Problem 3.": "Developers must adhere to secure coding practices"
    },
    "decision driver": "Secure Software Isn’t a Big Enough Priority, Quality Doesn’t Necessarily Guarantee Security, Not Enough Training for Security",
    "references": ["N/A"],
    "remarks": "N/A"
})
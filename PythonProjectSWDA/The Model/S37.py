from codeable_models import CClass, add_links
from metamodels.GT_metamodel import source
from models.E4M_ADD_models import *

source_S37 = CClass(source, "S37", values={
    "title": "How to deal with security challenges in software development",
    "url": "https://blog.convisoappsec.com/en/developers-how-to-deal-with-some-of-the-biggest-security-challenges-during-software-development/",
    "archive url": "https://web.archive.org/web/*/https://blog.convisoappsec.com/en/developers-how-to-deal-with-some-of-the-biggest-security-challenges-during-software-development/*",
    "source type": "Blog Post",
    "author type": "Gabriel Galdino",
    "date": "6 April 2022",
    "problem": [
        "Identify vulnerabilities in code which can affect the security.",
        "Recognize vulnerabilities in third-party components and dependencies.",
        "The risks of using open source components.",
        "Hard to capture the data change used beyond data security.",
        "Need secure software development for Application.",
        "Have ineffective Software Development Life Cycle.",
        "Need to improve your safety culture."
    ],
    "solution": {
        "Problem 1": "Verify that the code is efficient, scalable and secure.",
        "Problem 2": "Use the services that focus on checking codebase dependencies.",
        "Problem 3": "Realize the risks of using open source components.",
        "Problem 4": "Use DataOps.",
        "Problem 5": "Use AppSec.",
        "Problem 6": "Do threat modeling during your application planning.",
        "Problem 7": "Consider which items are most applicable to your organization, and then start making necessary adjustments."
    },
    "decision driver": "code language, chosen tools, team decision, stakeholders, time consuming",
    "references": "N/A",
    "remarks": "N/A"
})
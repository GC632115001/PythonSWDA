from codeable_models import CClass, add_links
from metamodels.GT_metamodel import source
from models.E4M_ADD_models import *

source_S13 = CClass(source, "S13", values={
    "title": "6 security risks in software development and how to address them",
    "url": "https://www.infoworld.com/article/3607914/6-security-risks-in-software-development-and-how-to-address-them.html",
    "archive url": "/web/20230702162855/https://www.infoworld.com/article/3607914/6-security-risks-in-software-development-and-how-to-address-them.html",
    "source type": "Blog Post",
    "author type": "Technology Blogger",
    "date": "8 Mar 2021",
    "problem": [
        "Not treating security as a first-class devops citizen",
        "Developing proprietary technical implementations",
        "Poor governance and management of open source and commercial components",
        "Unfettered access to source code repositories and CI/CD pipelines",
        "Securing and managing sensitive data",
        "DIY security expertise and solutions"
    ],
    "solution": {
        "Problem 1.": "Require ongoing security training for the development team, and require that all newly developed APIs, microservices, integrations, and applications instrument the required security tests in their CI/CD pipelines.",
        "Problem 2.": "Communicate with product owners, enforce user story development, and leverage third-party technologies.",
        "Problem 3.": "Make clear policies, governance procedures, and a multidisciplinary team for technology management.",
        "Problem 4.": "Implement automated security testing, avoid access to repositories, and apply the principle of least privilege.",
        "Problem 5.": "Adopt data governance, educate on data practices, centralized identity management, and implement data lineage capabilities.",
        "Problem 6.": "Seek advice from security experts to identify security challenges effectively."
    },
    "decision driver": "Prioritization, stakeholders (including third-party), approachability, team cohesion.",
    "references": ["Sacolick, I. (2021, March 8). 6 security risks in software development and how to address them. InfoWorld. Retrieved from https://www.infoworld.com/article/3607914/6-security-risks-in-software-development-and-how-to-address-them.html"],
    "remarks": "N/A"
})

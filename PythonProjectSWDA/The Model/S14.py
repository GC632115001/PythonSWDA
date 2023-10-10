from codeable_models import CClass, add_links
from metamodels.GT_metamodel import source
from models.E4M_ADD_models import *

source_S14 = CClass(source, "S14", values={
    "title": "Six security challenges — and how to overcome them",
    "url": "https://www.rackspace.com/blog/six-security-challenges",
    "archive url": "/web/20230702171838/https://www.rackspace.com/blog/six-security-challenges",
    "source type": "Blog Post",
    "author type": "Technology Blogger",
    "date": "24 Aug 2021",
    "problem": [
        "Lack of Navigating the cybersecurity skills gap",
        "Defending against evolving security threats",
        "Complex environments and operations",
        "Demanding compliance mandates",
        "Lack of Maintaining business speed",
        "Cloud native applications"
    ],
    "solution": {
        "Problem 1.": "Collaborating in an agile, sprint-based model to defend against cyberattacks.",
        "Problem 2.": "Consolidate threat intelligence, security analytics, alerts, and incident response services to deploy.",
        "Problem 3.": "Use Rackspace Elastic Engineering for Security assesses, monitors, and responds to your complex cloud security challenges, providing defense-in-depth architecture for your multicloud environments.",
        "Problem 4.": "Work with security experts to define, manage, and validate governance, risk, and compliance (GRC) requirements, including PCI DSS and HIPAA.",
        "Problem 5.": "Work with security experts to protect digital investments while ensuring security resiliency.",
        "Problem 6.": "Work with cloud security expertise to build, optimize, and secure your cloud environment and applications with access to various cloud security certifications."
    },
    "decision driver": "Stakeholders, team cohesion, team decision-making, methodology.",
    "references": ["Schlueter, M. (2021, August 24). Six security challenges — and how to overcome them. Retrieved from Rackspace Blog: https://www.rackspace.com/blog/six-security-challenges"],
    "remarks": "N/A"
})
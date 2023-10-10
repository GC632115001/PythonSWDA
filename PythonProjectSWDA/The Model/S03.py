from codeable_models import CClass, add_links
from metamodels.GT_metamodel import source
from models.E4M_ADD_models import *

source_S03 = CClass(source, "S03", values={
    "title": "10 Agile Software Development Security Concerns You Need to Know",
    "url": "https://www.legitsecurity.com/blog/10-agile-software-development-security-concerns-you-need-to-know",
    "archive url": "https://web.archive.org/web/20230703033943/https://www.legitsecurity.com/blog/10-agile-software-development-security-concerns-you-need-to-know",
    "source type": "Blog post",
    "author type": "Alex Babar",
    "date": "02/10/2023",
    "problem": [
        "Inadequate Security Awareness and Training",
        "Poor Third-Party and Open-Source Management",
        "Failing to Prioritize the Security Team",
        "Opting for DIY Security",
        "Lack of Process Documentation"
    ],
    "solution": {
        "Problem 1.": "Dedicate time to focus on security awareness education and security protocol training",
        "Problem 2.": "Establishing a policy on open-source use",
        "Problem 3.": "Drive a cultural change that makes secure development a non-negotiable priority",
        "Problem 4.": "Use external security expertise to manage your security",
        "Problem 5.": "Have some reference documentation independent of the product"
    },
    "decision driver": "team cohesion, code language, chosen tools",
    "references": ["https://www.legitsecurity.com/blog/10-agile-software-development-security-concerns-you-need-to-know"],
    "remarks": "N/A"
})
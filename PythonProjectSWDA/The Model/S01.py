from codeable_models import CClass, add_links
from metamodels.GT_metamodel import source
from models.E4M_ADD_models import *

source_S01 = CClass(source, "S01", values={
    "title": "Avoiding top 10 software security design flaws",
    "url": "https://ieeecs-media.computer.org/media/technical-activities/CYBSI/docs/Top-10-Flaws.pdf",
    "archive url": "https://web.archive.org/web/20230702031229/https://ieeecs-media.computer.org/media/technical-activities/CYBSI/docs/Top-10-Flaws.pdf",
    "source type": "PDF file",
    "author type": "IEEE Computer Society",
    "date": "N/A",
    "problem": [
        "Incorrect trust assumptions",
        "An unauthorized entity having access to a system or service that it should not",
        "Neglecting to authorize after authentication",
        "Poor key management",
        "Failure to centralize cryptography"
    ],
    "solution": {
        "Problem 1.": "Make sure all data from an untrusted client are validated",
        "Problem 2.": "Implement Principle of Least Privilege",
        "Problem 3.": "Periodically perform authorization as an explicit check",
        "Problem 4.": "Strict policy-based controls to prevent the misuse/reuse of keys",
        "Problem 5.": "Use Updated and Established Cryptographic Functions, Algorithms, and Protocols"
    },
    "decision driver": "implementation methodology, Chosen tools",
    "references": ["https://ieeecs-media.computer.org/media/technical-activities/CYBSI/docs/Top-10-Flaws.pdf"],
    "remarks": "N/A"
})

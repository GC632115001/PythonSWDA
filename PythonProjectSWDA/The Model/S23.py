from codeable_models import CClass, add_links
from metamodels.GT_metamodel import source
from models.E4M_ADD_models import *

source_S23 = CClass(source, "S23", values={
    "title": "10 Agile Software Development Security Concerns You Need to Know",
    "url": "https://www.legitsecurity.com/blog/10-agile-software-development-security-concerns-you-need-to-know",
    "archive url": "https://tinyurl.com/mucett5d",
    "source type": "Blog Post",
    "author type": "Alex Babar",
    "date": "Aug 31, 2022 11:45:58 AM",
    "problem": [
        "Inadequate Security Awareness And Training",
        "Unlimited Access To Source Code Repositories",
        "Rapid Release Cycle",
        "Failing To Prioritize The Security Team"
    ],
    "solution": {
        "Problem 1.": "Strive to achieve agile security. Use modern software supply chain security tools like Legit Security that provide an aggregated security score by product line and development team.",
        "Problem 2.": "Set limitations or privacy settings to control access to source code repositories.",
        "Problem 3.": "Focus on ensuring that security vulnerability testing protocols are followed.",
        "Problem 4.": "Spend time re-framing security procedures so that team members understand why a certain security practice is important."
    },
    "decision driver": "Approachability, team cohesion (decision making).",
    "references": [
        "https://www.legitsecurity.com/blog/secure-sdlc-the-best-advice-for-securing-your-code-and-application-data-in-2022-and-beyond",
        "https://www.umsl.edu/~sauterv/analysis/F2015/Integrating%20Security%20into%20Agile%20methodologies.html.htm",
        "https://www.legitsecurity.com/blog/secure-sdlc-the-best-advice-for-securing-your-code-and-application-data-in-2022-and-beyond"
    ],
    "remarks": "N/A"
})

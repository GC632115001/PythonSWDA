from codeable_models import CClass, add_links
from metamodels.GT_metamodel import source
from models.E4M_ADD_models import *

source_S05 = CClass(source, "S05", values={
    "title": "10 Best Practices for Software Development Security",
    "url": "https://www.orientsoftware.com/blog/software-development-security/",
    "archive url": "https://web.archive.org/web/20230703035321/https://www.orientsoftware.com/blog/software-development-security/",
    "source type": "Blog post",
    "author type": "N/A",
    "date": "Nov 29, 2021",
    "problem": [
        "Poorly written code",
        "Insecure password storage",
        "Legacy software"
    ],
    "solution": {
        "Problem 1.": "Treat Software Security as a Priority Right From The Start",
        "Problem 2.": "Secure coding guidelines and standards",
        "Problem 3.": "Make sure to use software that is updated regularly"
    },
    "decision driver": "team cohesion, code language",
    "references": ["https://www.orientsoftware.com/blog/software-development-security/"],
    "remarks": "N/A"
})
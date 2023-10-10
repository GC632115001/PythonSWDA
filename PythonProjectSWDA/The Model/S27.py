from codeable_models import CClass, add_links
from metamodels.GT_metamodel import source
from models.E4M_ADD_models import *

source_S27 = CClass(source, "S27", values={
    "title": "5 User Authentication Methods that Can Prevent the Next Breach",
    "url": "https://www.idrnd.ai/5-authentication-methods-that-can-prevent-the-next-breach/",
    "archive url": "https://tinyurl.com/mr3vnv5a",
    "source type": "Blog post",
    "author type": "Gilad David Maayan",
    "date": "OCTOBER 31, 2020",
    "problem": [
        "Few types of authentication systems that make it unsafe."
    ],
    "solution": {
        "Problem": "Add more Authentication ex. Multi-factor authentication, Certificate-based authentication, Biometric authentication, and Token-based authentication."
    },
    "decision driver": "Approachability, chosen tools, prioritization",
    "references": "N/A",
    "remarks": "N/A"
})

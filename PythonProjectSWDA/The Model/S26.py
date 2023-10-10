from codeable_models import CClass, add_links
from metamodels.GT_metamodel import source
from models.E4M_ADD_models import *

source_S26 = CClass(source, "S26", values={
    "title": "Best practices for REST API security: Authentication and authorization",
    "url": "https://stackoverflow.blog/2021/10/06/best-practices-for-authentication-and-authorization-for-rest-apis/",
    "archive url": "https://tinyurl.com/24ad8eu9",
    "source type": "Blog post",
    "author type": "Sam Scott and Graham Neray",
    "date": "OCTOBER 6, 2021",
    "problem": [
        "Need authentication and authorization by using API."
    ],
    "solution": {
        "Problem": "Use OAuth2 for single sign-on (SSO) with OpenID Connect. That SSO lets your users verify themselves with a trusted third party (like Google, Microsoft Azure, or AWS) by way of token exchange to get access to a resource. They’ll log in to their Google account, for instance, and be granted access to your app."
    },
    "decision driver": "Code language, approachability, chosen tools, team cohesion (decision making)",
    "references": "N/A",
    "remarks": "N/A"
})

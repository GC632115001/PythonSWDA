from codeable_models import CClass, add_links
from metamodels.GT_metamodel import source
from models.E4M_ADD_models import *
# ### Sources ###

ecom_S01 = CClass(source, "ecom-S01", values={
    "title": "THE FUTURE OF RETAIL: EXPLORING THE POSSIBILITIES OF METAVERSE ECOMMERCE",
    "url": "https://community.nasscom.in/communities/web-30/future-retail-exploring-possibilities-metaverse-ecommerce",
    "archive url": "xx",
    "date": "27.02.23",
    "author type": "Unknown",
    "type": "General Audience Article"})
s1_codes = [ecom, building_up, integration, ecom_platform, shopify, magento, woocommerce]
add_links({ecom_S01: s1_codes}, role_name="contained_code")

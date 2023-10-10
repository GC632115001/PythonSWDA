from metamodels.guidance_metamodel import decision, design_solution, add_decision_option_link, single_answer, practice
from codeable_models import CClass, add_links, CBundle


ecom = CClass(
    decision, "How to create an e-commerce presence within the metaverse?", stereotype_instances=single_answer)

building_up = CClass(design_solution, "Build the store from the ground up", values={
                     "background reading": "s01"})
integration = CClass(design_solution, "Integrate with existing e-commerce platform",
                     values={"background reading": "s01"})

add_decision_option_link(ecom, building_up, "Building from Scratch")
add_decision_option_link(ecom, integration, "Integration")

ecom_platform = CClass(
    decision,  "Which e-commerce platform is recommended for metaverse presence?", stereotype_instances=single_answer)

shopify = CClass(practice, "Shopify", values={"background reading": "s01"})
magento = CClass(practice, "Magento", values={"background reading": "s01"})
woocommerce = CClass(practice, "Woo Commerce", values={
                     "background reading": "s01"})

add_decision_option_link(ecom_platform, shopify, "Shopify")
add_decision_option_link(ecom_platform, magento, "Magento")
add_decision_option_link(ecom_platform, woocommerce, "Woo Commerce")

add_links({integration: ecom_platform}, role_name="next decision")


_all = CBundle("ADDEcom4CAMT-Metaverse",
               elements=ecom.class_object.get_connected_elements())

ADDecommerce_model_views = [_all, {}]

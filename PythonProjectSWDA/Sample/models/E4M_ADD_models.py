from metamodels.guidance_metamodel import decision, design_solution, add_decision_option_link, single_answer, practice
from codeable_models import CClass, add_links, CBundle


ecom = CClass(
    ## change the problem to suit with the food industry in topic security
    decision, "What can we do to enhance data security within our company?", stereotype_instances=single_answer)

development = CClass(design_solution, "Make the development process that is efficiency and won't leak")
securing = CClass(design_solution, "Secure and protect data from leaks")

add_decision_option_link(ecom, development, "Dev process")
add_decision_option_link(ecom, securing, "Secure data")

ecom_dev = CClass(
    decision,"How to make the development process to be more secure?",stereotype_instances=single_answer)

devops = CClass(practice, "Require ongoing security training for the development team, and require that all newly developed APIs, microservices, integrations, and applications instrument the required security tests in their CI/CD pipelines.",values={"background reading": "s13"})
access_control = CClass(practice,"Restricted user to only necessary area",values={"background reading": "s06"})
transport = CClass(practice,"Secure the data transportation",values={"background reading": "s11"})

add_decision_option_link(ecom_dev, devops, "Exposure of sensitive data")
add_decision_option_link(ecom_dev, access_control, "Broken access control")
add_decision_option_link(ecom_dev, transport, "Insufficient transport layer protection")

add_links({development: ecom_dev}, role_name="next decision")
# add_links({ecom_dev: development}, role_name="next decision")

ecom_secure = CClass(
    decision,  "How to secure the data of the company?", stereotype_instances=single_answer)

encryption = CClass(practice, "Personal or sensitive data has to be protected with encryption", values={"background reading": "s06"})
managing = CClass(practice, "Adopt data governance, educate on data practices, centralized identity management, and implement data lineage capabilities.", values={"background reading": "s13"})
automate = CClass(practice, "Implement automated security testing, avoid access to repositories, and apply the principle of least privilege.", values={
                     "background reading": "s13"})

add_decision_option_link(ecom_secure, encryption, "Exposure of sensitive data")
add_decision_option_link(ecom_secure, managing, "Securing and managing sensitive data")
add_decision_option_link(ecom_secure, automate, "Unfettered access to source code repositories and CI/CD pipelines")

add_links({securing: ecom_secure}, role_name="next decision")
# add_links({ecom_secure: securing}, role_name="next decision")


_all = CBundle("ADDEcom4CAMT-Metaverse",
               elements=ecom.class_object.get_connected_elements())

ADDecommerce_model_views = [_all, {}]

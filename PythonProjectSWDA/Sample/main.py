from plant_uml_renderer import PlantUMLGenerator
from models.E4M_ADD_models import ADDecommerce_model_views
from os import getcwd
if __name__ == "__main__":
    # UMLgenerator
    generator = PlantUMLGenerator(delete_gen_dir_during_init=True)
    generator.directory = f'{getcwd()}/_generated'
    generator.plant_uml_jar_path = f'{getcwd()}/libs/plantuml.jar'
    generator.object_model_renderer.name_break_length = 45
    generator.object_model_renderer.left_to_right = True

    class_models = {"ADD": ADDecommerce_model_views}
    for key, value in class_models.items():
        generator.generate_object_models(key, value)

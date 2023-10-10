## Getting Started 
In order to generate the files, the following artifacts must be downloaded and installed.
- CodeableModel: https://github.com/uzdun/CodeableModels
- PlantUML: https://plantuml.com/download
- GraphViz: https://graphviz.org/download/

**Take a look at**: generators/generate_all.py which generates all figures for the models and .md/latex files. Run it in the `generators` directory using: python .\generate_all.py

## Prerequisites 
PYTHONPATH must be correctly set: 
- The directory containing `codeableModels` and `plantUMLRenderer` must be on the PYTHONPATH. 
- The directory containing this project must be on the PYTHONPATH. See plant_uml_renderer directory in Codeable Models for instructions how to set up the plant UML jar. Without further configuration it is assumed to be in the default directory: 

```
self.directory = "../_generated"
self.plant_uml_jar_path = "../../libs/plantuml.jar" 
```
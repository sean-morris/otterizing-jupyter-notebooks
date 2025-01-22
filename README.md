# otterizing-jupyter-notebooks
This repo is a template for generating the student and autograder files Jupyter notebooks with (otter-grader)[https://otter-grader.readthedocs.io/en/latest/]. The GitHub Action defined in the .github/workflows directory determines if there are been any changes to Jupyter notebooks in the raw_notebooks folder when you make a commit. If there are changes then `otter assign` is executed for the notebook and the resulting files are pushed back to the folder, "generated_notebooks".

# GH Action Workflow Permissions:
In order to allow GH Action to commit back to your repository, you need to give permission:
- Navigate to the repository's Settings on GitHub.
- Go to Actions → General.
- Under Workflow permissions, ensure: "Read and write permissions" is selected.

# Files
- assign_config.yml -- the config used on each notebook -- see the top cell of the notebooks in raw_notebooks
- assign_requirements.txt -- these are requirements the **notebooks** need to execute in the hub
- requirements.txt - these are the requirements the GH Action needs to run `otter assign`
- Dockerfile -- I created the docker image used by the GH Action. You could modify the Dockerfile, build and push your own if you have other needs. Be sure to change the image path in the workflow.

# Running locally
- Install requirements.txt in virtual environment
- Install (act)[https://nektosact.com/installation/index.html]
- act -W .github/workflows/otter-assign.yaml
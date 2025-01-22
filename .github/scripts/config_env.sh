###
# This install the python packages in the requirements file into the environment.
# Note that the requirements for running otter-grader not the requirements needed
# by the notebooks themselves. Those requirements are in assign-requirements.txt and
# referenced in the notebook itself.

# The python requirements are cached by GH Actions.
###
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r $REQUIREMENTS_FILE
python3 -m ipykernel install --user --name=python3 --display-name "Python (venv)"
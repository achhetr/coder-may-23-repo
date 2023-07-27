python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

pytest

deactivate

rm -rf .venv .pytest_cache


# check if python is installed or not
# install it if not
# check if pip install or not
# install it if not

# create a virtual environment
# activate
# install packages
# run python program
# deactivate

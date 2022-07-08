# TaskManager-Flask-Test
Simple web task list manager in pyhton3 with Flask

# DEPLOY:
<a href="https://task-manager-flask-test.herokuapp.com/" target="_blank">HERE</a>

## TO CLONE - at terminal:
1 - Clone repository:
```console
git clone https://github.com/guipatriota/TaskManager-Flask-Test.git
```
```console
cd TaskManager-Flask-Test
```
## TO RUN - at Windows prompt or Linux console with Anaconda:
1 - Activate Conda default env:

```console
conda activate
```

2 - Create new conda environment:

```console
conda create --name task_flask python
```
```console
conda activate task_flask
```
```console
conda install --name task_flask pip
```
```console
pip install -r requirements.txt
```

3 - Run app.py

```console
python app.py
```

## TO CREATE NEW DB - at terminal:
1 - Activate env:

```console
conda activate task_flask
```

2 - Run python:

```console
python
```

3 - Create db:

```python
from app import db

db.create_all()

exit()
```

FROM python:3.14

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

#           dont save pip cache, upgrade packages to last version.
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /code/src

# start app file(main router)
CMD ["fastapi", "run", "src/app.py", "--port", "80"]
# in future CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "80"]


#/code
# ├── requirements.txt
# └── src/
#      └── app.py
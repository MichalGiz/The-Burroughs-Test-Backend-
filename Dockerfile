FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./main.py /code/
COPY ./generate_empl.py /code/
# 
CMD ["python3", "generate_empl.py", "-o", "data.json", "-n", "25"] 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "1980"]

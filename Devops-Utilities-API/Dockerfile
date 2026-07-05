# Take Pateela

FROM python:3.14

# Add Ingredients

WORKDIR /app

# COPY . /app  syntax : COPY source distance   //  COPY app,services,main.py, etc /app
#    OR

COPY . .

# Mix / Process the items

RUN pip install -r requirements.txt

EXPOSE 8000

# Gas on

CMD ["python", "main.py"]

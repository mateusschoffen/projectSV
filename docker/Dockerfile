FROM python:3.9

COPY ./fornecedorlog ./fornecedorlog
COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r ./requirements.txt

CMD ["uvicorn", "fornecedorlog.api:api", "--host", "0.0.0.0", "--port", "80"]

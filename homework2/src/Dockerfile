FROM python:3.8

RUN apt-get update && apt-get install -y texlive-latex-base

RUN pip install --index-url https://test.pypi.org/simple/ --no-deps small-latex-module-mmmmarryyy

COPY generate_table.py /app/generate_table.py

CMD ["pdflatex", "/app/artifacts/2_2.tex"]

CMD ["cp", "/app/artifacts/2_2.pdf", "/app/artifacts/2_3.pdf"]

# Run with ```docker-compose up --build``` in src folder
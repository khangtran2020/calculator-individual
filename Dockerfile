FROM python:3

ADD src /src

CMD ["python", "./src/CsvReaderTest.py"]
CMD ["python", "./src/CalculatorTest.py"]
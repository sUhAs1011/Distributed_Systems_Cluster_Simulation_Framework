FROM python:3.10-slim

WORKDIR /app
COPY node_container/node_sim.py .

RUN pip install requests

CMD ["python", "node_sim.py"]

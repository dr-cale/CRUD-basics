# crud-api Documentation

The goal was to raise a PostgreSQL database and write a continuously-running Python FastAPI app that would exact the basic CRUD operations against the DB by means of API calls - create (POST), read (GET), update (PUT) and delete (DELETE). The entire infrastructure was to be containerized in Docker and clusterized in Docker Compose, with only the app exposed to the outside world (outside the confines of the cluster).

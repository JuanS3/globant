FROM postgres:latest

ENV POSTGRES_USER=globanTest
ENV POSTGRES_PASSWORD=mypassword
ENV POSTGRES_DB=employees_jobs

EXPOSE 5432

COPY init.sql /docker-entrypoint-initdb.d/

<p align="center">
  <a href="" rel="noopener">
 <img width=300px height=200px src="./assets_readme/globant_logo.png" alt="Project logo"></a>
</p>

<h3 align="center">Globant’s  Data  Engineering  Coding Challenge</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-inactive-active)]()
[![Language](https://img.shields.io/badge/language-python-blue)]()
[![Developer](https://img.shields.io/badge/Developer-Sebastián_Martínez-orange)]()

</div>

---

<p align="center"> Globant’s  Data  Engineering  Coding Challenge
    <br>
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)

## 🧐 About <a name = "about"></a>

This is a coding challenge for Globant's Data Engineering position. The challenge consists of creating an API that reads data from a CSV file, processes it and stores it in a database. The data is related to the sales of a company and the goal is to create a database that allows to query the data in a more efficient way.

The API is built using FastAPI and the database is PostgreSQL. The API has the following endpoints:

- `/upload/csv/{model}`: This endpoint receives a CSV file and a model name. The model name is used to determine the structure of the data in the CSV file. The data is processed and stored in the database. The model name can be one of the following:
  - `departments`: The CSV file contains the following columns: `department_id`, `department_name`.
  - `jobs`: The CSV file contains the following columns: `job_id`, `job_title`.
  - `employees`: The CSV file contains the following columns: `employee_id`, `employee_name`, `hired_time`, `department_id`, `job_id`.

- `/reports/hires/departments/q/{year}`: Number of employees hired for each job and department in the given year divided by quarter. The table must be ordered alphabetically by department and job.

- `/reports/hires/departments/mean/{year}`: List of ids, name and number of employees hired of each department that hired more employees than the mean of employees hired in the given year for all the departments, ordered by the number of employees hired (descending).

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them.

- Python 3.11
- Docker


### Installing

A step by step series of examples that tell you how to get a development env running.

1. Clone the repository

by https
```bash
git clone https://github.com/JuanS3/globant.git
```

by ssh
```bash
git clone git@github.com:JuanS3/globant.git
```

2. If you want to use a virtual environment, create it with the following command:

```bash
python -m venv venv
```

3. Activate the virtual environment:

GNU/Linux or MacOS
```bash
source venv/bin/activate
```

Windows
```bash
venv\Scripts\activate.bat
```

4. Install the dependencies:

```bash
pip install -r requirements.txt
```

5. Run the API:

```bash
uvicorn main:app --reload
```

6. If you want to use the database with Docker, you can run the following command:

```bash
docker-compose up -d
```

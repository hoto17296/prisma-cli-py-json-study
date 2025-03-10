FROM python:3.13

RUN apt-get update && apt-get upgrade

# Node
RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash && apt-get install -y nodejs

# Poetry
ENV POETRY_HOME /etc/poetry
RUN curl -fsSL https://install.python-poetry.org | python -
ENV PATH $POETRY_HOME/bin:$PATH
RUN poetry config virtualenvs.create false
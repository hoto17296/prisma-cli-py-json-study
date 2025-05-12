FROM python:3.13

# Node
RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash && apt-get install -y nodejs

# uv
ENV UV_PROJECT_ENVIRONMENT /usr/local
RUN pip install uv
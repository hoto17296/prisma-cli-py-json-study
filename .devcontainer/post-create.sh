#!/bin/bash -eu

uv sync

prisma generate schema.prisma --generator python
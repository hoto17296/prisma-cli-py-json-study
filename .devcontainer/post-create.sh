#!/bin/bash -eu

WORKSPACE_DIR=$(cd $(dirname $0)/..; pwd)

poetry install

prisma generate schema.prisma --generator python
#!/bin/bash

while getopts 'p:' OPTION; do
  case "$OPTION" in
  p)
    uvicorn app.main:app --reload --port "$OPTARG"
    ;;
  ?)
    uvicorn app.main:app --reload --port 8844
    ;;
  esac
done

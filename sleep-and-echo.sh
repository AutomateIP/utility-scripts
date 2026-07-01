#!/bin/bash
while [[ $# -gt 0 ]]; do
  case "$1" in
    --seconds) seconds="$2"; shift 2 ;;
    *) shift ;;
  esac
done
sleep "$seconds" && echo "Done sleeping for $seconds second(s)."

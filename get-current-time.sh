#!/bin/bash
now_iso=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
now_epoch=$(date -u +"%s")
printf '{"utc_iso": "%s", "epoch": %s}\n' "$now_iso" "$now_epoch"

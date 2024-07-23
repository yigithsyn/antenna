#!/usr/bin/bash

source <(curl https://raw.githubusercontent.com/torokmark/assert.sh/main/assert.sh --silent)
python scripts/antenna.measurement.nearFieldSamplingLength.py 1E9 --human
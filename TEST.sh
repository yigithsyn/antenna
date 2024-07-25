#!/usr/bin/bash

source <(curl https://raw.githubusercontent.com/torokmark/assert.sh/main/assert.sh --silent)
python scripts/antenna.measurement.nearFieldSamplingLength.py 1E9 --human
python scripts/propagation/lineOfSightDistance.py 0.5 # 2.524371
echo -e "1\\n4" | python scripts/propagation/lineOfSightDistance.py 4
3.57
7.14
python scripts/propagation/radioHorizon.py 0.5
2.913280
echo -e "1\\n4" | python scripts/propagation/radioHorizon.py 4
4.120000
8.240000
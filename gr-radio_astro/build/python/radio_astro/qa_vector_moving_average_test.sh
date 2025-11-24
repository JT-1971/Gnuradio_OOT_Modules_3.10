#!/usr/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/dr/Code/gr-radio_astro/python/radio_astro
export GR_CONF_CONTROLPORT_ON=False
export PATH="/home/dr/Code/gr-radio_astro/build/python/radio_astro":"$PATH"
export LD_LIBRARY_PATH="":$LD_LIBRARY_PATH
export PYTHONPATH=/home/dr/Code/gr-radio_astro/build/test_modules:$PYTHONPATH
/usr/bin/python3 /home/dr/Code/gr-radio_astro/python/radio_astro/qa_vector_moving_average.py 

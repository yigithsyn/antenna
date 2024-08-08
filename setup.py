import os
import sys
from setuptools import setup

if os.path.exists ("VERSION"):
    with open ("VERSION", 'r', encoding="utf8") as f:
        __version__ = f.read ().strip ()
else:
    __version__ = '0+unknown'

with open ('README.rst') as f:
    description = f.read ()

license     = 'MIT License'
rq          = '>=3.7'
setup \
    ( name             = "plot-antenna"
    , version          = __version__
    , description      =
        "Antenna plotting program for plotting antenna simulation results"
    , long_description = ''.join (description)
    , long_description_content_type='text/x-rst'
    , license          = license
    , author           = "Ralf Schlatterbeck"
    , author_email     = "rsc@runtux.com"
    , install_requires = \
        [ 'matplotlib', 'numpy', 'pandas', 'plotly' ]
    , packages         = ['plot_antenna']
    , platforms        = 'Any'
    , url              = "https://github.com/schlatterbeck/plot-antenna"
    , python_requires  = rq
    , entry_points     = dict
        ( console_scripts =
            [ 'plot-antenna=plot_antenna.plot_antenna:main'
            , 'plot-measurements-from-file=plot_antenna.contrib'
              ':main_csv_measurement_data'
            , 'plot-eznec=plot_antenna.eznec:main_eznec'
            ]
        )
    , classifiers      = \
        [ 'Development Status :: 4 - Beta'
        , 'License :: OSI Approved :: ' + license
        , 'Operating System :: OS Independent'
        , 'Programming Language :: Python'
        , 'Intended Audience :: Science/Research'
        , 'Intended Audience :: Other Audience'
        ]
    )
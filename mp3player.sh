#!/bin/bash

ffmpeg -i $1 -f s16le -ar 22.05k -ac 1 - | sudo ./pifmlib/pifm -

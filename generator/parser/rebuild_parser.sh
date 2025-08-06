#!/bin/bash

java -Xmx500M -cp ~/tools/antlr/antlr-4.13.2-complete.jar org.antlr.v4.Tool -Dlanguage=Python3 -visitor Rules.g4

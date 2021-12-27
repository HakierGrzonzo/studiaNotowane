#!/bin/bash

tar czf $(date --rfc-3339=s | awk '{print $1}').tar.gz ./outputs/* ./inputs/* ./raport.html 

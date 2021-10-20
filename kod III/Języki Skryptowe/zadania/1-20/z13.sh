#!/usr/bin/bash
curl https://google.com > /dev/null 2> /dev/null && \
    echo "We have interwebs" || \
    echo "We do not have interwebs"

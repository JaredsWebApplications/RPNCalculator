#!/usr/bin/env zsh

#please do NOT run this

find . -type d -name '__pycache__' -exec rm -rf {} \;
[[ ! -d past_builds ]] && mkdir past_builds
find . -maxdepth 1 -type f -name '*.zip' -exec mv {} past_builds \;
current_time="$(ct)"
zip -r "$current_time".zip . -x '*.git*' -x '*virtual_env*' -x '*past_builds*' -x 'pkgr.sh'

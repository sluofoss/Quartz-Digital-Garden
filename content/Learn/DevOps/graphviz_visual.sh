
# syntax used here is bash parameter expansion
# https://stackoverflow.com/questions/2013547/assigning-default-values-to-shell-variables-with-a-single-command-in-bash
file="${1:-content/Learn/DevOps/example2.dot}"
cat $file | python -c "import sys; import base64; import zlib; print(base64.urlsafe_b64encode(zlib.compress(sys.stdin.read().encode('utf-8'), 9)).decode('ascii'))" | sed 's/^/ https:\/\/kroki.io\/graphviz\/svg\//'

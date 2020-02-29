main_pid=$(cat /tmp/tools.pid)
sudo kill $main_pid
rm -f /tmp/tools.pid

exit 0

echo download new script>>update_log
wget https://raw.githubusercontent.com/Cerber2ol8/scripts_update/master/task.sh
sudo bash ./stop.sh
rm -f tmp.py
wget https://raw.githubusercontent.com/Cerber2ol8/scripts_update/master/tmp.py
sudo bash ./start.sh


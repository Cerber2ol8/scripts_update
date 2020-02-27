echo download new script>>update_log
#wget https://gitee.com/Cerber2ol8/scripts_update/raw/master/task.sh

sudo bash ./stop.sh
rm -f tmp.py
wget https://gitee.com/Cerber2ol8/scripts_update/raw/master/tmp.py
sudo bash ./start.sh

echo update at>>update_log
echo `date`>>update_log

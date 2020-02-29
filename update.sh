echo download new script>>update_log
#wget https://gitee.com/Cerber2ol8/scripts_update/raw/master/task.sh

sudo bash ./stop.sh
rm -f tmp.py
wget https://gitee.com/Cerber2ol8/scripts_update/raw/master/tmp.py

rm -f start.sh
rm -f out
wget https://gitee.com/Cerber2ol8/scripts_update/raw/master/start.sh

cp /tmp/version.txt version.txt
echo update at>>update_log
echo `date`>>update_log
sudo bash ./start.sh

exit 0

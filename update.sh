echo download new script>>update_log
#wget --timeout=10 --waitretry=2 --tries=3 https://gitee.com/Cerber2ol8/scripts_update/raw/master/task.sh

sudo bash ./stop.sh
rm -f tmp.py
#wget --timeout=10 --waitretry=2 --tries=3 https://gitee.com/Cerber2ol8/scripts_update/raw/master/tmp.py
wget --timeout=10 --waitretry=2 --tries=3 https://raw.githubusercontent.com/Cerber2ol8/scripts_update/master/tmp.py

#rm -f start.sh
rm -f print.out
#wget --timeout=10 --waitretry=2 --tries=3 https://gitee.com/Cerber2ol8/scripts_update/raw/master/start.sh
#wget --timeout=10 --waitretry=2 --tries=3 https://raw.githubusercontent.com/Cerber2ol8/scripts_update/master/start.sh

cp /tmp/version.txt version.txt
echo update at>>update_log
echo `date`>>update_log
sudo bash ./start.sh

exit 0

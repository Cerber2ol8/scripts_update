import schedule
import time
import os
import sys
from datetime import datetime
import logging

LOG_FILE = '/home/mytools.log'
PID_FILE = '/tmp/tools.pid'
VERSION_FILE = '/tmp/version.txt'
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.DEBUG,
    format="%(asctime)-15s [pid:%(process)d] [thread:%(threadName)s] [%(filename)s] [%(levelname)s] %(message)s",
)
LOG = logging.getLogger(__name__)


def check_update():
    
    
    if not os.path.exists('version.txt'):
        try:
            os.system('wget -P /tmp https://raw.githubusercontent.com/Cerber2ol8/scripts_update/master/version.txt')
            update()

        finally:
            return

    with open('version.txt', 'r') as f:
        cur_version = f.read()
        try:
            if os.path.exists('/tmp/version.txt'):
                os.remove('/tmp/version.txt')
                time.sleep(1)
            os.system('wget -P /tmp https://raw.githubusercontent.com/Cerber2ol8/scripts_update/master/version.txt')
            if os.path.exists('/tmp/version.txt'):
                with open('/tmp/version.txt', 'r') as f1:
                    lastest_version = f1.read()
                    if cur_version != lastest_version:
                        update()
                    
                    
        finally:
            save_pid(PID_FILE)

def update():
    if os.path.exists('update.sh'):
        os.remove('update.sh')
    time.sleep(1)
    os.system('wget https://raw.githubusercontent.com/Cerber2ol8/scripts_update/master/update.sh')
    os.system('sudo bash ./update.sh')
    os.system('cp /tmp/version.txt version.txt')
    os.system("echo "+datetime.now().strftime("%Y-%m-%d %H:%M:%S")+">>log")
    os.system('echo last update update>>log')

def save_pid(pid_file):
    pid = os.getpid()
    with open(pid_file, 'w+') as f:
        f.write(str(os.getpid()))

def test_task():
    os.system('sudo bash ./task.sh')
    os.system('echo task test>>task_log')


if __name__ == '__main__':
    if os.path.exists(PID_FILE):
        os.system('sudo bash ./stop.sh')


            

    save_pid(PID_FILE)
    schedule.every(10).seconds.do(check_update)
    schedule.every().day.at("00:04").do(test_task)
    while True:
        schedule.run_pending()

        time.sleep(1)
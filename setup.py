from crontab import CronTab
import os

PROJECT_DIRECTORY = input("Project Directory: ")
DOCKER_BUILD_CMD = input("Docker Build Command: ")
DOCKER_RUN_CMD = input("Docker Run Command: ")
DOCKER_NAME = input("Docker Container Name: ")

FILE_INPUT = PROJECT_DIRECTORY + '\n' + DOCKER_BUILD_CMD \
            + '\n' + DOCKER_RUN_CMD + '\n' + DOCKER_NAME

CMD = f'python3 {os.getcwd()}/check.py < {FILE_INPUT}'

check_cron = CronTab(os.popen("echo $USER").read().strip())
job = check_cron.new(command=CMD)
job.minute.every(30)

if not os.system(CMD):
    print("Successfully Installed Crontab")
    check_cron.write()
else:
    print("Error")
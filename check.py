import os

PROJECT_DIRECTORY = input()
DOCKER_BUILD_CMD = input()
DOCKER_RUN_CMD = input()
DOCKER_NAME = input()

os.chdir(PROJECT_DIRECTORY)

if os.popen("git diff").read() != '':
    # Pull, rebuild, kill and run
    a = os.system("git pull")
    if a != 0:
        exit(a)

    a = os.system(DOCKER_BUILD_CMD)
    if a != 0:
        exit(a)
        
    a = os.system(f"docker kill {DOCKER_NAME}")
    if a != 0:
        exit(a)

    a = os.system(DOCKER_RUN_CMD)
    if a != 0:
        exit(a)
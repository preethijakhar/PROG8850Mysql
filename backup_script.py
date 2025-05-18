import os
import datetime
import subprocess

MYSQL_USER = 'root'
MYSQL_PASSWORD = 'pass'
MYSQL_HOST = 'localhost'
DATABASE_NAME = 'database_name'
BACKUP_DIR = 'backups'

def Create_b():
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

    time_s = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    File_backup = f"{DATABASE_NAME}_backup_{time_s}.sql"
    path_backup = os.path.join(BACKUP_DIR, File_backup)

    dump_command = [
        'mysqldump',
        f'-h{MYSQL_HOST}',
        f'-u{MYSQL_USER}',
        f'-p{MYSQL_PASSWORD}',
        DATABASE_NAME
    ]

    with open(path_backup, 'w') as backup_file:
        try:
            subprocess.run(dump_command, stdout=backup_file, check=True)
            print(f"backup_succes: {path_backup}")
        except subprocess.CalledProcessError as e:
            print("backup_failed:", e)

if __name__ == "__main__":
    Create_b()

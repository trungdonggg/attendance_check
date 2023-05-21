# Attendance Check Project
## Install Mysql server and Mysql Workbench
For windows: https://www.simplilearn.com/tutorials/mysql-tutorial/mysql-workbench-installation
For linux:
1. Install mysql server:
    ```bash
    sudo apt update
    sudo apt install mysql-server
    sudo systemctl start mysql.service
2. Install mysql workbench:
    ```bash
    sudo snap install mysql-workbench-community
    sudo snap connect mysql-workbench-community:password-manager-service :password-manager-service #run the given command to let the SNAP access the workbench password manager feature
3. Create the new USER:
    ```bash
    sudo mysql
    CREATE USER 'username'@'host' IDENTIFIED WITH authentication_plugin BY 'password';
## Create the Mysql databeases
1. Copy file mysql.sql to Documents.
2. Open Mysql Workbench and Login account.
3. Select File -> Open Mysql Script -> Documents -> mysql.sql.
4. Run.
    






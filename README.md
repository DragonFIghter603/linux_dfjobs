# dfjobs

a job management system for ubuntu server.

Start/stop jobs manually or register them to launch at start

### Setup

1. clone the repo
    ```sh
    git clone https://github.com/DragonFIghter603/linux_dfjobs.git ~/tools/dfjobs
    ```
2. give `dfjobs.py` execution permission
    ```sh
    chmod +x dfjobs.py
    ```
3. symlink `dfjobs.py` to make it a global command:  
    ```sh
    ln ~/tools/dfjobs/dfjobs.py /bin/dfjobs
    ```
4. add command to run on system startup <br>
    add this line to crontab (edit with `crontab -e`)
    ```
    @reboot dfjobs startall
    ```
5. add command to run on system shutdown <br>
    ```sh
    sudo nano /etc/rc6.d/dfjobs_shutdown.sh
    # in nano editor:
    dfjobs kill_all
    # ---
    sudo chmod +x /etc/rc6.d/dfjobs_shutdown.sh
    ```
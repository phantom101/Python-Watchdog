# Python-Watchdog
# by Patrick Schmoll 2024
# For more information visit: https://github.com/phantom101/Python-Watchdog 

import configparser
import subprocess
import time
import os

check_interval = 5

def watchdog_read_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    return config['settings']

def start_script(script_name):
    print(f"Starting {script_name}...")
    return subprocess.Popen(['python', script_name])

def stop_script(process):
    if process:
        print("Stopping the script...")
        process.terminate()
        process.wait()
        print("Script stopped.")
        

def watchdog_update(config_file, option, value):
    
    config = configparser.ConfigParser()
    config.read(config_file)
    
    section = 'settings'
    
    if section not in config:
        print(f"The section '{section}' could not be found.")
        return
    if option not in config[section]:
        print(f"The option '{option}' could not be found.")
        return
    
    config[section][option] = str(value)
    
    with open(config_file, 'w') as configfile:
        config.write(configfile)
    
    print(f"The value of '{option}' in '{config_file}' has changed to '{value}'.")


def manage_scripts(script_process_dict, config):
    for key in config.keys():
        if key.startswith('script'):
            script_name = config[key]
            start_key = f'start{key[-1]}'
            stop_key = f'stop{key[-1]}'
            restart_key = f'restart{key[-1]}'
            
            if config.getint(start_key) and (script_name not in script_process_dict or script_process_dict[script_name] is None):
                script_process_dict[script_name] = start_script(script_name)

            elif config.getint(stop_key) and script_name in script_process_dict:
                stop_script(script_process_dict[script_name])
                del script_process_dict[script_name]

            elif script_name in script_process_dict and config.getint(restart_key) == 1:
                if script_process_dict[script_name] is not None and script_process_dict[script_name].poll() is not None:
                    print(f"Script {script_name} has stopped, restarting...")
                    script_process_dict[script_name] = start_script(script_name)

def run_watchdog(config_file='config.ini'):
    last_modified_time = os.path.getmtime(config_file)
    config = watchdog_read_config(config_file)
    script_process_dict = {}

    try:
        while True:
            manage_scripts(script_process_dict, config)

            current_modified_time = os.path.getmtime(config_file)
            if current_modified_time != last_modified_time:
                print("Configuration file has changed! Reloading...")
                last_modified_time = current_modified_time
                config = watchdog_read_config(config_file)

            time.sleep(check_interval)

    except KeyboardInterrupt:
        for process in list(script_process_dict.values()):
            stop_script(process)

if __name__ == "__main__":
    run_watchdog()
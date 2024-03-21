import subprocess
import sys

def check_and_install(module_name):
    try:
        # Try to import the specified module
        __import__(module_name)
        #print(f"{module_name} is already installed.")
    except ImportError:
        #print(f"{module_name} is not installed. Installing...")
        try:
            # Execute the pip installation command for the module
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', module_name])
            #print(f"{module_name} has been installed successfully.")

            # Check for pip upgrade
            try:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
                #print("pip has been upgraded successfully.")
            except subprocess.CalledProcessError as e:
                print(f"Error during pip upgrade: {e}")

        except subprocess.CalledProcessError as e:
            print(f"Error during the installation of {module_name}: {e}")


# Use the function to check and install psutil and upgrade pip if necessary
check_and_install("psutil")
import psutil

def close_existing_chromedrivers():
    # Trouver tous les processus chromedriver en cours d'exécution
    chromedriver_processes = []
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == 'chromedriver':
            chromedriver_processes.append(proc)

    # Terminer tous les processus chromedriver en cours d'exécution
    for proc in chromedriver_processes:
        proc.terminate()

def terminate_existing_chrome_processes():
    try:
        for proc in psutil.process_iter(['pid', 'name']):
            if 'chrome.exe' in proc.info['name']:
                #print(f"Terminating Chrome process with PID {proc.info['pid']}")
                psutil.Process(proc.info['pid']).terminate()
        # Fermer toutes les autres instances WebDriver déjà lancées
        close_existing_chromedrivers()
        #print("Existing Chrome processes terminated.")
    except Exception as e:
        print(f"Error terminating Chrome processes: {e}")

# Call the function to terminate Chrome processes
terminate_existing_chrome_processes()



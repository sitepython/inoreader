from ChomeTools import check_and_install
check_and_install("selenium")
check_and_install("pyautogui")
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime
import pyautogui

def google_chrome(website_url):
    local_app_data = os.environ['LOCALAPPDATA']
    user_data_directory = os.path.join(local_app_data, 'Google', 'Chrome', 'User Data')

    # Create ChromeOptions object
    chrome_options = Options()

    # Add the user data directory option
    chrome_options.add_argument(f"user-data-dir={user_data_directory}")

    # Initialize the Chrome browser with options
    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to the specified URL
    driver.get(website_url)

    # Wait for the page to load (you might need to adjust the waiting time)
    driver.implicitly_wait(30)
    
    return driver
    
def save_page_source(driver):
    # Capture d'écran
    screenshot = pyautogui.screenshot()
    
    # Récupérez la date et l'heure actuelles
    now = datetime.datetime.now()
    
    # Formatez la date et l'heure dans une chaîne
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

    # Récupérez le chemin absolu du dossier du script Python
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Définissez le chemin complet du fichier texte avec la date et l'heure dans le nom
    file_name = f"code_source_{timestamp}.txt"
    file_path = os.path.join(script_dir, file_name)
    
    # Récupérez le code source de la page Web
    page_source = driver.page_source

    # Enregistrez le code source dans un fichier texte
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(page_source)

    # Enregistrement de l'image dans un fichier
    image_name = f"code_source_{timestamp}.png"
    chemin_fichier = os.path.join(script_dir, image_name)
    screenshot.save(chemin_fichier)
        

def is_element_visible(driver, css_selector):   
    elements = driver.find_elements(By.CSS_SELECTOR, css_selector)
    if elements:
        element = elements[0]  # Sélectionner le premier élément de la liste
        is_visible = element.is_displayed()
    else:
        is_visible = False
    return is_visible
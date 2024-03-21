from ChomeTools import check_and_install,terminate_existing_chrome_processes
from CodeJs import google_chrome

website_url = "https://www.inoreader.com/all_articles"

# terminate Chrome processes
print("terminate Chrome processes")
terminate_existing_chrome_processes()
print("===========================>1.terminate Chrome processes")
# lancer la page d'article
print("lancer all_articles")
driver = google_chrome(website_url)
print("===========================>2.lancer all_articles")
# Extraire les éléments div dans #reader_pane
check_and_install("beautifulsoup4")     
from selenium import webdriver
from bs4 import BeautifulSoup
import os
import time
from datetime import datetime

def file_name():
    # Obtenir la date et l'heure actuelles
    current_datetime = datetime.now()
    date_string = current_datetime.strftime("%Y-%m-%d")
    time_string = current_datetime.strftime("%H-%M-%S")

    # Construire le nom du fichier avec la date et l'heure actuelles
    file_name = f"result_{date_string}_{time_string}.txt"
    
    # Déterminer le chemin du script en cours d'exécution
    script_path = os.path.realpath(__file__)
    script_directory = os.path.dirname(script_path)
    file_path = os.path.join(script_directory, file_name)
    return file_path

def save_attributes_to_file(div_id, data_oid, title,file_path):
   
    with open(file_path, "a") as file:
            file.write(f"div_id: {div_id}\n")
            file.write(f"https://www.inoreader.com/article/{data_oid}-\n")
            file.write(f"{title}\n")
            file.write("-------------------------------------------------------------------\n")
     
def afficher_liste_div(driver):
    # Obtenir le code HTML de la page
    html = driver.page_source

    # Extraire les éléments div avec BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    reader_pane = soup.select_one('#reader_pane')
    div_list = reader_pane.find_all('div', recursive=False)
    # Construire le chemin du fichier de sortie
    file_path = file_name()
    # Afficher la liste des div
    for index, div in enumerate(div_list):
        div_id = div.get('id')
        data_oid = div.get('data-oid')
        print(f"{index + 1} : {div_id}")
        print(f"https://www.inoreader.com/article/{data_oid}-")
        print("-------------------------------------------------------------------")
        child_element = div.select_one(".header_date.flex.graylink")
        if child_element:
                title = child_element.get("title")
                print("Date:", title)
        save_attributes_to_file(div_id, data_oid, title,file_path)
    print("Résultats enregistrés dans le fichier")        
# Exécuter le script JavaScript de défilement
def scroll_to_element_by_id(driver, element_id):

    # Exécuter le script JavaScript de défilement
    script = f"document.getElementById('{element_id}').scrollIntoView();"
    driver.execute_script(script)


# Appeler la fonction en fournissant l'URL de la page et l'ID de l'élément à faire défiler

for _ in range(10):
    scroll_to_element_by_id(driver, "next_articles")
    # Mettre en pause pendant 1 seconde
    time.sleep(1)
    
# Appeler la fonction en fournissant l'URL de la page
afficher_liste_div(driver)
# Fermer le navigateur
# driver.quit()


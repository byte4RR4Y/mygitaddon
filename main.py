import xbmcgui
import git
import xbmc
import os

# Funktion zum Klonen eines Git-Repositorys
def clone_git_repository(url):
    try:
        # Extrahiere den Namen des Git-Repositorys aus der URL
        repo_name = url.split("/")[-1].split(".git")[0]

        # Hier wird das Zielverzeichnis auf ~/.kodi/addons/ gesetzt
        target_directory = os.path.join(xbmc.translatePath('special://home/addons/'), repo_name)

        # Klonen Sie das Git-Repository in das benannte Verzeichnis
        git.Repo.clone_from(url, target_directory)
        xbmcgui.Dialog().notification('Erfolg', 'Repository wurde geklont.', xbmcgui.NOTIFICATION_INFO, 5000)
    except Exception as e:
        xbmcgui.Dialog().notification('Fehler', str(e), xbmcgui.NOTIFICATION_ERROR, 5000)

# Erstellen Sie ein List-Dialog-Fenster für die URL-Eingabe
dialog = xbmcgui.Dialog()
url = dialog.input('Git Repository URL eingeben', type=xbmcgui.INPUT_ALPHANUM)

# Überprüfen, ob eine URL eingegeben wurde
if url:
    # Rufen Sie die Funktion auf, um das Repository zu klonen
    clone_git_repository(url)
else:
    xbmcgui.Dialog().notification('Hinweis', 'Keine URL eingegeben.', xbmcgui.NOTIFICATION_INFO, 5000)

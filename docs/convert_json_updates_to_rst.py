# Queste funzioni vengono eseguite al momento della compilazione della documentazione, dal file conf.py
import json
import os


def get_json_data(path):
    # Carica il json in una variabile data, se non esiste il path restituisce None
    broken_json = False
    data = None
    if os.path.isfile(path):
        with open(path) as f:
            # noinspection PyBroadException
            try:
                data = json.load(f)
            except:
                pass

    return data

def update_changelog():

    import os
    import requests
    # "updates.rst" è il file rst contenuto nella directory docs che contiene la lista delle modifiche

    # ottengo il file rst dalla directory docs he è nella stessa root di questo file
    updates_rst = os.path.join(os.path.dirname(__file__), "updates_log.rst")

    # The json_path is into te up directory with "exa_update.json" filename
    json_path = os.path.join(os.path.dirname(__file__), "..", "exa_update.json")
    json_data = get_json_data(json_path)

    updates = json_data["updates"]

    with open(updates_rst, "w") as f:

        # add the anchor:
        f.write(".. _updates_log:\n")
        f.write("\n")
        # Go ahead after the first line
        f.write("Updates Log\n")
        f.write("===========\n")
        f.write("\n")

        version_index = -1
        for version, value in updates.items():
            version_index += 1
            date = value.get("date")
            # Check if "xx" are present into "date" value, if yes, skip the writing of the update because it still not released
            if "xx" in date:
                continue

            video_embed_code = value.get("video_embed_code")

            # Scriviamo la versione
            version_date = "{}".format(version)
            f.write(version_date + "\n")
            f.write("-" * len(version_date) + "\n")
            f.write("\n")
            f.write("**Release date: {} (D/M/Y)**\n".format(date))
            f.write("\n")
            descriptions = value.get("descriptions")
            if video_embed_code:
                f.write(".. raw:: html\n")
                f.write("\n")
                f.write("    " + video_embed_code)
                f.write("\n")
                f.write("\n|")
                f.write("\n")
                f.write("\n")


            for idx, title_description in descriptions.items():
                title = title_description.get("title")
                description = title_description.get("description")

                f.write("- **" + title + "**\n")
                f.write("\n")
                f.write("    " + description + "\n")
                f.write("\n")

            if version_index < len(updates) - 1:

                f.write("\n")
                f.write("\n")
                f.write("--------------------------------------------------------------------------------------------")
                f.write("\n")
                f.write("\n")

    print("updates_log.rst recompiled :)")



def compile_al_materials_previews():

    path = "G:\\Cc0 Archivio Ufficiale\\EXTREME_PBR_DEFAULT_LIB"


    mat_previews = {}

    for cat in os.listdir(path):
        if cat.startswith("."):
            continue

        mat_files = mat_previews[cat] = {}

        cat_path = os.path.join(path, cat)

        for mat in os.listdir(cat_path):
            if not os.path.isdir(os.path.join(cat_path, mat)):
                continue
            mat_path = os.path.join(cat_path, mat)

            preview_folder = os.path.join(mat_path, "data", "previews", "default")
            if not os.path.isdir(preview_folder):
                continue

            for preview in os.listdir(preview_folder):
                preview_path = os.path.join(preview_folder, preview)
                # Se i file sono di tipo png o jpg li aggiungo alla lista
                if preview.endswith(".png") or preview.endswith(".jpg"):
                    mat_files[mat] = preview_path

    material_previews = os.path.join(os.path.dirname(__file__), "material_previews.rst")
    with open(material_previews, "w") as f:
        f.write("All Materials\n")
        f.write("===========\n")
        f.write("\n")

        for cat, mats in mat_previews.items():
            f.write(cat + "\n")
            f.write("-" * len(cat) + "\n")
            f.write("\n")

            for mat, preview_file in mats.items():
                f.write(mat + "\n")
                f.write("*" * len(mat) + "\n")
                f.write("    .. image:: {}\n".format(preview_file))
                f.write(":align: center\n")
                f.write(":width: 300\n")
                f.write(":alt: {}\n".format(mat))








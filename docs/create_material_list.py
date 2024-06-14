# Questo script deve prendere tutti i file di preview contenuti in EXTREMEPBR_DEFAULT_LIBRARY e creare una pagina rst di
# nome "material_list" i preview PNG devono essere convertiti in webp con compressione al 50% e spostati nella cartella
# material_list della documentazione


import os

from convert_json_updates_to_rst import get_json_data


def clean_name(name):
    return name.replace(" - ", "_").replace("_", " ").replace(" ", "_").lower()

def make_material_list():
    # Dichiariamo i percorisi

    extreme_pbr_lib_folder = "C:\\Users\\dnadj\\Desktop\\Extreme PBR Test\\EXTREME_PBR_DEFAULT_LIB"

    # material_list_folder è nel progetto corrente nella cartella _static\images\material_list se non esiste bisogna crearla
    material_list_folder = os.path.join(os.path.dirname(__file__), "_static", "_images", "material_list")
    # La material_list_rst invece va nella cartella superiore e nella docs contenuta in essa, get the parent folder:
    parent_folder_up = os.path.dirname(os.path.dirname(__file__))
    material_list_rst = os.path.join(parent_folder_up, "docs", "material_list.rst")

    # The json_path is into te up directory with "exa_update.json" filename
    json_path = os.path.join(os.path.dirname(__file__), "..", "exa_library_volumes.json")
    json_data = get_json_data(json_path)
    exapacks = json_data["exapacks"]


    if not os.path.isdir(material_list_folder):
        os.mkdir(material_list_folder)
    total_mat_idx = 0
    mat_dict = {}
    for cat in os.listdir(extreme_pbr_lib_folder):
        cat_folder = os.path.join(extreme_pbr_lib_folder, cat)
        if not os.path.isdir(cat_folder):
            continue

        if cat.startswith("."):
            continue

        # create category folder inside material_list_folder if not exists
        category_folder = os.path.join(material_list_folder, clean_name(cat))
        if not os.path.isdir(category_folder):
            os.mkdir(category_folder)

        cat_dict = mat_dict.get(cat)
        if not cat_dict:
            cat_dict = mat_dict[cat] = {}

        for mat in os.listdir(cat_folder):
            total_mat_idx += 1
            print(total_mat_idx, "Found Mat:", mat)
            mat_folder = os.path.join(cat_folder, mat)

            data_folder = os.path.join(mat_folder, "data")
            if not os.path.isdir(data_folder):
                continue

            if mat.startswith("."):
                continue

            preview_folder = os.path.join(data_folder, "previews")
            if not os.path.isdir(preview_folder):
                continue

            default_folder = os.path.join(preview_folder, "default")
            if not os.path.isdir(default_folder):
                continue

            # create material folder inside category_folder if not exists
            material_folder = os.path.join(category_folder, clean_name(mat))
            if not os.path.isdir(material_folder):
                os.mkdir(material_folder)

            preview_png = next((os.path.join(default_folder, fn) for fn in os.listdir(default_folder) if
                                fn.endswith(".png") or fn.endswith(".jpg") or fn.endswith(".webp")), None)
            if not preview_png:
                continue

            mat_fn = clean_name(mat)
            # convert preview_png to webp
            from PIL import Image
            new_preview_webp = mat_fn + ".webp"
            if not os.path.isfile(os.path.join(material_folder, new_preview_webp)):
                print("Sto convertendo l'immagine:", preview_png)
                new_preview_webp_path = os.path.join(material_folder, new_preview_webp)
                im = Image.open(preview_png)
                im.save(new_preview_webp_path, "webp", quality=50)

            exapacks_found = get_material_exapacks(mat, exapacks)

            cat_dict[mat] = {
                "preview": new_preview_webp,
                "exapacks": exapacks_found
            }


    writing_mat_index = 0
    len_cat=len(mat_dict)
    # Crea l'intestazione nella pagina con il nome Material List
    with open(material_list_rst, "w") as f:
        name = "Material List"
        f.write(name + "\n")
        f.write("=" * len(name) + "\n")
        f.write("\n")
        f.write("\n")
        info = "This is the complete list of materials contained in the Default Library of Extreme PBR." \
                "Here you can search for the materials you are interested in order to find the .exapack files that contain that material."

        f.write(info + "\n")
        f.write("\n")
        f.write(".. tip:: To search for the material you are interested in, you can search in the sidebar at the top left, or press `Ctrl + F` and type the name of the material you are looking for.\n")
        f.write("\n")
        f.write("|")
        f.write("\n")
        f.write("\n")
        for cat_idx, (cat, cat_dict) in enumerate(mat_dict.items()):
            cat_tile = cat.title() + " (Category)"
            f.write(cat_tile + "\n")
            f.write("-" * len(cat_tile) + "\n")
            f.write("\n")

            for mat_idx, (mat, mat_dict) in enumerate(cat_dict.items()):
                writing_mat_index += 1
                len_mat = len(mat_dict)
                print(writing_mat_index, "Writing Mat:", mat)
                preview_webp = mat_dict.get("preview")
                mat_title = mat.title()
                f.write(mat_title + "\n")
                f.write("*" * len(mat_title) + "\n")
                f.write("\n")
                f.write(".. image:: _static/_images/material_list/" + clean_name(cat) + "/" + clean_name(mat) + "/" + preview_webp + "\n")
                f.write("    :width: 30%\n")
                f.write("    :align: center\n")
                f.write("    :alt: " + mat_title + "\n")
                f.write("\n")
                f.write("\n")
                f.write("|")
                f.write("\n")
                f.write("\n")
                #
                # Qui dobbiamo scrivere in quali exapack è contenuto il materiale:
                exapacks_found = mat_dict.get("exapacks")
                f.write("**This material is contained in the following Exapacks:**\n")
                f.write("\n")
                for exa_idx, exapack in enumerate(exapacks_found):
                    if exa_idx != 0:
                        f.write("\n")
                    f.write("    - " + exapack + "\n")

                    if len(exapacks_found) != exa_idx + 1:
                        f.write("\n")

                # Qui bisogna disegnare un separatore, solo se il materiale non è l'ultimo materiale di tutti

                if total_mat_idx != writing_mat_index:
                    f.write("\n")
                    f.write("-" * 120 + "\n")
                    f.write("\n")
                    f.write("\n")





def get_material_exapacks(name, exapacks):
    # Il mat_name sarà per esempio "acoustic_foam_001"
    exapacks_found = []
    for exapack_vol_name, pack_dict in exapacks.items():
        file_dict = pack_dict.get("files_dict")
        if not file_dict:
            continue

        for idx, file_d in file_dict.items():
            file_name = file_d.get("file_name")
            if not file_name:
                continue
            file_name_clean = file_name.replace(".png", "").replace(".jpg", "").replace(".webp", "")
            if name == file_name_clean:
                exapacks_found.append(exapack_vol_name)

    return exapacks_found





def generate_exa_libraries_page():
    """Genera la pagina doc contenente tutti gli Exapack"""

    # ottengo il file rst dalla directory docs he è nella stessa root di questo file
    updates_rst = os.path.join(os.path.dirname(__file__), "exapack_dict.rst")


    # The json_path is into te up directory with "exa_update.json" filename
    json_path = os.path.join(os.path.dirname(__file__), "..", "exa_library_volumes.json")
    json_data = get_json_data(json_path)


    exapacks = json_data["exapacks"]

    material_dict = {}
    for exapack_vol_name, pack_dict in exapacks.items():
        file_dict = pack_dict.get("files_dict")
        if not file_dict:
            continue

        for idx, file_d in file_dict.items():

            mat_name = file_d.get("file_name")
            if not mat_name:
                continue
            if mat_name in ["mat_info.json", "tags.json"]:
                continue
            if "_xtm_" in mat_name:
                continue

            if not material_dict.get(exapack_vol_name):
                material_dict[exapack_vol_name] = []

            mat_name_clean = mat_name.replace(".png", "").replace(".jpg", "").replace(".webp", "")
            material_dict[exapack_vol_name].append(mat_name.replace(".png", "").replace(".jpg", "").replace(".webp", ""))

















# Questo script deve prendere tutti i file di preview contenuti in EXTREMEPBR_DEFAULT_LIBRARY e creare una pagina rst di
# nome "material_list" i preview PNG devono essere convertiti in webp con compressione al 50% e spostati nella cartella
# material_list della documentazione


import os

from convert_json_updates_to_rst import get_json_data


def clean_name(name):
    return name.replace(" - ", "_").replace("_", " ").replace(" ", "_").lower()


def make_material_list():
    # Dichiariamo i percorisi

    # Questa cartella è quella di Extreme PBR, occhio che potrebbe essere su un altra posizione.
    extreme_pbr_lib_folder = "C:\\Users\\dnadj\\Desktop\\Extreme PBR Test\\EXTREME_PBR_DEFAULT_LIB"

    # material_list_folder è nel progetto corrente nella cartella _static\images\material_list se non esiste bisogna crearla
    material_list_folder = os.path.join(os.path.dirname(__file__), "_static", "_images", "material_list")
    if not os.path.isdir(material_list_folder):
        os.mkdir(material_list_folder)

    # La material_list_rst invece va nella cartella superiore e nella docs contenuta in essa, get the parent folder:
    parent_folder_up = os.path.dirname(os.path.dirname(__file__))
    material_list_file_rst = os.path.join(parent_folder_up, "docs", "material_list.rst")

    material_list_folder_rst = os.path.join(parent_folder_up, "docs", "material_list_rst")
    if not os.path.isdir(material_list_folder_rst):
        os.mkdir(material_list_folder_rst)

    # The json_path is into te up directory with "exa_update.json" filename
    json_path = os.path.join(os.path.dirname(__file__), "..", "exa_library_volumes.json")
    json_data = get_json_data(json_path)
    exapacks = json_data["exapacks"]

    test_idx = 0

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
            # test_idx += 1
            # if test_idx > 10:
            #     break
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

            new_preview_webp_path = os.path.join(material_folder, new_preview_webp)
            if not os.path.isfile(new_preview_webp_path):
                print("Sto convertendo l'immagine:", preview_png)
                print("Al nuovo path:", new_preview_webp_path)
                im = Image.open(preview_png)
                im.save(new_preview_webp_path, "webp", quality=10)

            exapacks_found = get_material_exapacks(mat, exapacks)

            cat_dict[mat] = {
                "preview": new_preview_webp,
                "exapacks": exapacks_found
            }

    writing_mat_index = 0
    len_cat = len(mat_dict)
    # Crea l'intestazione nella pagina con il nome Material List
    with open(material_list_file_rst, "w") as ml_index:
        name = "Material List"
        ml_index.write(name + "\n")
        ml_index.write("=" * len(name) + "\n")
        ml_index.write("\n")
        ml_index.write("\n")

        info = "This is the complete list of materials in Extreme PBR, here you will find all the categories, within them " \
               "you will find the preview of the material, its name, and also the file.exapack in which it is contained."

        ml_index.write(info + "\n")
        ml_index.write("\n")

        tip = "To search for the material you are interested in, you can search in the sidebar at the top left, " \
              "or go to the category where you want to search for the material press `Ctrl + F` and then type the name of the material you are looking for."

        ml_index.write(".. tip:: {}\n".format(tip))


        ml_index.write("\n")
        ml_index.write("|")
        ml_index.write("\n")
        ml_index.write("\n")
        ml_index.write(".. toctree::\n")
        ml_index.write("   :maxdepth: 1\n")
        ml_index.write("   :caption: Categories\n")
        ml_index.write("\n")
        ml_index.write("\n")

        for cat_idx, (cat, cat_dict) in enumerate(mat_dict.items()):
            print("Writing Cat:", cat)
            cat_file_name = " ".join(cat.replace("-", "").split()).replace(" ", "_").lower()
            cat_formatted = cat_file_name + ".rst"
            cat_rst = os.path.join(material_list_folder_rst, cat_formatted)
            print("Writing Cat RST:", cat_rst)

            # ----------------------------------------------------------------------------------------------------------
            # Qui scrive nell'indice del material_list.rst
            ml_index.write("   {}/{}\n".format("material_list_rst", cat_file_name))
            # ----------------------------------------------------------------------------------------------------------

            with open(cat_rst, "w") as cat_file:
                cat_tile = cat.title() + " (Category)"
                cat_file.write(cat_tile + "\n")
                cat_file.write("-" * len(cat_tile) + "\n")
                cat_file.write("\n")

                for mat_idx, (mat, mat_dict) in enumerate(cat_dict.items()):
                    writing_mat_index += 1
                    len_mat = len(mat_dict)
                    print(writing_mat_index, "Writing Mat:", mat)
                    preview_webp = mat_dict.get("preview")
                    mat_title = mat.title()
                    cat_file.write(mat_title + "\n")
                    cat_file.write("*" * len(mat_title) + "\n")
                    cat_file.write("\n")
                    cat_file.write(".. image:: ../_static/_images/material_list/" + clean_name(cat) + "/" + clean_name(
                        mat) + "/" + preview_webp + "\n")
                    cat_file.write("    :width: 30%\n")
                    cat_file.write("    :align: center\n")
                    cat_file.write("    :alt: " + mat_title + "\n")
                    cat_file.write("\n")
                    cat_file.write("\n")
                    cat_file.write("|")
                    cat_file.write("\n")
                    cat_file.write("\n")
                    #
                    # Qui dobbiamo scrivere in quali exapack è contenuto il materiale:
                    exapacks_found = mat_dict.get("exapacks")
                    cat_file.write("**This material is contained in the following Exapacks:**\n")
                    cat_file.write("\n")
                    for exa_idx, exapack in enumerate(exapacks_found):
                        cat_file.write("    - " + exapack + "\n")

                    cat_file.write("\n")
                    # Qui bisogna disegnare un separatore, solo se il materiale non è l'ultimo materiale di tutti

                    # if total_mat_idx != writing_mat_index:
                    #     cat_file.write("\n")
                    #     cat_file.write("-" * 120 + "\n")
                    #     cat_file.write("\n")
                    #     cat_file.write("\n")


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
            material_dict[exapack_vol_name].append(
                mat_name.replace(".png", "").replace(".jpg", "").replace(".webp", ""))

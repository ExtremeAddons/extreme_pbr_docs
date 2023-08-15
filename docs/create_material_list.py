# Questo script deve prendere tutti i file di preview contenuti in EXTREMEPBR_DEFAULT_LIBRARY e creare una pagina rst di
# nome "material_list" i preview PNG devono essere convertiti in webp con compressione al 50% e spostati nella cartella
# material_list della documentazione


import os


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


    if not os.path.isdir(material_list_folder):
        os.mkdir(material_list_folder)

    # Crea l'intestazione nella pagina con il nome Material List

    with open(material_list_rst, "w") as f:
        name = "Material List"
        f.write(name + "\n")
        f.write("=" * len(name) + "\n")
        f.write("\n")
        f.write("-" * 120 + "\n")
        f.write("\n")

        for cat in os.listdir(extreme_pbr_lib_folder):
            cat_folder = os.path.join(extreme_pbr_lib_folder, cat)
            if not os.path.isdir(cat_folder):
                continue

            if cat.startswith("."):
                continue
            cat_tile = cat.title() + " (Category)"
            f.write(cat_tile + "\n")
            f.write("-" * len(cat_tile) + "\n")
            f.write("\n")

            # Create

            # create category folder inside material_list_folder if not exists
            category_folder = os.path.join(material_list_folder, clean_name(cat))
            if not os.path.isdir(category_folder):
                os.mkdir(category_folder)

            for mat in os.listdir(cat_folder):
                mat_folder = os.path.join(cat_folder, mat)

                data_folder = os.path.join(mat_folder, "data")
                if not os.path.isdir(data_folder):
                    print("Esco qui 1")
                    continue

                if mat.startswith("."):
                    print("Esco qui 2")
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

                preview_png = next((os.path.join(default_folder, fn) for fn in os.listdir(default_folder) if fn.endswith(".png") or fn.endswith(".jpg") or fn.endswith(".webp")), None)
                if not preview_png:
                    continue

                mat_fn = clean_name(mat)
                # convert preview_png to webp
                from PIL import Image
                new_preview_webp = mat_fn + ".webp"
                if not os.path.isfile(os.path.join(material_folder, new_preview_webp)):
                    new_preview_webp_path = os.path.join(material_folder, new_preview_webp)
                    im = Image.open(preview_png)
                    im.save(new_preview_webp_path, "webp", quality=50)

                mat_title = mat.title()
                f.write(mat_title + "\n")
                f.write("*" * len(mat_title) + "\n")
                f.write("\n")
                f.write(".. image:: _static/_images/material_list/" + clean_name(cat) + "/" + clean_name(mat) + "/" + new_preview_webp + "\n")
                f.write("    :width: 30%\n")
                f.write("    :align: center\n")
                f.write("    :alt: " + mat_title + "\n")
                f.write("\n")









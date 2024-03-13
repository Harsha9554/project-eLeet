import sys
import os


def get_insert_data(url):
    file_name = url.split("/")[-1]
    file_name = file_name.replace(".py", "")
    return f"def {file_name}():\n\tpass"


# def get_excalidraw_path(url):
#     url = url.replace("leets", "scribbles")
#     url = url.replace(".py", ".excalidraw.png")
#     return url


def make_path(url):
    default_path = "/home/harsha9554/code/projects/active/project-eLeet/"
    defautl_excalidraw_path = "/mnt/c/Users/Sai SriHarsha G/iCloudDrive/iCloud~md~obsidian/harsha's-vault/excalidraw/project-eleet/"
    attach_path = url[url.index("src") :]
    final_leet_path = default_path + attach_path
    return (
        final_leet_path,
        defautl_excalidraw_path,
        attach_path.replace(".py", ".excalidraw.md").split("/")[-1].split("_")[-1],
    )
    # final_excalidraw_path = default_path + get_excalidraw_path(attach_path)
    # return final_leet_path, final_excalidraw_path


lp, ep, ap = make_path(sys.argv[1])
os.system(f"touch {lp}")
print("leet-created.")
os.chdir(ep)
os.system(f"touch {ap}")
print(ep)
print(ap)
print("excal-created.")

# lp, ep = make_path(sys.argv[1])
# with open(lp, "w", encoding="utf-8") as fp:
#     fp.write(get_insert_data(lp))
# os.system(f"touch {ep}")
# print("scribble-created.")

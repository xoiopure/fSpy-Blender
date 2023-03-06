import glob
import os
import zipfile

src_dir_name = 'fspy_blender'
init_file_path = os.path.join(src_dir_name, '__init__.py')
with open(init_file_path) as init_file:
    version_parts = []
    for line in init_file:
        if '"version":' in line:
            version_string = line.split("(")[1]
            version_string = version_string.split(")")[0]
            version_parts = version_string.split(",")
            version_parts = map(str.strip, version_parts)
            break
if len(version_parts) == 0:
    raise f"Could not extract version number from {init_file_path}"

dist_archive_name = "fSpy-Blender-" + ".".join(version_parts) + ".zip"

dist_dir_name = "dist"

if not os.path.exists(dist_dir_name):
    os.makedirs(dist_dir_name)

zipf = zipfile.ZipFile(
    os.path.join(dist_dir_name, dist_archive_name),
    'w',
    zipfile.ZIP_DEFLATED
)

for py_file in glob.glob(os.path.join(src_dir_name, '*.py')):
    zipf.write(py_file)

zipf.close()


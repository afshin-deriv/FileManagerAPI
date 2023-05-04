from flask import Flask, request, jsonify
import os
import shutil
import urllib.request
import zipfile

app = Flask(__name__)

# List all files/folders on instance/folder
@app.route('/list_files')
def list_files():
    path = request.args.get('path')
    file_list = os.listdir(path)
    return jsonify({'files': file_list})

# Delete files
@app.route('/delete_files', methods=['DELETE'])
def delete_files():
    path = request.args.get('path')
    file_list = request.get_json()['files']
    for file in file_list:
        os.remove(os.path.join(path, file))
    return jsonify({'message': 'Files deleted successfully'})

# Rename files
@app.route('/rename_files', methods=['PUT'])
def rename_files():
    path = request.args.get('path')
    old_file_name = request.get_json()['old_file_name']
    new_file_name = request.get_json()['new_file_name']
    os.rename(os.path.join(path, old_file_name), os.path.join(path, new_file_name))
    return jsonify({'message': 'File renamed successfully'})

# Move files
@app.route('/move_files', methods=['PUT'])
def move_files():
    src_path = request.args.get('src_path')
    dst_path = request.args.get('dst_path')
    file_list = request.get_json()['files']
    for file in file_list:
        shutil.move(os.path.join(src_path, file), os.path.join(dst_path, file))
    return jsonify({'message': 'Files moved successfully'})

# Create new html and text files
@app.route('/create_files', methods=['POST'])
def create_files():
    path = request.args.get('path')
    file_type = request.get_json()['file_type']
    file_name = request.get_json()['file_name']
    if file_type == 'html':
        with open(os.path.join(path, file_name), 'w') as f:
            f.write('<html><head><title></title></head><body></body></html>')
    elif file_type == 'txt':
        with open(os.path.join(path, file_name), 'w') as f:
            f.write('')
    return jsonify({'message': 'File created successfully'})

# Transfer files from a website URL to the server (via HTTP or FTP, ideally HTTP)
@app.route('/transfer_files', methods=['POST'])
def transfer_files():
    path = request.args.get('path')
    file_url = request.get_json()['file_url']
    file_name = os.path.basename(file_url)
    urllib.request.urlretrieve(file_url, os.path.join(path, file_name))
    return jsonify({'message': 'File transferred successfully'})

# Zip multiple files
@app.route('/zip_files', methods=['POST'])
def zip_files():
    path = request.args.get('path')
    zip_name = request.get_json()['zip_name']
    file_list = request.get_json()['files']
    with zipfile.ZipFile(os.path.join(path, zip_name), 'w') as zipf:
        for file in file_list:
            zipf.write(os.path.join(path, file), file)
    return jsonify({'message': 'Files zipped successfully'})

if __name__ == '__main__':
    app.run(debug=True, port=8080)


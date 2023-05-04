File Manager API

This API provides functionality to manage files and folders on a server using HTTP requests. The API is accessible via cURL or any other HTTP client tool.

List all files/folders on instance/folder

This endpoint lists all the files and folders in a specified directory on the server.

Endpoint: /list_files

HTTP Method: GET

Parameters:

path (required): The path to the directory to list.
Example:
curl http://localhost:5000/list_files?path=/path/to/folder

Delete files
This endpoint deletes one or more files from a specified directory on the server.

Endpoint: /delete_files

HTTP Method: DELETE

Parameters:

path (required): The path to the directory that contains the files to delete.
files (required): A list of file names to delete.
Request Body:

{
    "files": [
        "file1.txt",
        "file2.txt"
    ]
}

Example:

curl -X DELETE -H "Content-Type: application/json" -d '{"files":["file1.txt","file2.txt"]}' http://localhost:5000/delete_files?path=/path/to/folder


Rename files
This endpoint renames a file in a specified directory on the server.

Endpoint: /rename_files

HTTP Method: PUT

Parameters:

path (required): The path to the directory that contains the file to rename.
Request Body:

{
    "old_file_name": "file1.txt",
    "new_file_name": "newfile.txt"
}

Example:


curl -X PUT -H "Content-Type: application/json" -d '{"old_file_name":"file1.txt","new_file_name":"newfile.txt"}' http://localhost:5000/rename_files?path=/path/to/folder

Move files
This endpoint moves one or more files from one directory to another on the server.

Endpoint: /move_files

HTTP Method: PUT

Parameters:

src_path (required): The path to the source directory that contains the files to move.
dst_path (required): The path to the destination directory where the files will be moved.
Request Body:

{
    "files": [
        "file1.txt",
        "file2.txt"
    ]
}

Example:


curl -X PUT -H "Content-Type: application/json" -d '{"files":["file1.txt","file2.txt"]}' http://localhost:5000/move_files?src_path=/path/to/src&dst_path=/path/to/dst

Create new html and text files
This endpoint creates a new HTML or text file in a specified directory on the server.

Endpoint: /create_files

HTTP Method: POST

Parameters:

path (required): The path to the directory where the new file will be created.
Request Body:

{
    "file_name": "newfile.txt",
    "file_content": "This is the content of the file."
}

Example:
curl -X POST -H "Content-Type: application/json" -d '{"file_name":"newfile.txt","file_content":"This is the content of the file."}' http://localhost:500


Transfer files from a website URL to the server

This endpoint transfers a file from a website URL to the server.

Endpoint: /transfer_files

HTTP Method: POST
Parameters:
url (required): The URL of the file to transfer.
path (required): The path to the directory where the transferred file will be saved.

Example:

curl -X POST http://localhost:5000/transfer_files?url=https://example.com/file.txt&path=/path/to/folder


Zip multiple files
This endpoint creates a ZIP archive containing multiple files in a specified directory on the server.

Endpoint: /zip_files

HTTP Method: POST
Parameters:
path (required): The path to the directory that contains the files to zip.

Request Body:


{
    "files": [
        "file1.txt",
        "file2.txt"
    ],
    "zip_name": "archive.zip"
}

Example:

curl -X POST -H "Content-Type: application/json" -d '{"files":["file1.txt","file2.txt"],"zip_name":"archive.zip"}' http://localhost:5000/zip_files?path=/path/to/folder


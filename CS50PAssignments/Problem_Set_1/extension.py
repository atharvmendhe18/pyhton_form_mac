user_file = input("name: ").split(".")
user_file_ext = user_file[1]
if user_file_ext == 'gif':
    print('image/gif')
elif user_file_ext == 'jpg':
    print('image/jpg')
elif user_file_ext == 'jpeg':
    print('image/jpeg')
elif user_file_ext == 'png':
    print('image/png')
elif user_file == 'pdf':
    print('application/pdf')
elif user_file_ext == 'txt':
    print('text/plain')
elif user_file_ext == 'zip':
    print('application/zip')
else:
    print('application/octet-stream')

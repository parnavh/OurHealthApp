from firebase_admin import credentials, storage, initialize_app

cred = credentials.Certificate('./credentials.json')
initialize_app(cred, {
    'storageBucket': 'ourhealthapp-ca43a.appspot.com'
})

def upload(filename, file, user):
    try:
        bucket = storage.bucket()
        blob = bucket.blob(f'{user}/{filename}')
        blob.upload_from_filename(file)
        return True
    except Exception as err:
        print(err)
        return False

def delete_file(filename, user):
    try:
        bucket = storage.bucket()
        blob = bucket.blob(f'{user}/{filename}')
        blob.delete()
        return True
    except Exception as err:
        print(err)
        return False
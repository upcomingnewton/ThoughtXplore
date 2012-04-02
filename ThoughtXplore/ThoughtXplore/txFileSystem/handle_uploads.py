

def handle_uploaded_file(f):
    dest='/home/sarvpriye/git/ThoughtXplore/ThoughtXplore/ThoughtXplore/txFileSystem/uploadedcontent/'
    dest+=f.name
    destination = open(dest, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
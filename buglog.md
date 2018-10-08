# Bug and Issues faced during development

##### Issue #1
```
  File "c:\users\asus\appdata\local\programs\python\python36\lib\site-packages\flask\app.py", line 1813, in full_dispatch_request
    rv = self.dispatch_request()
  File "c:\users\asus\appdata\local\programs\python\python36\lib\site-packages\flask\app.py", line 1799, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "F:\Work\profiles\mashups.github.io\Flask\app.py", line 34, in upload_file
    aud,sr = librosa.load(os.path.join(app.config['UPLOAD_FOLDER'],filename))
  File "c:\users\asus\appdata\local\programs\python\python36\lib\site-packages\librosa\core\audio.py", line 112, in load
    with audioread.audio_open(os.path.realpath(path)) as input_file:
  File "c:\users\asus\appdata\local\programs\python\python36\lib\site-packages\audioread\__init__.py", line 116, in audio_open
    raise NoBackendError()
audioread.NoBackendError
```
##### Fix
```
![](https://github.com/librosa/librosa/issues/390#issuecomment-359517517)
Hi everyone! I had struggled with this error for long time and I've figured out what was the problem is. Essentially, you have to make sure that the ffmpeg library is available to python by publishing its location in the environment variables. To be sure its fine, open a new shell / cmd line window and type ffmpeg -version to see its details. If the result is seen as the installed version you can now run python to execute librosa calls.
Hope it helps.
```
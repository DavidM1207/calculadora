[app]
# (str) Title of your application
title = MyApplication

# (str) Package name
package.name = myapplication

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py is located
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to include (let empty to include all the files)
source.dir = .\

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# Please note that we use the Python 3 specifier for Buildozer
requirements = python3,kivy,kivymd,pillow

# (str) OS X Kivy version to use
osx.kivy_version = 1.11.1

# (int) Android API to use
android.api = 29

# (int) Minimum API allowed by the application
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 29

# (int) Android NDK version to use
android.ndk = 21e

# (str) Android architecture
android.arch = armeabi-v7a

[buildozer]
# (int) Log level (0 = error only, 1 = warn, 2 = info, 3 = debug (default), 4 = trace)
log_level = 2

# (bool) Warn on root access
warn_on_root = 1

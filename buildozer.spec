# buildozer.spec
[app]
title = HelloWorld
package.name = helloworld
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.3.0
orientation = portrait
osx.python_version = 3
osx.kivy_version = 2.3.0
fullscreen = 0
p4a.branch = stable
p4a.recursive_clone = False
p4a.private_dir = ./private
android.api = 33
android.minapi = 21
android.ndk = 23b
android.sdk = 33
android.ant = False
android.gradle_dependencies =
android.enable_androidx = True
android.add_src =
android.permissions = INTERNET
android.allow_backup = True
android.manifest_landscape_orientation = False
android.manifest_portrait_orientation = True
android.release_keystore = $(HOME)/.buildozer/keys/helloworld.keystore
android.release_keystore_alias = myalias
android.release_keystore_password = mypassword
android.release_keystore_alias_password = mypassword
android.ndk_shared = False
android.bootstrap = sdl2
android.entitlements =
android.intent_filters =
android.ios_sdk_version =
android.ios_arch =

[buildozer]
log_level = 2
warn_on_root = 1

[app]
title = Glicemia

package.name = glicemia

package.domain = org.carlos

source.dir = .

source.include_exts = py,kv,png,jpg,ttf

version = 1.0

# Adicione 'openpyxl' e 'et_xmlfile' (dependência comum do openpyxl) 
requirements = python3==3.10, kivy==2.2.1, kivymd==1.2.0, pillow, pyjnius, openpyxl, et_xmlfile

fullscreen = 0

android.api = 31

android.minapi = 21

android.sdk = 31

android.ndk = 23b

android.build_tools = 30.0.3

android.archs = arm64-v8a

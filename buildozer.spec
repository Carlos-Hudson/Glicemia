[app]
title = Glicemia

package.name = glicemia

package.domain = org.carlos

source.dir = .

source.include_exts = py,kv,png,jpg,ttf

version = 1.0

# Adicione 'openpyxl' e 'et_xmlfile' (dependência comum do openpyxl) 
requirements = python3, kivy==2.2.1, kivymd==1.2.0, pillow, pyjnius, openpyxl, et_xmlfile

fullscreen = 0

android.api = 33

android.minapi = 24

android.archs = arm64-v8a, armeabi-v7a
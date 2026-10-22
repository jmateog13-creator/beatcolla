# Genera index.html (pàgina completa per a GitHub Pages) a partir de beatcolla.html
import re, pathlib
src = pathlib.Path(__file__).with_name('beatcolla.html').read_text()
title = re.search(r'<title>.*?</title>', src).group(0)
src = src.replace(title, '', 1)
head = ('<!doctype html>\n<html lang="ca">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
        '<meta name="description" content="BeatColla: crea música per capes en català. Per a 1r d\'ESO.">\n'
        + title + '\n<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}'
        'body{margin:0;font:14px system-ui,sans-serif}img{max-width:100%}[hidden]{display:none!important}</style>\n</head>\n<body>\n')
out = pathlib.Path(__file__).with_name('index.html')
out.write_text(head + src + '\n</body>\n</html>\n')
print('ok', out)

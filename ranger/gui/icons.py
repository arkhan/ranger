# -*- coding: utf-8 -*-
# This file is part of ranger, the console file manager.
# License: GNU GPL version 3, see the file "AUTHORS" for details.

"""Nerd Font icon mappings synced from yazi theme.toml.

All glyphs use explicit Unicode escape sequences so they survive any
copy/paste or encoding transformation.

Nerd Fonts codepoint ranges used:
  \\ue000-\\ue0ff  Powerline / Powerline Extra
  \\ue200-\\ue2ff  Font Awesome Extension
  \\ue600-\\ue6ff  Seti-UI + devicons
  \\ue700-\\ue7ff  devicons (continued)
  \\uf000-\\uf2ff  Font Awesome (fa-)
  \\uf300-\\uf3ff  Font Logos
  \\uf400-\\uf4ff  Octicons (oct-)
  \\uf500-\\uf8ff  Material Design subset / misc
  \\U000fXXXX     Nerd Fonts v3 supplementary (md- icons)
"""

from __future__ import absolute_import

# ---------------------------------------------------------------------------
# Default / fallback icons
# ---------------------------------------------------------------------------
ICON_DIRECTORY = '\uf07b'       # nf-fa-folder
ICON_DIRECTORY_LINK = '\uf482'  # nf-oct-file_symlink_directory
ICON_FILE = '\uf15b'            # nf-fa-file
ICON_FILE_LINK = '\uf481'       # nf-oct-file_symlink_file
ICON_LINK_BAD = '\uf127'        # nf-fa-chain_broken  (orphan symlink)
ICON_EXEC = '\uf489'            # nf-oct-terminal
ICON_FIFO = '\uf731'            # nf-fa-exchange (pipe)
ICON_SOCKET = '\uf6ff'          # nf-fa-plug
ICON_BLOCK = '\uf0a0'           # nf-fa-hdd_o

# Separator appended after the icon (thin space works well with NF v3)
ICON_SEPARATOR = ' '

# ---------------------------------------------------------------------------
# Icons by directory name  (lowercase basename -> glyph)
# ---------------------------------------------------------------------------
ICONS_BY_DIRNAME = {
    # Version control
    '.git':         '\ue702',   # nf-dev-git
    '.github':      '\uf408',   # nf-oct-mark_github
    '.svn':         '\uf408',
    '.hg':          '\uf408',
    # Package managers / build
    'node_modules': '\ue60c',   # nf-dev-javascript
    '.npm':         '\ue60c',
    # Python
    '.venv':        '\ue606',   # nf-dev-python
    'venv':         '\ue606',
    '__pycache__':  '\ue606',
    # Misc build
    'build':        '\uf187',   # nf-fa-archive
    'dist':         '\uf187',
    'target':       '\uf187',
    '.cache':       '\uf187',
    # Config / system
    '.config':      '\ue615',   # nf-custom-settings
    '.local':       '\ue615',
    '.ssh':         '\uf023',   # nf-fa-lock
    '.gnupg':       '\uf023',
    '.docker':      '\ue7b0',   # nf-dev-docker
    '.trash':       '\uf1f8',   # nf-fa-trash
    'trash':        '\uf1f8',
    # XDG user dirs
    'desktop':      '\uf108',   # nf-fa-desktop
    'documents':    '\uf02d',   # nf-fa-book
    'downloads':    '\uf019',   # nf-fa-download
    'music':        '\uf001',   # nf-fa-music
    'pictures':     '\uf03e',   # nf-fa-picture_o
    'photos':       '\uf03e',
    'public':       '\uf064',   # nf-fa-share
    'videos':       '\uf03d',   # nf-fa-film
    'movies':       '\uf03d',
    'library':      '\uf02d',
    'development':  '\uf121',   # nf-fa-code
}

# ---------------------------------------------------------------------------
# Icons by exact filename  (lowercase -> glyph)
# ---------------------------------------------------------------------------
ICONS_BY_FILENAME = {
    # Version control
    '.gitattributes':           '\ue702',
    '.gitconfig':               '\ue702',
    '.gitignore':               '\ue702',
    '.gitmodules':              '\ue702',
    '.git-blame-ignore-revs':   '\ue702',
    '.gitkeep':                 '\ue702',
    '.hgignore':                '\uf408',
    '.mailmap':                 '\ue702',
    'commit_editmsg':           '\ue702',
    '.gitlab-ci.yml':           '\uf296',   # nf-fa-gitlab

    # Shell config
    '.bash_profile':            '\uf489',
    '.bashrc':                  '\uf489',
    '.bash_logout':             '\uf489',
    '.profile':                 '\uf489',
    '.zprofile':                '\uf489',
    '.zshenv':                  '\uf489',
    '.zshrc':                   '\uf489',

    # Editor config
    '.editorconfig':            '\ue615',
    '.gvimrc':                  '\ue62b',   # nf-dev-vim
    '.nvimrc':                  '\ue62b',
    '.vimrc':                   '\ue62b',
    '_vimrc':                   '\ue62b',
    '_gvimrc':                  '\ue62b',

    # Linters / Formatters
    '.babelrc':                 '\ue60c',
    '.clang-format':            '\ue61d',
    '.clang-tidy':              '\ue61d',
    '.eslintignore':            '\ue60c',
    '.eslintrc':                '\ue60c',
    '.luacheckrc':              '\ue620',   # nf-dev-lua
    '.nanorc':                  '\ue62a',
    '.npmignore':               '\ue60c',
    '.npmrc':                   '\ue60c',
    '.nvmrc':                   '\ue60c',
    '.prettierrc':              '\ue60c',
    '.pylintrc':                '\ue606',
    'eslint.config.js':         '\ue60c',
    'eslint.config.ts':         '\ue60c',
    'eslint.config.mjs':        '\ue60c',
    'prettier.config.js':       '\ue60c',
    'prettier.config.ts':       '\ue60c',

    # Environment / secrets
    '.env':                     '\uf462',   # nf-oct-gear
    '.dockerignore':            '\ue7b0',   # nf-dev-docker

    # Build / Package managers
    'cmakelists.txt':           '\ue779',
    'compose.yaml':             '\ue7b0',
    'compose.yml':              '\ue7b0',
    'containerfile':            '\ue7b0',
    'docker-compose.yaml':      '\ue7b0',
    'docker-compose.yml':       '\ue7b0',
    'dockerfile':               '\ue7b0',
    'gemfile':                  '\ue21e',   # nf-dev-ruby
    'gemfile.lock':             '\ue21e',
    'gnumakefile':              '\ue779',   # nf-dev-gnu
    'go.mod':                   '\ue627',   # nf-dev-go
    'go.sum':                   '\ue627',
    'go.work':                  '\ue627',
    'gruntfile.js':             '\uf0d0',   # nf-fa-flag
    'gruntfile.ts':             '\uf0d0',
    'gulpfile.js':              '\uf0f9',
    'gulpfile.ts':              '\uf0f9',
    'justfile':                 '\uf013',   # nf-fa-gear
    'makefile':                 '\ue779',
    'mix.lock':                 '\ue62d',   # nf-dev-elixir
    'package-lock.json':        '\ue60c',
    'package.json':             '\ue60c',
    'pkgbuild':                 '\uf303',   # nf-fa-linux
    'pom.xml':                  '\ue738',   # nf-dev-java
    'procfile':                 '\uf013',
    'rakefile':                 '\ue21e',
    'vagrantfile':              '\ue7b0',
    'workspace':                '\ue22b',   # nf-fa-briefcase

    # CI
    '.travis.yml':              '\ue77e',   # nf-dev-travis
    'jenkinsfile':              '\ue767',   # nf-dev-jenkins

    # Frameworks
    'next.config.js':           '\ue60c',
    'next.config.ts':           '\ue60c',
    'nuxt.config.js':           '\ue6a0',   # nf-dev-vue
    'nuxt.config.ts':           '\ue6a0',
    'svelte.config.js':         '\ue697',   # nf-dev-svelte
    'tailwind.config.js':       '\uf1e7',   # nf-fa-css3 (tailwind approx)
    'tailwind.config.ts':       '\uf1e7',
    'tsconfig.json':            '\ue628',   # nf-dev-typescript
    'vite.config.js':           '\ue7a2',   # nf-dev-vitejs (approx)
    'vite.config.ts':           '\ue7a2',
    'vitest.config.js':         '\ue7a2',
    'vitest.config.ts':         '\ue7a2',
    'playwright.config.js':     '\uf489',
    'playwright.config.ts':     '\uf489',

    # Docs / Meta
    'authors':                  '\uf007',   # nf-fa-user
    'authors.txt':              '\uf007',
    'copying':                  '\uf718',   # nf-fa-creative_commons
    'copying.lesser':           '\uf718',
    'license':                  '\uf718',
    'license.md':               '\uf718',
    'unlicense':                '\uf718',
    'readme':                   '\uf48a',   # nf-oct-markdown
    'readme.md':                '\uf48a',
    'readme.txt':               '\uf48a',
    'security':                 '\uf023',
    'security.md':              '\uf023',
    'code_of_conduct':          '\uf4be',
    'code_of_conduct.md':       '\uf4be',
    'changelog':                '\uf46a',
    'changelog.md':             '\uf46a',
    'favicon.ico':              '\uf005',   # nf-fa-star

    # Config (app-specific)
    'config':                   '\ue615',
    'mpv.conf':                 '\uf03d',   # nf-fa-film
    'tmux.conf':                '\uf489',
    'tmux.conf.local':          '\uf489',
    'hypridle.conf':            '\uf013',
    'hyprland.conf':            '\uf013',
    'hyprlock.conf':            '\uf013',
    'hyprpaper.conf':           '\uf03e',
    'i3blocks.conf':            '\uf0c9',
    'i3status.conf':            '\uf0c9',
    'xorg.conf':                '\uf17c',   # nf-fa-linux
    'node_modules':             '\ue60c',

    # Prisma
    'prisma.config.ts':         '\uf1c0',
}

# ---------------------------------------------------------------------------
# Icons by file extension  (lowercase -> glyph)
# ---------------------------------------------------------------------------
ICONS_BY_EXTENSION = {
    # --- Python ---
    'py':           '\ue606',   # nf-dev-python
    'pyc':          '\ue606',
    'pyd':          '\ue606',
    'pyi':          '\ue606',
    'pyo':          '\ue606',
    'pyw':          '\ue606',
    'pyx':          '\ue606',
    'pxd':          '\ue606',
    'ipynb':        '\ue606',

    # --- JavaScript ---
    'cjs':          '\ue60c',   # nf-dev-javascript
    'js':           '\ue60c',
    'jsx':          '\ue60c',
    'mjs':          '\ue60c',

    # --- TypeScript ---
    'cts':          '\ue628',   # nf-dev-typescript
    'mts':          '\ue628',
    'ts':           '\ue628',
    'tsx':          '\ue628',

    # --- Rust ---
    'rs':           '\ue7a8',   # nf-dev-rust

    # --- Go ---
    'go':           '\ue627',   # nf-dev-go

    # --- C / C++ ---
    'c':            '\ue61e',   # nf-dev-c
    'h':            '\ue61e',
    'cc':           '\ue61d',   # nf-dev-cpp
    'cpp':          '\ue61d',
    'cxx':          '\ue61d',
    'hh':           '\ue61d',
    'hpp':          '\ue61d',
    'hxx':          '\ue61d',
    'cppm':         '\ue61d',
    'ixx':          '\ue61d',
    'mm':           '\ue61d',

    # --- C# ---
    'cs':           '\uf031b',  # nf-md-language_csharp
    'cshtml':       '\uf031b',
    'csproj':       '\uf031b',
    'sln':          '\uf031b',

    # --- Java ---
    'java':         '\ue738',   # nf-dev-java
    'jar':          '\ue738',
    'class':        '\ue738',

    # --- Kotlin ---
    'kt':           '\ue634',   # nf-dev-kotlin
    'kts':          '\ue634',

    # --- Swift ---
    'swift':        '\ue755',   # nf-dev-swift

    # --- Dart ---
    'dart':         '\ue798',   # nf-dev-dart

    # --- Ruby ---
    'rb':           '\ue21e',   # nf-dev-ruby
    'erb':          '\ue21e',
    'gemspec':      '\ue21e',

    # --- PHP ---
    'php':          '\ue73d',   # nf-dev-php

    # --- Perl ---
    'pl':           '\ue769',   # nf-dev-perl
    'pm':           '\ue769',

    # --- Lua ---
    'lua':          '\ue620',   # nf-dev-lua
    'luac':         '\ue620',

    # --- Elixir ---
    'ex':           '\ue62d',   # nf-dev-elixir
    'exs':          '\ue62d',

    # --- Erlang ---
    'erl':          '\ue7b1',
    'hrl':          '\ue7b1',

    # --- Haskell ---
    'hs':           '\ue61f',   # nf-dev-haskell
    'lhs':          '\ue61f',

    # --- Scala ---
    'scala':        '\ue737',   # nf-dev-scala
    'sc':           '\ue737',
    'sbt':          '\ue737',

    # --- Clojure ---
    'clj':          '\ue76a',   # nf-dev-clojure
    'cljs':         '\ue76a',
    'cljc':         '\ue76a',
    'edn':          '\ue76a',

    # --- F# ---
    'fs':           '\ue7a7',
    'fsi':          '\ue7a7',
    'fsx':          '\ue7a7',

    # --- Elm ---
    'elm':          '\ue62c',   # nf-dev-elm

    # --- Crystal ---
    'cr':           '\uf048',

    # --- Nim ---
    'nim':          '\uf0e7',

    # --- Nix ---
    'nix':          '\uf313',   # nf-linux-nixos

    # --- Zig ---
    'zig':          '\uf0e7',

    # --- Shell ---
    'awk':          '\uf489',
    'bash':         '\uf489',
    'fish':         '\uf489',
    'ksh':          '\uf489',
    'ps1':          '\uf489',
    'sh':           '\uf489',
    'zsh':          '\uf489',

    # --- Web ---
    'css':          '\ue60b',   # nf-dev-css3
    'htm':          '\ue60e',   # nf-dev-html5
    'html':         '\ue60e',
    'less':         '\ue60a',   # nf-dev-less
    'sass':         '\ue603',   # nf-dev-sass
    'scss':         '\ue603',
    'svelte':       '\ue697',   # nf-dev-svelte
    'vue':          '\ue6a0',   # nf-dev-vue
    'xhtml':        '\ue60e',

    # --- Data / Config ---
    'cfg':          '\ue615',
    'conf':         '\ue615',
    'ini':          '\ue615',
    'json':         '\ue60b',
    'json5':        '\ue60b',
    'jsonc':        '\ue60b',
    'toml':         '\ue615',
    'xml':          '\ue619',   # nf-dev-xml
    'yaml':         '\ue615',
    'yml':          '\ue615',
    'env':          '\uf462',   # nf-oct-gear

    # --- Documents ---
    'doc':          '\uf1c2',   # nf-fa-file_word
    'docx':         '\uf1c2',
    'odt':          '\uf1c2',
    'rtf':          '\uf1c2',
    'xls':          '\uf1c3',   # nf-fa-file_excel
    'xlsx':         '\uf1c3',
    'ods':          '\uf1c3',
    'csv':          '\uf1c3',
    'ppt':          '\uf1c4',   # nf-fa-file_powerpoint
    'pptx':         '\uf1c4',
    'odp':          '\uf1c4',
    'pdf':          '\uf1c1',   # nf-fa-file_pdf
    'djvu':         '\uf1c1',
    'epub':         '\uf02d',   # nf-fa-book
    'cbr':          '\uf02d',
    'cbz':          '\uf02d',
    'mobi':         '\uf02d',
    'md':           '\uf48a',   # nf-oct-markdown
    'markdown':     '\uf48a',
    'mdx':          '\uf48a',
    'rst':          '\uf15c',   # nf-fa-file_text
    'txt':          '\uf15c',
    'tex':          '\uf15c',
    'bib':          '\uf15c',
    'org':          '\uf4b6',   # nf-oct-checklist
    'log':          '\uf15c',
    'nfo':          '\uf15c',

    # --- Image ---
    'ai':           '\uf1c5',   # nf-fa-file_image
    'avif':         '\uf1c5',
    'bmp':          '\uf1c5',
    'gif':          '\uf1c5',
    'heic':         '\uf1c5',
    'ico':          '\uf1c5',
    'jpeg':         '\uf1c5',
    'jpg':          '\uf1c5',
    'jxl':          '\uf1c5',
    'png':          '\uf1c5',
    'psd':          '\uf1c5',
    'svg':          '\uf1c5',
    'svgz':         '\uf1c5',
    'tif':          '\uf1c5',
    'tiff':         '\uf1c5',
    'webp':         '\uf1c5',
    'xcf':          '\uf1c5',

    # --- Video ---
    '3gp':          '\uf1c8',   # nf-fa-file_video
    'avi':          '\uf1c8',
    'flv':          '\uf1c8',
    'm4v':          '\uf1c8',
    'mkv':          '\uf1c8',
    'mov':          '\uf1c8',
    'mp4':          '\uf1c8',
    'mpeg':         '\uf1c8',
    'mpg':          '\uf1c8',
    'ogv':          '\uf1c8',
    'webm':         '\uf1c8',
    'wmv':          '\uf1c8',

    # --- Audio ---
    'aac':          '\uf1c7',   # nf-fa-file_audio
    'aif':          '\uf1c7',
    'aiff':         '\uf1c7',
    'flac':         '\uf1c7',
    'm4a':          '\uf1c7',
    'mp3':          '\uf1c7',
    'oga':          '\uf1c7',
    'ogg':          '\uf1c7',
    'opus':         '\uf1c7',
    'wav':          '\uf1c7',
    'wma':          '\uf1c7',

    # --- Archives ---
    '7z':           '\uf1c6',   # nf-fa-file_archive
    'bz':           '\uf1c6',
    'bz2':          '\uf1c6',
    'bz3':          '\uf1c6',
    'deb':          '\uf1c6',
    'gz':           '\uf1c6',
    'iso':          '\uf1c6',
    'pkg':          '\uf1c6',
    'rar':          '\uf1c6',
    'rpm':          '\uf1c6',
    'tar':          '\uf1c6',
    'tgz':          '\uf1c6',
    'txz':          '\uf1c6',
    'xz':           '\uf1c6',
    'zip':          '\uf1c6',
    'zst':          '\uf1c6',
    'apk':          '\uf1c6',
    'dmg':          '\uf1c6',
    'img':          '\uf1c6',

    # --- Database ---
    'db':           '\uf1c0',   # nf-fa-database
    'dump':         '\uf1c0',
    'sql':          '\uf1c0',
    'sqlite':       '\uf1c0',
    'sqlite3':      '\uf1c0',

    # --- Font ---
    'eot':          '\uf031',   # nf-fa-font
    'otf':          '\uf031',
    'ttf':          '\uf031',
    'woff':         '\uf031',
    'woff2':        '\uf031',

    # --- Docker ---
    'dockerfile':   '\ue7b0',

    # --- Keys / Certs ---
    'asc':          '\uf023',   # nf-fa-lock
    'cer':          '\uf023',
    'crt':          '\uf023',
    'gpg':          '\uf023',
    'key':          '\uf023',
    'pem':          '\uf023',
    'pub':          '\uf023',

    # --- Patch / Diff ---
    'diff':         '\uf440',   # nf-oct-diff
    'patch':        '\uf440',

    # --- Lock files ---
    'lock':         '\uf023',
    'lck':          '\uf023',

    # --- Misc ---
    'bat':          '\uf489',
    'bin':          '\uf17a',   # nf-fa-windows (exe)
    'exe':          '\uf17a',
    'dll':          '\uf17a',
    'so':           '\uf17a',
    'bak':          '\uf15c',
    'cache':        '\uf15c',
    'class':        '\ue738',
    'torrent':      '\uf019',   # nf-fa-download
    'wasm':         '\uf05b',
    'ics':          '\uf073',   # nf-fa-calendar
    'ifb':          '\uf073',
}


def get_icon(fobj):
    """Return the Nerd Font icon glyph for *fobj*.

    Resolution order (mirrors yazi):
      1. Exact filename match (case-insensitive)
      2. Directory name match
      3. File extension match
      4. Special file types (exec, link, fifo, socket, device)
      5. Generic dir / file fallback
    """
    basename_lower = fobj.basename.lower()

    # 1. Exact filename
    icon = ICONS_BY_FILENAME.get(basename_lower)
    if icon:
        return icon

    # 2. Directory
    if fobj.is_directory:
        if fobj.is_link:
            return ICON_DIRECTORY_LINK
        return ICONS_BY_DIRNAME.get(basename_lower, ICON_DIRECTORY)

    # 3. Broken or valid symlink
    if fobj.is_link:
        return ICON_LINK_BAD if not fobj.exists else ICON_FILE_LINK

    # 4. Extension match
    if '.' in fobj.basename:
        ext = fobj.basename.rsplit('.', 1)[-1].lower()
        icon = ICONS_BY_EXTENSION.get(ext)
        if icon:
            return icon

    # 5. Special file types
    if fobj.is_fifo:
        return ICON_FIFO
    if fobj.is_socket:
        return ICON_SOCKET
    if fobj.is_device:
        return ICON_BLOCK

    if fobj.stat and fobj.stat.st_mode & 0o111:
        return ICON_EXEC

    return ICON_FILE

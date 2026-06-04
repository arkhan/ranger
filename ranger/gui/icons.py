# -*- coding: utf-8 -*-
# This file is part of ranger, the console file manager.
# License: GNU GPL version 3, see the file "AUTHORS" for details.

"""Nerd Font icon mappings — synced from yazi theme.toml [icon] section.

Set `set nerd_font_version 3` in rc.conf when using NF v3 terminals so
that 2-cell-wide glyphs are measured correctly by widestring.py.
"""

from __future__ import absolute_import

# ---------------------------------------------------------------------------
# Icons by file extension  (lowercase key → glyph)
# Source: yazi theme.toml [icon] exts
# ---------------------------------------------------------------------------
ICONS_BY_EXTENSION = {
    # 3D / CAD
    "3gp": "",
    "3mf": "󰆧",
    "fbx": "󰆧",
    "obj": "󰆧",
    "ply": "󰆧",
    "stl": "󰆧",
    "wrl": "󰆧",
    "wrz": "󰆧",
    "brep": "󰻫",
    "dwg": "󰻫",
    "dxf": "󰻫",
    "f3d": "󰻫",
    "ifc": "󰻫",
    "ige": "󰻫",
    "iges": "󰻫",
    "igs": "󰻫",
    "skp": "󰻫",
    "sldasm": "󰻫",
    "sldprt": "󰻫",
    "slvs": "󰻫",
    "ste": "󰻫",
    "step": "󰻫",
    "stp": "󰻫",
    "blend": "󰂫",
    "scad": "",
    "gcode": "󰐫",
    "fcbak": "",
    "fcmacro": "",
    "fcmat": "",
    "fcparam": "",
    "fcscript": "",
    "fcstd": "",
    "fcstd1": "",
    "fctb": "",
    "fctl": "",

    # Archives
    "7z": "",
    "a": "",
    "apk": "",
    "bz": "",
    "bz2": "",
    "bz3": "",
    "cpio": "",
    "deb": "",
    "gz": "",
    "ko": "",
    "lib": "",
    "o": "",
    "out": "",
    "pkg": "",
    "rar": "",
    "rpm": "",
    "tar": "",
    "tgz": "",
    "txz": "",
    "xpi": "",
    "xz": "",
    "zip": "",
    "zst": "",

    # Audio
    "aac": "",
    "aif": "",
    "aiff": "",
    "ape": "",
    "flac": "",
    "m4a": "",
    "mp3": "",
    "oga": "",
    "ogg": "",
    "opus": "",
    "pcm": "",
    "spx": "",
    "wav": "",
    "wma": "",
    "wv": "",
    "wvc": "",

    # Config / Data
    "cfg": "",
    "conf": "",
    "dconf": "",
    "desktop": "",
    "env": "",
    "ini": "",
    "json": "",
    "json5": "",
    "jsonc": "",
    "plist": "",
    "properties": "",
    "toml": "",
    "xml": "󰗀",
    "xslt": "󰗀",
    "yaml": "",
    "yml": "",

    # C / C++
    "c": "",
    "h": "",
    "hh": "",
    "hpp": "",
    "hxx": "",
    "cc": "",
    "cp": "",
    "cpp": "",
    "cppm": "",
    "ccm": "",
    "cxx": "",
    "cxxm": "",
    "ixx": "",
    "mm": "",
    "xm": "",

    # C#
    "cs": "󰌛",
    "cshtml": "󱦗",
    "csproj": "󰪮",
    "razor": "󱦘",
    "xaml": "󰙳",
    "sln": "",
    "slnx": "",
    "suo": "",
    "vsix": "",

    # Clojure
    "clj": "",
    "cljc": "",
    "cljd": "",
    "cljs": "",
    "edn": "",

    # COBOL
    "cbl": "",
    "cob": "",
    "cobol": "",
    "cpy": "",

    # Crystal
    "cr": "",

    # CSS / Style
    "css": "",
    "less": "",
    "sass": "",
    "scss": "",
    "styl": "",

    # Dart
    "dart": "",

    # Database
    "db": "",
    "dump": "",
    "sql": "",
    "sqlite": "",
    "sqlite3": "",
    "mdb": "",
    "accdb": "",
    "kdb": "",
    "kdbx": "",

    # Docker
    "Dockerfile": "󰡨",
    "dockerignore": "󰡨",

    # Documents
    "bib": "󱉟",
    "cbr": "",
    "cbz": "",
    "djvu": "",
    "doc": "󰈬",
    "docx": "󰈬",
    "ebook": "",
    "epub": "",
    "fodt": "",
    "mobi": "",
    "odf": "",
    "odt": "",
    "pdf": "",
    "pod": "",
    "ps": "",
    "rmd": "",
    "rst": "",
    "rtf": "",
    "tex": "",
    "txt": "󰈙",
    "typ": "",

    # Elixir
    "ex": "",
    "exs": "",
    "eex": "",
    "heex": "",
    "leex": "",

    # Elm
    "elm": "",

    # Erlang
    "erl": "",
    "hrl": "",

    # F#
    "fs": "",
    "fsi": "",
    "fsscript": "",
    "fsx": "",

    # Fennel
    "fnl": "",

    # Fish
    "fish": "",

    # Font
    "eot": "",
    "flf": "",
    "lff": "",
    "otf": "",
    "ttf": "",
    "woff": "",
    "woff2": "",

    # Fortran
    "f90": "󱈚",

    # GLSL / Shaders
    "frag": "",
    "geom": "",
    "glsl": "",
    "vert": "",

    # Go
    "go": "",

    # GraphQL
    "gql": "",
    "graphql": "",

    # Gradle / Build
    "gradle": "",

    # Groovy
    "groovy": "",

    # Haskell
    "hs": "",
    "lhs": "",

    # HTML
    "htm": "",
    "html": "",
    "xhtml": "",

    # Image
    "ai": "",
    "avif": "",
    "bmp": "",
    "gif": "",
    "ico": "",
    "jxl": "",
    "jpeg": "",
    "jpg": "",
    "png": "",
    "psb": "",
    "psd": "",
    "svg": "󰜡",
    "svgz": "󰜡",
    "tiff": "",
    "tif": "",
    "webp": "",
    "xcf": "",

    # Java
    "java": "",
    "jar": "",
    "class": "",

    # JavaScript
    "cjs": "",
    "js": "",
    "jsx": "",
    "mjs": "",
    "spec.js": "",
    "test.js": "",

    # Julia
    "jl": "",

    # Jupyter
    "ipynb": "",

    # Kotlin
    "kt": "",
    "kts": "",

    # Lua
    "lua": "",
    "luac": "",
    "luau": "",

    # Markdown
    "md": "",
    "markdown": "",
    "mdx": "",

    # ML / OCaml
    "ml": "",
    "mli": "",

    # Nim
    "nim": "",

    # Nix
    "nix": "",

    # Nu
    "nu": "",

    # Patch / Diff
    "diff": "",
    "patch": "",

    # PDF
    "pdf": "",

    # Perl
    "pl": "",
    "pm": "",
    "t": "",

    # PHP
    "php": "",
    "blade.php": "",

    # PowerShell
    "ps1": "󰨊",
    "psd1": "󰨊",
    "psm1": "󰨊",

    # Presentations
    "fodp": "",
    "odp": "",
    "ppt": "󰈧",
    "pptx": "󰈧",

    # Prisma
    "prisma": "",

    # Python
    "py": "",
    "pyc": "",
    "pyd": "",
    "pyi": "",
    "pyo": "",
    "pyw": "",
    "pyx": "",
    "pxd": "",
    "pxi": "",

    # R
    "r": "󰟔",
    "R": "󰟔",

    # Ruby
    "rb": "",
    "erb": "",
    "gemspec": "",
    "rake": "",

    # Rust
    "rs": "",
    "rlib": "",

    # Scala
    "scala": "",
    "sc": "",
    "sbt": "",

    # Shell
    "awk": "",
    "bash": "",
    "bat": "",
    "csh": "",
    "ksh": "",
    "sh": "",
    "zsh": "",

    # Spreadsheets
    "csv": "",
    "fods": "",
    "ods": "",
    "xls": "󰈛",
    "xlsx": "󰈛",

    # SQL
    "sql": "",
    "sqlite": "",
    "sqlite3": "",

    # Svelte
    "svelte": "",

    # Swift
    "swift": "",

    # TOML
    "toml": "",

    # TypeScript
    "cts": "",
    "mts": "",
    "ts": "",
    "tsx": "",
    "spec.ts": "",
    "test.ts": "",
    "spec.tsx": "",
    "test.tsx": "",
    "d.ts": "",

    # Vala
    "vala": "",

    # Verilog / VHDL
    "sv": "󰍛",
    "svh": "󰍛",
    "v": "󰍛",
    "vh": "󰍛",
    "vhd": "󰍛",
    "vhdl": "󰍛",

    # Video
    "avi": "",
    "cast": "",
    "flv": "",
    "m4v": "",
    "mkv": "",
    "mov": "",
    "mp4": "",
    "mpeg": "",
    "mpg": "",
    "ogv": "",
    "ogx": "",
    "webm": "",
    "wmv": "",

    # Vim
    "vim": "",

    # Vue
    "vue": "",

    # WASM
    "wasm": "",

    # Zig
    "zig": "",

    # Misc
    "asc": "󰦝",
    "bak": "󰁯",
    "bin": "",
    "cache": "",
    "cert": "",
    "crt": "",
    "crdownload": "",
    "download": "",
    "dropbox": "",
    "elf": "",
    "exe": "",
    "fdmdownload": "",
    "gpg": "󰯄",
    "hex": "",
    "image": "",
    "img": "",
    "iso": "",
    "kbx": "󰯄",
    "lck": "",
    "lock": "",
    "log": "󰌱",
    "magnet": "",
    "md5": "󰕥",
    "pem": "󰷖",
    "pub": "󰷖",
    "sha1": "󰕥",
    "sha256": "󰕥",
    "sha512": "󰕥",
    "so": "",
    "torrent": "",
    "dll": "",
    "lrc": "󰨖",
    "srt": "󰨖",
    "ssa": "󰨖",
    "sub": "󰨖",
    "ass": "󰨖",
    "part": "",
    "ical": "",
    "icalendar": "",
    "ics": "",
    "ifb": "",
    "rss": "",
    "po": "",
    "pot": "",
    "strings": "",
    "qm": "",
    "nfo": "",
    "info": "",
}

# ---------------------------------------------------------------------------
# Icons by exact filename  (lowercase → glyph)
# Source: yazi theme.toml [icon] files
# ---------------------------------------------------------------------------
ICONS_BY_FILENAME = {
    # Version control
    ".gitattributes": "",
    ".gitconfig": "",
    ".gitignore": "",
    ".git-blame-ignore-revs": "",
    ".gitlab-ci.yml": "",
    ".gitmodules": "",
    ".mailmap": "󰊢",
    "commit_editmsg": "",

    # Shell config
    ".bash_profile": "",
    ".bashrc": "",
    ".zprofile": "",
    ".zshenv": "",
    ".zshrc": "",

    # Editor config
    ".editorconfig": "",
    ".gvimrc": "",
    ".nvimrc": "",
    ".vimrc": "",
    "_gvimrc": "",
    "_vimrc": "",

    # Linters / Formatters
    ".babelrc": "",
    ".clang-format": "",
    ".clang-tidy": "",
    ".codespellrc": "󰓆",
    ".eslintignore": "",
    ".eslintrc": "",
    ".luacheckrc": "",
    ".luaurc": "",
    ".nanorc": "",
    ".npmignore": "",
    ".npmrc": "",
    ".nuxtrc": "󱄆",
    ".nvmrc": "",
    ".prettierignore": "",
    ".prettierrc": "",
    ".prettierrc.cjs": "",
    ".prettierrc.js": "",
    ".prettierrc.json": "",
    ".prettierrc.json5": "",
    ".prettierrc.mjs": "",
    ".prettierrc.toml": "",
    ".prettierrc.yaml": "",
    ".prettierrc.yml": "",
    ".pylintrc": "",
    "eslint.config.cjs": "",
    "eslint.config.js": "",
    "eslint.config.mjs": "",
    "eslint.config.ts": "",
    "prettier.config.cjs": "",
    "prettier.config.js": "",
    "prettier.config.mjs": "",
    "prettier.config.ts": "",

    # Environment
    ".condarc": "",
    ".ds_store": "",
    ".env": "",
    ".env.local": "",
    ".env.example": "",
    ".gtkrc-2.0": "",
    ".justfile": "",
    ".pnpmfile.cjs": "",
    ".pre-commit-config.yaml": "󰛢",
    ".settings.json": "",
    ".SRCINFO": "󰣇",
    ".Xauthority": "",
    ".xinitrc": "",
    ".Xresources": "",
    ".xsession": "",
    "gtkrc": "",
    "weston.ini": "",
    "xdph.conf": "",
    "xorg.conf": "",
    "xsettingsd.conf": "",

    # Build / Package managers
    "build": "",
    "build.gradle": "",
    "build.zig.zon": "",
    "bun.lock": "",
    "bun.lockb": "",
    "cantorrc": "",
    "cmakelists.txt": "",
    "compose.yaml": "󰡨",
    "compose.yml": "󰡨",
    "containerfile": "󰡨",
    "docker-compose.yaml": "󰡨",
    "docker-compose.yml": "󰡨",
    "dockerfile": "󰡨",
    "gemfile": "",
    "gemfile.lock": "",
    "gnumakefile": "",
    "go.mod": "",
    "go.sum": "",
    "go.work": "",
    "gradle-wrapper.properties": "",
    "gradle.properties": "",
    "gradlew": "",
    "gruntfile.babel.js": "",
    "gruntfile.coffee": "",
    "gruntfile.js": "",
    "gruntfile.ts": "",
    "gulpfile.babel.js": "",
    "gulpfile.coffee": "",
    "gulpfile.js": "",
    "gulpfile.ts": "",
    "justfile": "",
    "makefile": "",
    "mix.lock": "",
    "package-lock.json": "",
    "package.json": "",
    "pkgbuild": "󰣇",
    "platformio.ini": "",
    "pnpm-lock.yaml": "",
    "pnpm-workspace.yaml": "",
    "pom.xml": "",
    "procfile": "",
    "rakefile": "",
    "settings.gradle": "",
    "workspace": "",

    # CI / Infra
    ".dockerignore": "󰡨",
    ".travis.yml": "",
    "jenkinsfile": "",
    "vagrantfile": "",

    # Configs (app-specific)
    "bspwmrc": "",
    "checkhealth": "󰓙",
    "commitlint.config.js": "󰜘",
    "commitlint.config.ts": "󰜘",
    "config": "",
    "fp-info-cache": "",
    "fp-lib-table": "",
    "freecad.conf": "",
    "groovy": "",
    "hypridle.conf": "",
    "hyprland.conf": "",
    "hyprlandd.conf": "",
    "hyprlock.conf": "",
    "hyprpaper.conf": "",
    "hyprsunset.conf": "",
    "i18n.config.js": "󰗊",
    "i18n.config.ts": "󰗊",
    "i3blocks.conf": "",
    "i3status.conf": "",
    "index.theme": "",
    "ionic.config.json": "",
    "kalgebrarc": "",
    "kdeglobals": "",
    "kdenlive-layoutsrc": "",
    "kdenliverc": "",
    "kritadisplayrc": "",
    "kritarc": "",
    "lxde-rc.xml": "",
    "lxqt.conf": "",
    "mpv.conf": "",
    "qtproject.conf": "",
    "sxhkdrc": "",
    "sym-lib-table": "",
    "tmux.conf": "",
    "tmux.conf.local": "",
    "vercel.json": "",
    "vlcrc": "󰕼",
    "webpack": "󰜫",
    "wrangler.jsonc": "",
    "wrangler.toml": "",
    "xmobarrc": "",
    "xmobarrc.hs": "",
    "xmonad.hs": "",

    # Frameworks
    "next.config.cjs": "",
    "next.config.js": "",
    "next.config.ts": "",
    "node_modules": "",
    "nuxt.config.cjs": "󱄆",
    "nuxt.config.js": "󱄆",
    "nuxt.config.mjs": "󱄆",
    "nuxt.config.ts": "󱄆",
    "svelte.config.js": "",
    "tailwind.config.js": "󱏿",
    "tailwind.config.mjs": "󱏿",
    "tailwind.config.ts": "󱏿",
    "tsconfig.json": "",
    "vite.config.cjs": "",
    "vite.config.cts": "",
    "vite.config.js": "",
    "vite.config.mjs": "",
    "vite.config.mts": "",
    "vite.config.ts": "",
    "vitest.config.cjs": "",
    "vitest.config.cts": "",
    "vitest.config.js": "",
    "vitest.config.mjs": "",
    "vitest.config.mts": "",
    "vitest.config.ts": "",

    # Testing
    "playwright.config.cjs": "",
    "playwright.config.cts": "",
    "playwright.config.js": "",
    "playwright.config.mjs": "",
    "playwright.config.mts": "",
    "playwright.config.ts": "",

    # Docs / Meta
    "authors": "",
    "authors.txt": "",
    "brewfile": "",
    "code_of_conduct": "",
    "code_of_conduct.md": "",
    "copying": "",
    "copying.lesser": "",
    "favicon.ico": "",
    "license": "",
    "license.md": "",
    "unlicense": "",
    "readme": "󰂺",
    "readme.md": "󰂺",
    "security": "󰒃",
    "security.md": "󰒃",

    # Prisma
    "prisma.config.mts": "",
    "prisma.config.ts": "",
}

# ---------------------------------------------------------------------------
# Icons by directory name  (lowercase → glyph)
# Source: yazi theme.toml [icon] dirs + conds
# ---------------------------------------------------------------------------
ICONS_BY_DIRNAME = {
    ".config": "",
    ".git": "",
    ".github": "",
    ".npm": "",
    "desktop": "",
    "development": "",
    "documents": "",
    "downloads": "",
    "library": "",
    "movies": "",
    "music": "",
    "pictures": "",
    "photos": "",
    "public": "",
    "videos": "",
    # Extra common dirs not in yazi (kept from original)
    ".cache": "",
    ".docker": "󰡨",
    ".gnupg": "󰯄",
    ".local": "",
    ".ssh": "󰷖",
    ".trash": "",
    ".venv": "",
    "__pycache__": "",
    "build": "",
    "dist": "",
    "node_modules": "",
    "target": "",
    "trash": "",
    "venv": "",
}

# ---------------------------------------------------------------------------
# Default / fallback icons
# ---------------------------------------------------------------------------
ICON_DIRECTORY = ""        # dir (yazi cond: dir)
ICON_DIRECTORY_LINK = ""   # dir symlink
ICON_FILE = ""             # generic file (yazi cond: !dir)
ICON_FILE_LINK = ""        # file symlink (yazi cond: link)
ICON_LINK_BAD = ""         # broken symlink (yazi cond: orphan)
ICON_EXEC = ""             # executable (yazi cond: exec)
ICON_FIFO = ""             # named pipe (yazi cond: fifo)
ICON_SOCKET = ""           # socket (yazi cond: sock)
ICON_BLOCK = ""            # block device (yazi cond: block)

# Separator appended after the icon
ICON_SEPARATOR = " "


def get_icon(fobj):
    """Return the Nerd Font icon glyph for *fobj*.

    Priority order mirrors yazi's resolution:
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
    if "." in fobj.basename:
        ext = fobj.basename.rsplit(".", 1)[-1].lower()
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

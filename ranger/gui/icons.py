# -*- coding: utf-8 -*-
# This file is part of ranger, the console file manager.
# License: GNU GPL version 3, see the file "AUTHORS" for details.

"""Nerd Font icon mappings for ranger.

Supports Nerd Fonts v2 (1-cell glyphs) and v3 (2-cell glyphs).
Set `set nerd_font_version 3` in rc.conf for NF v3 terminals.

Icon sources: - \ue000-\ue0ff  Powerline / Powerline Extra
  - \ue200-\ue2ff  Font Awesome Extension
  - \ue600-\ue6ff  Seti-UI + Custom
  - \ue700-\ue7ff  devicons
  - \uf000-\uf2ff  Font Awesome (fa-)
  - \uf300-\uf3ff  Font Logos
  - \uf400-\uf4ff  Octicons (oct-)
  - \uf500-\uf8ff  Material Design subset

Reference: https://www.nerdfonts.com/cheat-sheet
"""

from __future__ import (absolute_import, division, print_function)

# ---------------------------------------------------------------------------
# Icons by file extension (lowercase key)
# ---------------------------------------------------------------------------
ICONS_BY_EXTENSION = {
    # --- Python ---
    'py': '\ue606',   # nf-dev-python
    'pyc': '\ue606',
    'pyo': '\ue606',
    'pyi': '\ue606',
    'ipynb': '\ue606',

    # --- JavaScript / TypeScript ---
    'js': '\ue60c',   # nf-dev-javascript
    'mjs': '\ue60c',
    'cjs': '\ue60c',
    'jsx': '\ue60c',
    'ts': '\ue628',   # nf-dev-typescript
    'tsx': '\ue628',
    'mts': '\ue628',

    # --- Compiled / Systems ---
    'rs': '\ue7a8',   # nf-dev-rust
    'go': '\ue627',   # nf-dev-go
    'c': '\ue61e',   # nf-dev-c
    'h': '\ue61e',
    'cpp': '\ue61d',   # nf-dev-cpp
    'cc': '\ue61d',
    'cxx': '\ue61d',
    'hpp': '\ue61d',
    'hxx': '\ue61d',
    'cs': '\uf031b',  # nf-md-language_csharp (NF v3) / fallback \ue648
    'java': '\ue738',   # nf-dev-java
    'class': '\ue738',
    'jar': '\ue738',
    'kt': '\ue634',   # nf-dev-kotlin
    'kts': '\ue634',
    'swift': '\ue755',   # nf-dev-swift
    'zig': '\ue6a9',
    'nim': '\ue677',
    'v': '\ue6ac',

    # --- Ruby / PHP / Perl ---
    'rb': '\ue21e',   # nf-dev-ruby
    'erb': '\ue21e',
    'gemspec': '\ue21e',
    'php': '\ue73d',   # nf-dev-php
    'pl': '\ue769',   # nf-dev-perl
    'pm': '\ue769',

    # --- Functional ---
    'hs': '\ue61f',   # nf-dev-haskell
    'lhs': '\ue61f',
    'ml': '\ue67a',
    'mli': '\ue67a',
    'clj': '\ue76a',   # nf-dev-clojure
    'cljs': '\ue76a',
    'erl': '\ue7b1',   # nf-dev-erlang
    'ex': '\ue62d',   # nf-dev-elixir
    'exs': '\ue62d',
    'scala': '\ue737',   # nf-dev-scala

    # --- Shell / Scripts ---
    'sh': '\uf489',   # nf-oct-terminal
    'bash': '\uf489',
    'zsh': '\uf489',
    'fish': '\uf489',
    'ksh': '\uf489',
    'ps1': '\uebc7',   # nf-md-powershell
    'psm1': '\uebc7',
    'bat': '\uf17a',   # nf-fa-windows (bat script)
    'cmd': '\uf17a',

    # --- Web ---
    'html': '\ue60e',   # nf-dev-html5
    'htm': '\ue60e',
    'xhtml': '\ue60e',
    'css': '\ue60b',   # nf-dev-css3
    'scss': '\ue603',   # nf-dev-sass
    'sass': '\ue603',
    'less': '\ue60a',   # nf-dev-less
    'vue': '\ue6a0',   # nf-dev-vue
    'svelte': '\ue697',   # nf-dev-svelte

    # --- Data / Config ---
    'json': '\ue60b',   # reuse CSS icon (common fallback)
    'jsonc': '\ue60b',
    'json5': '\ue60b',
    'yaml': '\uf481',   # nf-oct-settings
    'yml': '\uf481',
    'toml': '\ue6b2',
    'xml': '\uf72d',   # nf-fa-code
    'csv': '\uf1c3',   # nf-fa-file_excel
    'tsv': '\uf1c3',
    'ini': '\ue615',   # nf-custom-settings
    'conf': '\ue615',
    'cfg': '\ue615',
    'properties': '\ue615',
    'env': '\uf462',   # nf-oct-gear
    'editorconfig': '\ue615',

    # --- Documents ---
    'pdf': '\uf1c1',   # nf-fa-file_pdf
    'doc': '\uf1c2',   # nf-fa-file_word
    'docx': '\uf1c2',
    'odt': '\uf1c2',
    'xls': '\uf1c3',   # nf-fa-file_excel
    'xlsx': '\uf1c3',
    'ods': '\uf1c3',
    'ppt': '\uf1c4',   # nf-fa-file_powerpoint
    'pptx': '\uf1c4',
    'odp': '\uf1c4',
    'txt': '\uf15c',   # nf-fa-file_text
    'log': '\uf15c',
    'md': '\uf48a',   # nf-oct-markdown
    'markdown': '\uf48a',
    'rst': '\uf15c',
    'org': '\uf718',   # nf-fa-creative_commons (org-mode)
    'tex': '\ue600',   # nf-dev-aptana (TeX approximation)
    'bib': '\ue600',
    'djvu': '\uf1c1',
    'epub': '\uf1c1',
    'cbz': '\uf1c1',
    'cbr': '\uf1c1',

    # --- Images ---
    'png': '\uf1c5',   # nf-fa-file_image
    'jpg': '\uf1c5',
    'jpeg': '\uf1c5',
    'gif': '\uf1c5',
    'bmp': '\uf1c5',
    'svg': '\uf1c5',
    'webp': '\uf1c5',
    'ico': '\uf1c5',
    'tiff': '\uf1c5',
    'tif': '\uf1c5',
    'psd': '\uf1c5',
    'xcf': '\uf1c5',
    'raw': '\uf1c5',
    'heic': '\uf1c5',
    'avif': '\uf1c5',

    # --- Video ---
    'mp4': '\uf1c8',   # nf-fa-file_video
    'mkv': '\uf1c8',
    'avi': '\uf1c8',
    'mov': '\uf1c8',
    'wmv': '\uf1c8',
    'flv': '\uf1c8',
    'webm': '\uf1c8',
    'm4v': '\uf1c8',
    'mpg': '\uf1c8',
    'mpeg': '\uf1c8',

    # --- Audio ---
    'mp3': '\uf1c7',   # nf-fa-file_audio
    'flac': '\uf1c7',
    'ogg': '\uf1c7',
    'wav': '\uf1c7',
    'aac': '\uf1c7',
    'm4a': '\uf1c7',
    'opus': '\uf1c7',
    'wma': '\uf1c7',
    'mid': '\uf1c7',
    'midi': '\uf1c7',

    # --- Archives ---
    'zip': '\uf1c6',   # nf-fa-file_archive
    'tar': '\uf1c6',
    'gz': '\uf1c6',
    'bz2': '\uf1c6',
    'xz': '\uf1c6',
    'zst': '\uf1c6',
    'lz4': '\uf1c6',
    'rar': '\uf1c6',
    '7z': '\uf1c6',
    'deb': '\uf1c6',
    'rpm': '\uf1c6',
    'pkg': '\uf1c6',
    'dmg': '\uf1c6',
    'iso': '\uf1c6',
    'img': '\uf1c6',
    'apk': '\uf1c6',
    'appimage': '\uf1c6',

    # --- Database ---
    'db': '\uf1c0',   # nf-fa-database
    'sql': '\uf1c0',
    'sqlite': '\uf1c0',
    'sqlite3': '\uf1c0',
    'mdb': '\uf1c0',
    'accdb': '\uf1c0',

    # --- Font ---
    'ttf': '\uf031',   # nf-fa-font
    'otf': '\uf031',
    'woff': '\uf031',
    'woff2': '\uf031',
    'eot': '\uf031',

    # --- 3D / CAD ---
    'stl': '\uf1b2',   # nf-fa-cube
    'obj': '\uf1b2',
    'fbx': '\uf1b2',
    'blend': '\ue7bd',   # nf-dev-blender (approx)

    # --- Crypto / Keys ---
    'pem': '\uf023',   # nf-fa-lock
    'key': '\uf023',
    'crt': '\uf023',
    'cer': '\uf023',
    'pub': '\uf023',
    'asc': '\uf023',
    'gpg': '\uf023',

    # --- Patch / Diff ---
    'patch': '\uf440',   # nf-oct-diff
    'diff': '\uf440',

    # --- Build / Package ---
    'lock': '\uf023',   # generic lock icon
    'sum': '\uf023',
    'wasm': '\ue7bd',
}


# ---------------------------------------------------------------------------
# Icons by exact filename (lowercase key, no path)
# ---------------------------------------------------------------------------
ICONS_BY_FILENAME = {
    # Version control
    '.gitignore': '\ue702',   # nf-dev-git
    '.gitconfig': '\ue702',
    '.gitmodules': '\ue702',
    '.gitattributes': '\ue702',
    '.gitkeep': '\ue702',
    '.hgignore': '\uf408',   # nf-oct-history
    '.svnignore': '\uf408',

    # Shell config
    '.bashrc': '\uf489',   # nf-oct-terminal
    '.bash_profile': '\uf489',
    '.bash_history': '\uf489',
    '.bash_logout': '\uf489',
    '.zshrc': '\uf489',
    '.zprofile': '\uf489',
    '.zshenv': '\uf489',
    '.profile': '\uf489',
    '.inputrc': '\uf489',
    '.fishrc': '\uf489',
    'config.fish': '\uf489',

    # Editor config
    '.vimrc': '\ue62b',   # nf-dev-vim
    '.nvimrc': '\ue62b',
    '.gvimrc': '\ue62b',
    '.vim': '\ue62b',

    # Build / Package managers
    'makefile': '\ue779',   # nf-dev-gnu
    'gnumakefile': '\ue779',
    'cmakelists.txt': '\ue779',
    'dockerfile': '\ue7b0',   # nf-dev-docker
    'docker-compose.yml': '\ue7b0',
    'docker-compose.yaml': '\ue7b0',
    '.dockerignore': '\ue7b0',
    'vagrantfile': '\ue7b0',
    'package.json': '\ue60c',   # nf-dev-javascript
    'package-lock.json': '\ue60c',
    'yarn.lock': '\ue60c',
    '.yarnrc': '\ue60c',
    '.npmrc': '\ue60c',
    '.nvmrc': '\ue60c',
    'cargo.toml': '\ue7a8',   # nf-dev-rust
    'cargo.lock': '\ue7a8',
    'pyproject.toml': '\ue606',   # nf-dev-python
    'setup.py': '\ue606',
    'setup.cfg': '\ue606',
    'requirements.txt': '\ue606',
    'pipfile': '\ue606',
    'pipfile.lock': '\ue606',
    'poetry.lock': '\ue606',
    'go.mod': '\ue627',   # nf-dev-go
    'go.sum': '\ue627',
    'gemfile': '\ue21e',   # nf-dev-ruby
    'gemfile.lock': '\ue21e',
    'rakefile': '\ue21e',
    'pom.xml': '\ue738',   # nf-dev-java
    'build.gradle': '\ue738',
    'build.gradle.kts': '\ue634',   # nf-dev-kotlin

    # Config files
    '.editorconfig': '\ue615',
    '.eslintrc': '\ue60c',
    '.eslintignore': '\ue60c',
    '.prettierrc': '\ue60c',
    '.babelrc': '\ue60c',
    'tsconfig.json': '\ue628',   # nf-dev-typescript
    '.env': '\uf462',   # nf-oct-gear
    '.env.local': '\uf462',
    '.env.example': '\uf462',

    # Docs
    'readme': '\uf48a',   # nf-oct-markdown
    'readme.md': '\uf48a',
    'readme.txt': '\uf48a',
    'readme.rst': '\uf48a',
    'license': '\uf718',   # nf-fa-creative_commons
    'licence': '\uf718',
    'copying': '\uf718',
    'authors': '\uf007',   # nf-fa-user
    'contributors': '\uf007',
    'changelog': '\uf17a',   # nf-fa-windows (change list)
    'changelog.md': '\uf48a',

    # CI / Infra
    '.travis.yml': '\ue77e',   # nf-dev-travis
    'jenkinsfile': '\ue767',   # nf-dev-jenkins
    '.github': '\ue702',   # nf-dev-git (GitHub)
    'terraform.tf': '\ue6b2',
    'ansible.cfg': '\ue6b2',
}


# ---------------------------------------------------------------------------
# Icons for special directory names (lowercase basename)
# ---------------------------------------------------------------------------
ICONS_BY_DIRNAME = {
    '.git': '\ue702',   # nf-dev-git
    '.github': '\ue702',
    '.svn': '\uf408',   # nf-oct-history
    '.hg': '\uf408',
    'node_modules': '\ue60c',   # nf-dev-javascript
    '.venv': '\ue606',   # nf-dev-python
    'venv': '\ue606',
    '__pycache__': '\ue606',
    'dist': '\uf187',   # nf-fa-archive
    'build': '\uf187',
    'target': '\uf187',
    '.config': '\ue615',   # nf-custom-settings
    '.local': '\ue615',
    '.cache': '\uf187',
    'downloads': '\uf019',   # nf-fa-download
    'documents': '\uf02d',   # nf-fa-book
    'pictures': '\uf03e',   # nf-fa-picture_o
    'photos': '\uf03e',
    'music': '\uf001',   # nf-fa-music
    'videos': '\uf03d',   # nf-fa-film
    'movies': '\uf03d',
    'desktop': '\uf108',   # nf-fa-desktop
    'trash': '\uf1f8',   # nf-fa-trash
    '.trash': '\uf1f8',
    '.ssh': '\uf023',   # nf-fa-lock
    '.gnupg': '\uf023',
    '.docker': '\ue7b0',   # nf-dev-docker
}

# ---------------------------------------------------------------------------
# Default icons
# ---------------------------------------------------------------------------
ICON_DIRECTORY      = '\uf07b'   # nf-fa-folder
ICON_DIRECTORY_LINK = '\uf482'   # nf-oct-file_symlink_directory (approx)
ICON_FILE           = '\uf15b'   # nf-fa-file
ICON_FILE_LINK      = '\uf481'   # nf-oct-file_symlink_file (approx)
ICON_LINK_BAD       = '\uf481'   # broken symlink

# Separator appended after the icon (thin space U+2009 works well with NF v3)
ICON_SEPARATOR = ' '


def get_icon(fobj):
    """Return the appropriate Nerd Font icon glyph for *fobj*.

    Falls back to generic file/directory icons when no specific match exists.
    """
    basename_lower = fobj.basename.lower()

    # 1. Exact filename match (highest priority)
    icon = ICONS_BY_FILENAME.get(basename_lower)
    if icon:
        return icon

    # 2. Directory (including dir-symlinks)
    if fobj.is_directory:
        return ICON_DIRECTORY_LINK if fobj.is_link \
            else ICONS_BY_DIRNAME.get(basename_lower, ICON_DIRECTORY)

    # 3. Symlinks: broken -> ICON_LINK_BAD, valid -> ICON_FILE_LINK
    if fobj.is_link:
        return ICON_LINK_BAD if not fobj.exists else ICON_FILE_LINK

    # 4. Extension match, with generic file fallback
    if '.' in fobj.basename:
        ext = fobj.basename.rsplit('.', 1)[-1].lower()
        return ICONS_BY_EXTENSION.get(ext, ICON_FILE)

    return ICON_FILE

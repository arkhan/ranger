# -*- coding: utf-8 -*-
# This file is part of ranger, the console file manager.
# License: GNU GPL version 3, see the file "AUTHORS" for details.
# Author: Wojciech Siewierski <wojciech.siewierski@onet.pl>, 2015

from __future__ import (absolute_import, division, print_function)

from abc import abstractproperty, abstractmethod
from datetime import datetime

from ranger.ext.abc import ABC
from ranger.ext.human_readable import human_readable, human_readable_time
from ranger.ext import spawn

try:
    from ranger.gui.icons import get_icon, ICON_SEPARATOR
    from ranger.ext.widestring import uwid as _uwid
    _ICONS_AVAILABLE = True
except ImportError:
    _ICONS_AVAILABLE = False
    _uwid = None


def _icon_prefix(icon):
    """Return icon + padding so the slot is always exactly 2 display cells.

    BMP PUA icons (U+E000-U+F8FF) are 2-cell wide under NF v3.
    Supplementary PUA icons (U+F0000+) are 1-cell wide.
    Without normalisation every row has a different prefix width, which
    misaligns the filename column.
    """
    w = _uwid(icon) if _uwid is not None else 1
    pad = ' ' * max(0, 2 - w)
    return icon + pad + ICON_SEPARATOR


DEFAULT_LINEMODE = "filename"


class LinemodeBase(ABC):
    """Supplies the file line contents for BrowserColumn.

    Attributes:
        name (required!) - Name by which the linemode is referred to by the user

        uses_metadata - True if metadata should to be loaded for this linemode

        required_metadata -
            If any of these metadata fields are absent, fall back to
            the default linemode
    """

    uses_metadata = False
    required_metadata = []

    name = abstractproperty()

    @abstractmethod
    def filetitle(self, fobj, metadata):
        """The left-aligned part of the line."""
        raise NotImplementedError

    def infostring(self, fobj, metadata):
        """The right-aligned part of the line.

        If `NotImplementedError' is raised (e.g. this method is just
        not implemented in the actual linemode), the caller should
        provide its own implementation (which in this case means
        displaying the hardlink count of the directories, size of the
        files and additionally a symlink marker for symlinks). Useful
        because only the caller (BrowserColumn) possesses the data
        necessary to display that information.

        """
        raise NotImplementedError


class DefaultLinemode(LinemodeBase):  # pylint: disable=abstract-method
    name = "filename"

    def filetitle(self, fobj, metadata):
        return fobj.relative_path


class IconLinemode(LinemodeBase):  # pylint: disable=abstract-method
    """Prepend a Nerd Font icon to the filename.

    Requires a Nerd Font (https://www.nerdfonts.com) installed and active in
    the terminal. Set `set nerd_font_version 3` in rc.conf if using NF v3
    so that 2-cell-wide glyphs are measured correctly.

    Activate with:  set linemode icons
    Or map:         map Mi linemode icons
    """
    name = "icons"

    def filetitle(self, fobj, metadata):
        if _ICONS_AVAILABLE:
            return _icon_prefix(get_icon(fobj)) + fobj.relative_path
        return fobj.relative_path


class PermissionsIconLinemode(LinemodeBase):
    """Like `permissions` linemode but with a Nerd Font icon prefix."""
    name = "permissionsicons"

    def filetitle(self, fobj, metadata):
        prefix = ""
        if _ICONS_AVAILABLE:
            prefix = _icon_prefix(get_icon(fobj))
        return "%s%s %s %s %s" % (
            prefix,
            fobj.get_permission_string(),
            fobj.user,
            fobj.group,
            fobj.relative_path,
        )

    def infostring(self, fobj, metadata):
        return ""


class TitleLinemode(LinemodeBase):
    name = "metatitle"
    uses_metadata = True
    required_metadata = ["title"]

    def filetitle(self, fobj, metadata):
        name = metadata.title
        if metadata.year:
            return "%s - %s" % (metadata.year, name)
        return name

    def infostring(self, fobj, metadata):
        if metadata.authors:
            authorstring = metadata.authors
            if ',' in authorstring:
                authorstring = authorstring[0:authorstring.find(",")]
            return authorstring
        return ""


class PermissionsLinemode(LinemodeBase):
    name = "permissions"

    def filetitle(self, fobj, metadata):
        return "%s %s %s %s" % (
            fobj.get_permission_string(), fobj.user, fobj.group, fobj.relative_path)

    def infostring(self, fobj, metadata):
        return ""


class FileInfoLinemode(LinemodeBase):
    name = "fileinfo"

    def filetitle(self, fobj, metadata):
        return fobj.relative_path

    def infostring(self, fobj, metadata):
        if not fobj.is_directory:
            from subprocess import CalledProcessError
            try:
                fileinfo = spawn.check_output(["file", "-Lb", fobj.path]).strip()
            except CalledProcessError:
                return "unknown"
            return fileinfo
        else:
            raise NotImplementedError


class MtimeLinemode(LinemodeBase):
    name = "mtime"

    def filetitle(self, fobj, metadata):
        return fobj.relative_path

    def infostring(self, fobj, metadata):
        if fobj.stat is None:
            return '?'
        return datetime.fromtimestamp(fobj.stat.st_mtime).strftime("%Y-%m-%d %H:%M")


class SizeMtimeLinemode(LinemodeBase):
    name = "sizemtime"

    def filetitle(self, fobj, metadata):
        return fobj.relative_path

    def infostring(self, fobj, metadata):
        if fobj.stat is None:
            return '?'
        if fobj.is_directory and not fobj.cumulative_size_calculated:
            if fobj.size is None:
                sizestring = ''
            else:
                sizestring = fobj.size
        else:
            sizestring = human_readable(fobj.size)
        return "%s %s" % (sizestring,
                          datetime.fromtimestamp(fobj.stat.st_mtime).strftime("%Y-%m-%d %H:%M"))


class HumanReadableMtimeLinemode(LinemodeBase):
    name = "humanreadablemtime"

    def filetitle(self, fobj, metadata):
        return fobj.relative_path

    def infostring(self, fobj, metadata):
        if fobj.stat is None:
            return '?'
        return human_readable_time(fobj.stat.st_mtime)


class SizeHumanReadableMtimeLinemode(LinemodeBase):
    name = "sizehumanreadablemtime"

    def filetitle(self, fobj, metadata):
        return fobj.relative_path

    def infostring(self, fobj, metadata):
        if fobj.stat is None:
            return '?'
        if fobj.is_directory and not fobj.cumulative_size_calculated:
            if fobj.size is None:
                sizestring = ''
            else:
                sizestring = fobj.size
        else:
            sizestring = human_readable(fobj.size)
        return "%s %11s" % (sizestring, human_readable_time(fobj.stat.st_mtime))

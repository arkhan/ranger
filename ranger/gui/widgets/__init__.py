# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function)

from ranger.gui.displayable import Displayable


class Widget(Displayable):
    """A class for classification of widgets."""

    # Default VCS symbols (plain Unicode, works without Nerd Fonts)
    vcsstatus_symb = {
        'conflict':  ('X',  ['vcsconflict']),
        'untracked': ('?',  ['vcsuntracked']),
        'deleted':   ('-',  ['vcschanged']),
        'changed':   ('+',  ['vcschanged']),
        'staged':    ('*',  ['vcsstaged']),
        'ignored':   ('·',  ['vcsignored']),
        'sync':      ('✓',  ['vcssync']),
        'none':      (' ',  []),
        'unknown':   ('!',  ['vcsunknown']),
    }

    vcsremotestatus_symb = {
        'diverged': ('Y',  ['vcsdiverged']),
        'ahead':    ('>',  ['vcsahead']),
        'behind':   ('<',  ['vcsbehind']),
        'sync':     ('=',  ['vcssync']),
        'none':     ('⌂',  ['vcsnone']),
        'unknown':  ('!',  ['vcsunknown']),
    }

    # Nerd Font v2/v3 VCS symbols — activate by calling Widget.use_nerd_font_vcs()
    # nf-dev-git=\ue702  nf-fa-check=\uf00c  nf-fa-times=\uf00d  nf-oct-x=\uf52a
    # nf-md-source_branch=\uebe6  nf-md-cloud_sync=\ueb55
    _vcsstatus_symb_nf = {
        'conflict':  ('\uf00d',  ['vcsconflict']),   # nf-fa-times
        'untracked': ('\uf128',  ['vcsuntracked']),  # nf-fa-question
        'deleted':   ('\uf014',  ['vcschanged']),    # nf-fa-trash
        'changed':   ('\uf044',  ['vcschanged']),    # nf-fa-pencil_square
        'staged':    ('\uf067',  ['vcsstaged']),     # nf-fa-plus
        'ignored':   ('\uf070',  ['vcsignored']),    # nf-fa-eye_slash
        'sync':      ('\uf00c',  ['vcssync']),       # nf-fa-check
        'none':      (' ',       []),
        'unknown':   ('\uf128',  ['vcsunknown']),    # nf-fa-question
    }

    _vcsremotestatus_symb_nf = {
        'diverged': ('\uf0e2',  ['vcsdiverged']),   # nf-fa-rotate_left (diverged)
        'ahead':    ('\uf062',  ['vcsahead']),      # nf-fa-arrow_up
        'behind':   ('\uf063',  ['vcsbehind']),     # nf-fa-arrow_down
        'sync':     ('\uf00c',  ['vcssync']),       # nf-fa-check
        'none':     (' ',       ['vcsnone']),
        'unknown':  ('\uf128',  ['vcsunknown']),    # nf-fa-question
    }

    @classmethod
    def use_nerd_font_vcs(cls):
        """Switch VCS symbols to Nerd Font glyphs."""
        cls.vcsstatus_symb = cls._vcsstatus_symb_nf
        cls.vcsremotestatus_symb = cls._vcsremotestatus_symb_nf

    @classmethod
    def use_plain_vcs(cls):
        """Restore plain-Unicode VCS symbols (default)."""
        cls.vcsstatus_symb = {
            'conflict':  ('X',  ['vcsconflict']),
            'untracked': ('?',  ['vcsuntracked']),
            'deleted':   ('-',  ['vcschanged']),
            'changed':   ('+',  ['vcschanged']),
            'staged':    ('*',  ['vcsstaged']),
            'ignored':   ('·',  ['vcsignored']),
            'sync':      ('✓',  ['vcssync']),
            'none':      (' ',  []),
            'unknown':   ('!',  ['vcsunknown']),
        }
        cls.vcsremotestatus_symb = {
            'diverged': ('Y',  ['vcsdiverged']),
            'ahead':    ('>',  ['vcsahead']),
            'behind':   ('<',  ['vcsbehind']),
            'sync':     ('=',  ['vcssync']),
            'none':     ('⌂',  ['vcsnone']),
            'unknown':  ('!',  ['vcsunknown']),
        }

    ellipsis = {False: '~', True: '…'}

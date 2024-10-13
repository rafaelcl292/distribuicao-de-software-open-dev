#!/usr/bin/env python3
import os

from babel.support import Translations

from dev_aberto.dev_aberto import hello

# Load translations
localedir = os.path.join(
    os.path.abspath(os.path.dirname(__file__)), "translations"
)
translations = Translations.load(localedir, locales=["en"])

# Set the translation function
_ = translations.gettext

if __name__ == "__main__":
    date, name = hello()
    print(
        _("Last commit made on: {date} by {name}").format(date=date, name=name)
    )

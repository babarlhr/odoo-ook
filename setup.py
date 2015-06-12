from distutils.core import setup

setup(
        name             = "ook",
        version          = "1.0.0",
        author           = "Frederic van der Essen",
        author_email     = "fvdessen+x@gmail.com",
        packages         = ["ook"],
        url              = "https://github.com/fvdsn/odoo-ook",
        license          = "MIT",
        install_requires = [
            "appdirs"
        ],
        scripts          = [
            "scripts/ook"
        ]
    )


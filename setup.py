from setuptools import find_packages, setup


setup(
    name="pyLBL",
    version="0.0.0",
    author="R. Menzel, R. Pincus",
    author_email="",
    description="Line-by-line absorption calculators.",
    url="",
    python_requires=">=3.6",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: ",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        # Required depenedencies.
        "netCDF4",
        "numpy",
        "scipy",
        "sqlalchemy",
        "xarray",
        "mt_ckd @ git+http://github.com/GRIPS-code/MT_CKD@fortran-90-and-python",
        "arts_crossfit @ git+http://github.com/menzel-gfdl/arts-crossfit@make-package",

        # To build documentation.
        "Sphinx",
        "sphinxcontrib-apidoc",
        "sphinxcontrib-napoleon",
        "sphinx-autopackagesummary",
    ],
    entry_points={
        "pyLBL" : ["Gas=pyLBL.spectral_lines:Gas",],
#       "arts": ["Gas=pyLBL.pyarts_frontend:PyArtsGas",],
#       "grtcode" : ["Gas=pygrt.gas_optics:Gas",],
#       "pyrad" : ["Gas=pyrad.optics.gas:Gas",
#                  "CrossSection=pyrad.lbl.hitran.cross_sections:HitranCrossSection",
#                  "CIA=pyrad.lbl.hitran.collision_induced_absorption:HitranCIA",
#                  "H2OForeignContinuum=pyrad.lbl.continua.water_vapor:WaterVaporForeignContinuum",
#                  "H2OSelfContinuum=pyrad.lbl.continua.water_vapor:WaterVaporSelfContinuum",
#                  "O3Continuum=pyrad.lbl.continua.ozone:OzoneContinuum",
#       ],
        "mt_ckd": ["CO2Continuum=mt_ckd.carbon_dioxide:CarbonDioxideContinuum",
                   "H2OForeignContinuum=mt_ckd.water_vapor:WaterVaporForeignContinuum",
                   "H2OSelfContinuum=mt_ckd.water_vapor:WaterVaporSelfContinuum",
                   "N2Continuum=mt_ckd.nitrogen:NitrogenContinuum",
                   "O2Continuum=mt_ckd.oxygen:OxygenContinuum",
                   "O3Continuum=mt_ckd.ozone:OzoneContinuum",
        ],
        "arts_crossfit": ["CrossSection=arts_crossfit.cross_section:CrossSection"],
    },
)

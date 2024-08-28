import setuptools
with open("Readme.md","r") as fh:
    long_description=fh.read()
setuptools.setup(
     name="MITS AIML",
     version="2023.08.28",
     author="bhargav,lokesh,yaseer",
     author_email="bhargavmc@gmail.com",
     description="this software is developed at the MITS,andhra pradesh,india",
     long_description=long_description,
     long_description_content_type= ("text/markdown"),
     packages=setuptools.find_packages(),
     url="https://github.com/bhargavmc/MITS AIML",
     license="GPLv3",
     install_requires=[
         "psutil","pandas","plotly","matplotlib","resource","validator","urllib3","pillow","numpy",
     ],
     extras_require={
         "gpu":["cupy","pycuda"],
         "spark":["pyspark"],
         "dev":["twine","setuptools","build"],
         "all":["cupy","pycuda","pyspark","twine","setuptools","build"]
     },
     classifiers=[
         "development Status :: 4 - Beta",
         "Programming Language :: Python :: 3",
         "licence:: OSI Approved :: GNU General Public License v3 (GPLv3)",
         "Operating System :: OS Independent",
     ],
     python_requires=">=3.6",
)
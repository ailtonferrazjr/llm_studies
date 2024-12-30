from setuptools import setup, find_packages

setup(
   name="llm_studies",
   version="0.1.0",
   packages=find_packages(where="src"),
   package_dir={"": "src"},
   install_requires=[
       "openai",
       "beautifulsoup4",
       "requests",
       "selenium",
       "python-dotenv"
   ],
   python_requires=">=3.11"
)
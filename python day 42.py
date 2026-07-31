#create a virtual environemnt:
"create a text file then in vs code etc or in terminal"
python -m venv myenv
#activate virtual environemnt:
myenv\Scripts\activate.bat
#to activate in powershell:
myenv\Scripts\activate.ps1
# deactivate virtual environemnt:
deactivate
# requirements.txt (to send all installed modules \ packages to another person)
pip freeze > requirements.txt
# to intall:
pip install -r requirements .txt
#just checking pandas version using pd.
import pandas as pd
print(pd. __version__)

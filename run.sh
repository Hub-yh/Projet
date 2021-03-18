pip3 install virtual env --force-reinstall
pip install --upgrade virtualenv
pip3 install pandas
if [[ ! -d ".virtualenv" ]]
then        
	virtualenv -p python3 .virtualenv
fi
source .virtualenv/bin/activate
python3 main.py


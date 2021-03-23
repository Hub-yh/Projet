pip3 install virtual env
pip333 install --upgrade virtualenv
if [[ ! -d ".virtualenv" ]]
then        
	virtualenv -p python3 .virtualenv
fi
source .virtualenv/bin/activate
pip3 install pandas
python3 main.py


# iqbal-concordance

Available at [iqbal.chaoticity.com](https://iqbal.chaoticity.com)

To run locally:
```
npm install
npm run dev
```
Then open browser on http://localhost:5173


To generate concordance files: 
```
sudo locale-gen ur_PK
sudo update-locale
locale -a # should see ur_PK here
sudo apt install python3-icu
pip install -r requirements.txt
python3 concordancer.py
```

ver=$(google-chrome --version | awk '{print $3}' | cut -d "." -f 1)
if [ $ver -eq 84 ]
then
	wget https://chromedriver.storage.googleapis.com/84.0.4147.30/chromedriver_linux64.zip
	echo "Downloaded Chromedriver for Chrome version ${ver}!"
elif [ $ver -eq 83 ]
then
	wget https://chromedriver.storage.googleapis.com/83.0.4103.39/chromedriver_linux64.zip
	echo "Downloaded Chromedriver for Chrome version ${ver}!"
elif [ $ver -eq 81 ]
then
	wget https://chromedriver.storage.googleapis.com/81.0.4044.138/chromedriver_linux64.zip
	echo "Downloaded Chromedriver for Chrome version ${ver}!"
else
	echo "Chromedriver should be manually installed for the Chrome version ${ver} available at https://chromedriver.chromium.org/downloads"
fi
unzip chromedriver_linux64.zip
sudo chmod +x chromedriver
sudo mv -f chromedriver /usr/local/share/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
rm chromedriver_linux64.zip
python3 -m pip install -r requirements.txt
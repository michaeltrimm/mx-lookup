## MX Lookup Demo

Simple python web application using Flask to lookup MX records for a provided domain name.

### Setting Up Environment

    git clone https://github.com/michaeltrimm/mx-lookup.git
    cd mx-lookup
    mkvirtualenv mx-lookup
    pip3 install -r requirements.txt


### Start Service

    python3 run.py

To quit the service, press `Ctrl-C` on the keyboard.

### JSON Only Request

    curl -X "POST" "http://localhost:8080/check" \
    	-H "Accept: application/json" \
    	-H "Content-Type: application/x-www-form-urlencoded; charset=utf-8" \
    	--data-urlencode "domain=dyn.com"


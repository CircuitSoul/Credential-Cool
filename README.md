# Credential-Cool
    The Credential-Cool tool that collects leaked credentials on the http://pwndb2am4tzkvold.onion/ website and stores it in a json file

# Requirements
      Python 3.x.x
      Pip (python 3.x)
      Tor 
   
# Install Tor service
    The installation of Tor depends on your system, and is detailed on the official website. On a Debian or Raspbian, we use:
            $ sudo apt install tor
    To launch Tor, just run:
            $ sudo service tor start
    To check if it works, simply run the following command from a terminal:
            $ curl --socks5 localhost:9050 --socks5-hostname localhost:9050 -s https://check.torproject.org/ | cat | grep -m 1 Congratulations | xargs
    This command will display:
            Congratulations. This browser is configured to use Tor.
            
# Install requirements
    $ pip3 install -r requirements.txt

# How to use
    $ python3 cc.py <example.com>

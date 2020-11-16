# Ping Provider

Ping Provider is a CLI program that tests your internet connection. It pings your internet service
provider (or DNS address provided) every second for a fixed amount of minutes, and logs the response
time in a specified output file.

## How to install
Clone the repo and change into that directory.

```bash
cd <PATH>/Ping_Provider/
```

**Note**
It is recommended you use a virtual environment.

* Install requirements from requirements.txt
  
```bash
pip install -r requirements.txt
```

* Install the package locally

```bash
pip install --editable .
```

## Running the program

```bash
sudo pingprovider --isp <ISP NAME or DNS> --minutes <NUMBER OF MINUTES>
```

# Course

## https://www.udemy.com/course/python-js-react-blockchain/

```
The course includes Python, Blockchains, Cryptocurrencies, Web Development (Backend and Frontend), JavaScript, React JS, React Hooks and more.
```

**Activate the virtual environment**
```
source blockchain-env\Scripts\activate
```

**Install all packages**
```
pip3 install -r requirements.txt
```

**Run the tests**

Make sure to activate the virtual environment.

```
python3 -m pytest backend/tests
```

**Run the application and API**

Make sure to activate the virtual environment.

```
python3 -m backend.app
```

**Run a peer instance**

Make sure to activate the virtual environment.

```
export PEER=True && python3 -m backend.app

or

$env:PEER='True'
python3 -m backend.app
```

**Run the frontend**

In the frontend directory:
```
npm run start
```

**Seed the backend with data**

Make sure to activate the virtual environment.

```
export SEED_DATA=True && python3 -m backend.app

or

$env:SEED_DATA='True'
python3 -m backend.app
```

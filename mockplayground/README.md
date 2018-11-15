
1) setup

mkdir mockplayground
cd mockplayground
virtualenv venv3 -p python3
source venv3/bin/activate
pip install --upgrade pip
pip install pytest
echo "[pytest]" >> pytest.ini
echo "norecursedirs=venv*" >> pytest.ini
mkdir tests
touch myobj.py
touch tests/test_mock.py
PYTHONPATH="." py.test

2) run tests with
$ PYTHONPATH="." py.test
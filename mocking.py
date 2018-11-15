import logging
from unittest import mock

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(process)d:%(thread)d - %(module)s:%(lineno)d - %(levelname)s - %(message)s')

def play1():
    #http://blog.thedigitalcatonline.com/blog/2016/03/06/python-mocks-a-gentle-introduction-part-1/
    m = mock.Mock()
    logging.debug(m.some_attribute)
    m.some_attribute.return_value = 42
    logging.debug(m.some_attribute())

    def print_answer():
        logging.debug("42")

    m.some_attribute.return_value = print_answer
    logging.debug(m.some_attribute())

    m.some_attribute.side_effect = ValueError('A custom value error')
    try:
        m.some_attribute()
    except:
        logging.debug('exception caught')

    m.some_attribute.side_effect = range(3)

    try:
        for i in m.some_attribute():
            logging.debug(i)
    except:
        logging.debug('not an iterator')

    logging.debug(m.some_attribute())
    logging.debug(m.some_attribute())

    try:
        logging.debug(m.some_attribute())
    except Exception:
        logging.debug("stop iteration")

    def print_number(num):
        logging.debug("number:{0}".format(num))

    m.some_attribute.side_effect = print_number
    m.some_attribute.side_effect(5)

    class Number(object):
        def __init__(self, value):
            self._value = value

        def print_value(self):
            logging.debug("Value:{0}".format(self._value))

    m.some_attribute.side_effect = Number
    n = m.some_attribute.side_effect(26)

    logging.debug(n)
    n.print_value()

if __name__ == '__main__':
    play1()
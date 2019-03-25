# -*- coding: utf-8 -*-

import sys
import time
import json
from six import StringIO, BytesIO


def basic_buffer_api():
    data = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Cathy"},
    ]

    buffer = StringIO("HelloWorld")
    value = buffer.getvalue()
    print(type(value), value)

    buffer = StringIO()
    buffer.write("Hello")
    buffer.write("World")
    value = buffer.getvalue()
    print(type(value), value)

    buffer = StringIO()
    json.dump(data, buffer)
    value = buffer.getvalue()
    print(type(value), value)


# basic_buffer_api()

def understand_buffer_usage_and_performance():
    multiplier = 1000 * 100
    big_data = data * multiplier

    # no buffer
    st = time.time()
    big_data_json = json.dumps(big_data)
    elapse = time.time() - st
    print("%.6f" % elapse)

    # write to text, then create buffer
    st = time.time()
    buffer = StringIO()
    big_data_json = json.dumps(big_data)
    buffer = StringIO(big_data_json)
    value = buffer.getvalue()
    elapse = time.time() - st
    print("%.6f" % elapse)

    # write to buffer
    st = time.time()
    buffer = StringIO()
    json.dump(big_data, buffer)
    value = buffer.getvalue()
    elapse = time.time() - st
    print("%.6f" % elapse)

    print("%s KB" % sys.getsizeof(big_data_json))


# understand_buffer_usage_and_performance()


def use_buffer_with_pandas():
    import pandas as pd

    data = [(1, "Alice"), (2, "Bob"), (3, "Cathy")]
    data = data * 100000
    df = pd.DataFrame(data, columns=["id", "name"])

    st = time.time()
    buffer = StringIO()
    df.to_csv(buffer, index=False)
    csv = buffer.getvalue()
    elapse = time.time() - st
    print("%.6f" % elapse)

    st = time.time()
    df.to_csv("data.csv", index=False)
    elapse = time.time() - st
    print("%.6f" % elapse)


# use_buffer_with_pandas()

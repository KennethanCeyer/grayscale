<h1 align="center">grayscale</h1>
<p align="center">Native performance computational toolkit for maximum performance in limited resources</p>

## What is this project?

### Thread resource restriction release

This project focuses on researching ways to circumvent Python's performance flaws, and providing native functions with stability and accuracy to run "properly" in the standard marketplace.

By bypassing the thread resource through C, the CPU bound resource is provided on the thread environment, out of the constraints of GIL. To do this, function-level reflection through PyDLL connection is entered. The target level is an interface like the one below.

**Python Thread**

```python
from concurrent import futures
import json


def my_func(url):
    return json.loads(my_json_lists)


with futures.ThreadPoolExecutor(max_workers=5) as executor:
    # This is a CPU-bound process, It will be a bottle-neck by GIL(Global Interpreter Lock)
    res = list(executor.map(my_func, my_json_lists))
```

**Grayscale Thread**

```python
from grayscale.thread import Pool
import json


def my_func(url):
    return json.loads(my_json_lists) # json pkg, my_json_lists will be refered in C(DLL) API


def Pool(workers=5) as pool:
    # This thread reflects all the reference of the function provided
    # by the user and activates the thread after cloning the C function,
    # so the user cannot write to the reference of the existing variable. However,
    # we plan to provide guidelines on how to share variables through pipes and queues.
    res = list(pool.map(my_func, my_json_lists))
```

It operates in a completely different way from the previous thread.
The above function is transferred to PyObject through DLL, converted to CallableObject and called.

**What is different?**

So far, it's like a normal thread. Importantly, all PyObjects in Callable objects are under the influence of GIL, so INCREF/DECREF may be required in C as well. However, Grayscale reflects all functions in Callable, duplicates it as a new PyObject, and creates it for each thread. In other words, all packages and references used within a thread are "cloned", which is similar to the principle of the process.

However, the process is clearly assigned a new Python Interpreter and "reruns" the code to get all the resources it needs. At this time, the code that prepares the necessary data in advance is difficult to predict and requires a lot of cost. In addition, pid is given from the operating system and context is switched by the scheduler, so additional cost is required for switching between SP (StackPointer) and PC (Program Counter). Grayscale thread

It is replicated based on the pickle of references used within the function, and everything runs on native threads. Pickle's replication is the only overhead for running a thread, and this is predictable and it is easy to control as it occurs locally only within the function to be run as a thread.

### Resource optimization

We sometimes use it in loops over 100,000 iterations without knowing how well it performs to get the standard deviation. If you repeat a list with only a small number of 5 or so elements over 100,000 times with np.std(), it is 13 times slower than the same function written in C. (C: 57ms, np.std: 2,281ms)

Therefore, this project aims to optimize and provide all calculation functions that require weight reduction to achieve efficient performance when used for general purposes.

### Hardware acceleration

For machine learning projects or data analysis, numpy and sklearn are adopted. This expands the basic data type of python to handle large vector operations stably, but it does not fully utilize the given resources, and unnecessary memory waste occurs in the process of boxing and unboxing.

This project creates an inline assembly in C language to test the functions of AVX, tests the experimental functions of BLAS, SIMD, and SSE, and plans to upgrade the functions to a level that can be used at the commercial level.

### User-friendly interface

The function we want to use is very simple, but wasn't there a case where the project documentation was too complex or there were too many functions to even start? This project is an experimental project that puts the user's experience first. We do our best to make everything from function design to documentation seamless, simple and intuitive.

## Performances

Performance code: [main.py](https://github.com/KennethanCeyer/grayscale/blob/main/main.py)

Function | Data Size | Hit        | Python(3.9)      | Clang
:-------:|----------:|-----------:|-----------------:|-----------------:
sum      | 5,000     | 10         |     0.2503ms     |     0.5932ms
sum      | 5,000     | 100        |     2.4950ms     |     5.3709ms
sum      | 5,000     | 1,000      |    25.9339ms     |    54.5022ms
sum      | 5,000     | 5,000      |   130.2577ms     |   295.1121ms
sum      | 5,000     | 10,000     |   261.4358ms     |   559.4767ms
sum      | 5,000     | 100,000    |  2638.4197ms     |  5475.1927ms
mean     | 5,000     | 10         |     0.3519ms     |     0.5587ms
mean     | 5,000     | 100        |     2.4620ms     |     5.5887ms
mean     | 5,000     | 1,000      |    24.7765ms     |    55.1612ms
mean     | 5,000     | 5,000      |   132.4594ms     |   287.8916ms
mean     | 5,000     | 10,000     |   261.3916ms     |   557.2935ms
mean     | 5,000     | 100,000    |  2264.3831ms     |  5706.8613ms
var      | 5,000     | 10         |     9.6276ms     |     2.6688ms
var      | 5,000     | 100        |    93.0232ms     |    26.4128ms
var      | 5,000     | 1,000      |   947.7371ms     |   275.9430ms
var      | 5,000     | 5,000      |  4742.1413ms     |  1361.4284ms
var      | 5,000     | 10,000     |  9476.7556ms     |  2692.9102ms
var      | 5,000     | 100,000    | 95506.5377ms     | 26945.4650ms
std      | 5,000     | 10         |     9.6860ms     |     2.6522ms
std      | 5,000     | 100        |    94.6309ms     |    26.6898ms
std      | 5,000     | 1,000      |   931.5487ms     |   268.1115ms
std      | 5,000     | 5,000      |  4734.4382ms     |  1361.0979ms
std      | 5,000     | 10,000     |  9431.5443ms     |  2702.1994ms
std      | 5,000     | 100,000    | 94582.3715ms     | 27095.2179ms

## Roadmap

### Computation Operators
- [x] sum
- [x] mean
- [x] var
- [x] std
- [ ] median
- [ ] floor
- [ ] ceil
- [ ] exp
- [ ] log2
- [ ] log10
- [ ] matmul
- [ ] inner
- [ ] outer
- [ ] prod
- [ ] transpose
- [ ] tile
- [ ] shape
- [ ] dot
- [ ] all
- [ ] any
- [ ] isnan
- [ ] create
- [ ] ones
- [ ] min
- [ ] max
- [ ] reshape

### Threading
- [ ] Pool
    - [ ] map
    - [ ] reduce
    - [ ] stream
    - [ ] async/await support (Allow other coroutines to occupy while the pool is waiting)
- [ ] fork
- [ ] join

### Parallel (OMP based)
- [ ] Pool
    - [ ] map
    - [ ] reduce
    - [ ] stream
    - [ ] async/await support (Allow other coroutines to occupy while the pool is waiting)

### Parallel (AsyncIO based)
- [ ] Pool
    - [ ] map
    - [ ] reduce
    - [ ] stream

### CUDA

- [ ] add
- [ ] substract
- [ ] floor
- [ ] ceil
- [ ] log2
- [ ] log10
- [ ] matmul
- [ ] divide
- [ ] dot
- [ ] exp
- [ ] prod
- [ ] all
- [ ] any
- [ ] isnan

### Example

**Machine Learning**

- [ ] MNIST Training Example (w/o ML Framework)
- [ ] Transformer iterative matmul calculation
- [ ] Batch Inferencing Parallelization

**Computing**

- [ ] Serialize/deserialize in 10 million protobuf thread environments
- [ ] Microphone voice background thread pipeline processing
- [ ] Distributed Web Server Worker

**Data Engineering**

- [ ] Large web crawl
- [ ] Parallelize data processing

## Reference

- [grayscale c lib](https://github.com/KennethanCeyer/grayscale_c)

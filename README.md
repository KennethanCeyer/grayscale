<h1 align="center">grayscale</h1>
<p align="center">Native performance computational toolkit for maximum performance in limited resources</p>

## Performances

Performance code: [main.py](https://github.com/KennethanCeyer/grayscale/blob/main/main.py)

Function | Data Size | Hit        | Python           | Clang
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

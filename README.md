# Python Fractal

This project consists in creating a [Sierpinski](https://en.wikipedia.org/wiki/Sierpinski_triangle) triangle using Turtle module. Based on the given number of levels, the program makes recursive calls to create a multi level [fractal](https://en.wikipedia.org/wiki/Fractal). This is an exercise developed during [CITS1401](http://teaching.csse.uwa.edu.au/units/CITS1401/) in 2014.


## Getting Started

Make sure you have [Python](https://www.python.org/) installed. This project is working on Ubuntu 16.04 with Python 2.7 without any issues. It also work on Python 3.X.

### Prerequisites

If you just have installed Python you might not have [TkInter](https://wiki.python.org/moin/TkInter). Tkinter is Python's de-facto standard GUI (Graphical User Interface) package. I have to install it on my Ubuntu using:

```
sudo apt-get install python-tk
```

Note: make sure you follow the right installation guide for your operational system.

## Running

```
python runner.py fractal_level window_size
```
Note: Both parameters are optional.

**fractal_level**: number of repetitions in this fractal. Default value is 2 and it must be integer.
**window_size**: size of the Turtle's window in pixels. Default value is 480 and it must be integer.

## Contributing

```
git clone git@github.com:tmmgarcia/frac-turtle.git
cd frac-turtle/
git checkout -b your-feature
git push --set-upstream origin origin/your-feature
git commit -am "feature description"
git push origin your-feature   
# make a pull request
```

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Author

* **Tiago Garcia** - [tmmgarcia](https://github.com/tmmgarcia)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

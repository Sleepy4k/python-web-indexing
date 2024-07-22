# Python Web Indexing

So in here i make a script for search data from spesific domain, for example
i want to gain data about "chocolate" on web with domain "wikipedia.com",
this script will automate your searching by listing all domain inside urls file

## Installation

Dependencies

```bash
- requests
- beautifulsoup4
```

Install Dependencies

```bash
pip install -r ./requirements.txt
```

Run program

```bash
python main.py
```

## Configuration

After running this program you may ask "why urls output feels weird, how to fix it?",
Basically you can set it to strict mode go to "config/url.py", set must start with to true
and enable domain on must contain, result will be optimized,
but keep it mind urls output must be less from bare minimum or standard config

## Update

Maybe some of you asking "how to search data from all website?",
For now, you can search data only providing a keyword without giving a spesific domain.
On domain input section, you can provide '*' as a wildcard,
script will automatic read it as search from all website domain

## Unit Test

Run Unit Test

```bash
python test.py
```

## Notes

This program only use for educational purpose, please use this on your own


Run shell commands more easily in python.

# Example usage with string interpolation enabled

- see test.py
  - You can use `s['{a} {b}']` to have interpolated strings.
  - You can use shell-style environment variables like `$HOME`.

- compile

```bash
python compile.py test.py
```

- run your script

```bash
./test.py
```

# Example usage without string interpolation

Just write your python script, importing pysh and run normally.

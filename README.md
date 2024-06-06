# ephemtxt: an ephemeral text box
`ephemtxt.py` launches a window containing a monospace text box and nothing
else. You can't open or save your text. Great for temporarily storing text,
bad for just about anything else.

## installing and running
```
$ pip install git+https://github.com/fellerts/ephemtxt.git
$ ephemtext
```
No python 3.12 support, sorry.

Suggestion for i3/sway users: The following binds `$mod+s` to open `ephemtxt` in
floating mode under your cursor.
```
bindsym $mod+s exec ephemtxt
for_window [class="ephemtxt"] floating enable, border pixel 0, move position mouse
```
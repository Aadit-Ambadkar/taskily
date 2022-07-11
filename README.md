# Taskily

I really struggle with keeping organized. Like really really struggle. I noticed that around 3 years ago, and decided to start taking steps to fix that. I starting planning each day with a schedule. Fastforward to now and my computer dies everytime I open the spreadsheet containing all of my daily plans (also I ran out of drive space twice). Instead of making a new spreadsheet, I decided to create a terminal app because working with commands is so much more natural to me.

And now, I introduce: **Taskily**

### Features
Look at the source code!
```yaml
Usage: taskily [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  append   Add to the end of the Task List
  init     Create a new Task List for Today
  insert   Insert at an index of the Task List
  list     Display the Task List
  remove   Remove a Task (at an index) from the Task List
  replace  Replace one Task with another
  sinsert  Split a Task and Insert inbetween the Task at an index of the...
```

For command specific help, run `taskily <command> --help`

### Installation
**Make sure you have all necessary requirements installed (click, prettytable)**

* If you want to keep the file readable, run `bash py_install.sh` (Recommended as it's faster)
    * Note that this method requires python to be installed on the computer that the file is run on, so don't transfer the file to other computers
    * Note that by default, this script makes the cli use `/usr/bin/env python`, ie the environment python. To make the script use a fixed python (ex: `/usr/bin/python3`) navigate to `cli.py` and change `#!/usr/bin/env python` to `#!<path-to-python>`
* If you want to conver the file to an executable, run `bash exe_install.sh` (Not recommended as it's slower)

### Contributions / Modifications

* If you would like to contribute, feel free to fork this and open a PR.
* If you would like to modify, please make sure to adhere to the Modified MIT License.
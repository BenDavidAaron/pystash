# pystash
CLI based secret keeper (for fun not audited)

## Why?

Just for Fun, wanted to try my hand at an encrypted storage service.

Keys are generated from user-supplied passwords, not properly salted, 
and _NOT_ secure. 
Please use an audited cryptosystem if you have to store bonafide secrets. 
Maybe I'll add GPG integration one day and this can be a serious secret keeper.

## How?

It's pretty simple:

### Setup

install it:
```
pip[x] install https://github.com/BenDavidAaron/pystash.git
```
specify a storage directory (optional, defaults to `appdirs.user_data_dir()`)
```
export PYSTASH_ROOT=~/.secrets/pystash
```
initalize your store with a password you can remember:
```
pystash init
-> *MY_PASSWORD*
```

### Usage:
You can put secrets by name, and you can store secrets from multiple sources:

Via shell with `--val S3CRE7`
```
pystash put a_secret --val S3CRE7
```

Masked entry with `-v`
```
pystash put a_secret -v
secret: ******
```

From env vars with `-e MY_SECRET`
```
export MY_SECRET=S3CRE7
pystash put a_secret -e MY_SECRET
```

From files with `-f ./my-secret.txt`
```
echo S3CRE7 > ./my_secret.txt
pystash put a_secret -f ./my_secret.txt
```

From system clipboard with `-c`
```
echo S3CRE7 | pbcopy
pystash put a_secret -c
```

You can retrieve secrets to multiple destinations as well:

To stdout via `-v`
```
pystash get a_secret -v
```

to clipboard via `-c`
```
pystash get a_secret -c
```

to a file via `-f`
```
pystash get a_secret -f ./a_secret.txt
```

You can delete secrets with a command as well:
```
pystash delete a_secret
```

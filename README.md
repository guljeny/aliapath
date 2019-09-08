# jsaliapath

## install

`Plug 'guljeny/aliapath'`

## Usage

place cursor in line with path ad then type
`:OpenPath`

## set up entries

default is
```vim script
let g:aliapath_entries = {^\(.*\)$': '\1.js'}
```

for example

```vim script
let g:aliapath_entries = {'^utils\(.*\)$': './apps/utils\1.js'}
```

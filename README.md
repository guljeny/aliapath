# aliapath

![Prewiew](/demo/demo.gif)

**serch aliases from vim startup directory**

## Install

`Plug 'guljeny/aliapath'`

## Usage

place cursor in line with path and type `:OpenPath`

## Tips

> Work slowly? Try to exclude large folders ex `node_modules` etc.

``` vimscript
:set wildignore+=**/node_modules/**
:set wildignore+=**/tmp/**
:set wildignore+=**/bin/**
:set wildignore+=**/cache/**
:set wildignore+=**/db/**
```

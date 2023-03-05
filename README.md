# Aliapath

Very fast way open relative and aliased imports in VIM.

[Install plugin](#install), place cursor on the line with path and type `:OpenPath`. That's all! 

For more details see [How it works](#how-it-works).

![Prewiew](/demo/demo.gif)

## Why is fast?
As search core there used [The Silver Searcher](https://github.com/ggreer/the_silver_searcher) which is defenetly fast 💫

## Install
- Install [The Silver Searcher](https://github.com/ggreer/the_silver_searcher)

  `brew install the_silver_searcher`
- Install [FZF vim plugin](https://github.com/junegunn/fzf#as-vim-plugin)

  `Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }`
- Install this plugin

  `Plug 'guljeny/aliapath'`
- Enjoy 🔥

# How it works

Place cursor on the line with path and type `:OpenPath`.

Plugin understand as path any string wrapped in `'` or `"`.

> Relative (starts from `./` or `../`) and absolute (starts from `/`) paths will be open imediately.

If only one file with name (last part of path, `baz` in `foo/bar/baz`) found, this file will be opened.

If there some files with the same name (`baz.js` and `baz.css`) - you will see the file picker window.

- Use `CTRL-K` / `CTRL-J` to navigate up / down in this window.
- Use `Enter` to open file.
- For more details check [Using FZF](https://github.com/junegunn/fzf#using-the-finder) docs.

## Tips

> Still slowly? Try to create alias?

``` vimscript
map <leader>o :OpenPath<CR>
```

function OpenPath ()
  let dir = getcwd()

  let path = substitute(getline("."), '^.\{-}[''|"]\(.*\)[''|"].*', '\1', "")
  if len(path) == 0
    echo "don`t find path in line"
    return
  endif
  if path !~ '^[a-zA-Z\.]'
    let path = strcharpart(path, 1, len(path) - 1)
  endif
  let src = split(path, "/")
  let name = remove(src, len(src) - 1)
  if path == '^\.'
    let src = join(src, "/")."/"
    let file = findfile(name, src)
    if len(file) == 0
      let file = findfile('index', src.name)
    endif
  else
    let src = join(src, '/**/').'/**/'
    let file = findfile(name, dir.'/**/'.src)
    if len(file) == 0
      let file = findfile('index', dir.'/**/'.src.name)
    endif
  endif
  if len(file) == 0
    echo "don`t find file for: `".path."`!"
    return
  endif
  if filereadable(file)
    execute "e " . fnameescape(file)
  endif
endfunction

command! OpenPath call OpenPath()

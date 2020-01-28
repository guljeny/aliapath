let g:aliapath_entries = {'^\(.*\)$': '\1.js'}

function OpenPath ()
  let filename = expand('%:e') 
  if filename != 'js'
    return
  endif

  let path = substitute(getline("."), '^.\{-}[''|"]\(.*\)[''|"].*', '\1', "")
  if path != '^[\.\w]'
    let path = strcharpart(path, 1, len(path) - 1)
  endif
  let src = split(path, "/")
  let name = remove(src, len(src) - 1)
  let src = join(src, "/") . "/"
  let file = findfile(name, src)
  if filereadable(file)
    execute "e " . fnameescape(path)
  endif
endfunction

command! OpenPath call OpenPath()

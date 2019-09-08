let g:aliapath_entries = {'^\(.*\)$': '\1.js'}

function OpenPath ()
  let filename = expand('%:e') 
  if filename != 'js'
    return
  endif

  normal! vi"
  normal! "zy

  let filepath = @z

  for conf in items(g:aliapath_entries)
    if matchstr(filepath, conf[0]) != ""
      let path = substitute(filepath, conf[0], conf[1], "g")
      if filereadable(path)
        execute "e " . fnameescape(path)
        return
      endif
    endif
  endfor
endfunction

command! OpenPath call OpenPath()
